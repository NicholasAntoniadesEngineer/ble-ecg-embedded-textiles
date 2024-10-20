# Using Hexiwear with Python
import pexpect
import time
import RPi.GPIO as GPIO
import csv
import datetime
import sys
import numpy as np
 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
@brief Converts raw ECG ADC value to Voltage
@return state
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''    
def raw_to_ecg(value):
    ADC_MAX = 0xF30000
    V_REF = 2.4
    raw_value = value/ADC_MAX
    raw_value = raw_value - 0.5 + 0.16
    raw_value = raw_value*V_REF*2
    out_value = raw_value/3.5
    return out_value
 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
@brief Converts 3 bytes into a 24bit value
@return 24bit value
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''          
def bytes_to_data(bytes):
    data = (int(bytes[0], 16) <<16) + (int(bytes[1], 16) <<8) + (int(bytes[2], 16))
    return data        
       
def main():
    
    # Devices to connect to
    Device_1 = "48:23:35:00:36:1B" # 6-lead ECG device, old hardware
    Device_2 = "48:23:35:00:36:3E" # 6-lead ECG device, old hardware
    Device_3 = "CC:86:EC:65:E4:DC" # 3-lead ECG device, latest hardware
    DEVICE = Device_3
      
    # Fetch date and time
    time_stamp = datetime.datetime.now()
    deltaTime = (datetime.timedelta(seconds=(1 / 500)))
    
    # Create array to hold timestamp for each sample
    Rows_Time_val, Cols_Time_val = (10, 1)
    Time_val = [Cols_Time_val]*Rows_Time_val
   
    # Initialise the arrays for the data to be organised into.
    if DEVICE == Device_1:
        Num_Channels     = 5
    else:    
        Num_Channels     = 2
    
    Num_Samples      = 10
    Num_Values       = Num_Channels*Num_Samples
    Bytes_per_value  = 3
    Total_bytes      = Bytes_per_value*Num_Channels*Num_Samples*3 ## Why multiply by 3??
    CH_bytes         = [1]*Num_Values
    CH_converted_val = [1]*Num_Values
    CH_val           = np.array([[1]*Num_Samples]*Num_Channels, dtype=float)

    # Loop counter, used to skip writing the first n measurements to .csv
    WriteCount = 0
    SkipNum = 10
    
    # Initialise to GPIO mode
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    # Set GPIO24 to be CS1 pin
    CS1 = 18    
    GPIO.setup(CS1, GPIO.OUT)
    
    # Toggle power to device reseting the bluetooth connection
    GPIO.output(CS1,0)
    time.sleep(0.1)
    GPIO.output(CS1,1)
    time.sleep(0.1)
    
    # Counter incrementing data sets
    counter = 0
    
    while True:
        
        # Run gatttool interactively.
        print('')
        print("Running gatttool...")
        child = pexpect.spawn("gatttool -I")
    
        # Connect to the device.
        print("Attempting to connect to :", DEVICE)
    
        # Attempt to connect to bluetooth device, loop until connected
        try:
            child.sendline("connect {0}".format(DEVICE))
            child.expect("Connection successful", timeout=0.5)
            print("Connected!" + '\n')
        except Exception:
            print("Cannot connect to bluetooth device")
            print('')
            while True:
                try:
                    child.sendline("connect {0}".format(DEVICE))
                    child.expect("Connection successful", timeout=0.5)
                    print()
                    print("Connected!             ' '")
                    print("                      '---'")
                    print()
                    time.sleep(0.5)
                    break
                except Exception:
                    print()
                    print("Attempting to connect  . . ")
                    print("                      .---.")
                    time.sleep(0.5)
    
        # Set MTU
        child.sendline('mtu 250')
        
        # Stream data
        if DEVICE == Device_3:
            child.sendline('char-write-req 0x0016 0100')
            child.expect("Notification handle = 0x0015 value:", timeout=1)
        else:
            child.sendline('char-write-req 0x001d 0100')
            child.expect("Notification handle = 0x001c value:", timeout=1)       
        

    

        # open the file in the write mode
        f = open('Nanoleq_Nick_20221404_1140_Device_3_v'+str(counter)+'.csv', 'w')
        # Increment counter
        counter = counter + 1
        # create the csv writer
        writer = csv.writer(f)
        # write an initial row to the csv file
        Initial_data=['ecg1', 'ecg2', 'ecg3','ecg4', 'ecg5', 'tstamp']
        writer.writerow(Initial_data)
        # Reset write count
        WriteCount = 0

        while True:
            # Request and listen for data
            try:
                if DEVICE == Device_3:
                    child.expect("Notification handle = 0x0015 value:", timeout=3)
                else:
                    child.expect("Notification handle = 0x001c value:", timeout=3)   
            except Exception:
                print()
                print("Connection lost!  . .  ")
                print("                 .---.")
                print()
                f.close()
                break
                
            # Convert data from 3 byte values to a single 24 bit value
            x = 0
            for i in range(1,Total_bytes,9):
                CH_bytes[x] = (child.before[i:i+2]),(child.before[i+3:i+5]),(child.before[i+6:i+8])
                CH_converted_val[x] = bytes_to_data(CH_bytes[x])
                x = x + 1      
        
        # Insert values into respective channels while simultaneosly converting it to voltage.
            for h in range(0,Num_Channels):
                x = 0
                for j in range(h,Num_Values,Num_Channels):
                    CH_val[h,x] = raw_to_ecg(CH_converted_val[j])
                    x = x + 1  
        
            # Create array of time stamps
            for k in range(0,Num_Samples):
                time_stamp = time_stamp + deltaTime
                Time_val[k] = time_stamp.isoformat()
            
            # Skip writing first n items to .csv
            data_to_write = [0]*(5 + 1)
            if WriteCount >= SkipNum:
                for l in range(0,Num_Samples):
                    # Write channel data values with a times tamp
                    for m in range(0,Num_Channels):
                        data_to_write[m]=CH_val[m,l]
                    data_to_write[5] = Time_val[l]
                    print(data_to_write)
                    writer.writerow(data_to_write)    
            else:
                WriteCount = WriteCount + 1
                
    
if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print('')
            print('Interrupted')
            sys.exit(0)
       
       
 
 
 
 
 

