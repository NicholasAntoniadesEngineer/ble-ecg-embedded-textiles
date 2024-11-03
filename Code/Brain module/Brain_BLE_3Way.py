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
    Device_3 = "CC:86:EC:65:E4:DC"
    Toms_Brain = "CC:86:EC:65:E4:E9"
    
    # Fetch date and time
    time_stamp = datetime.datetime.now()
    deltaTime = (datetime.timedelta(seconds=(1 / 500)))
    
    # Create array to hold timestamp for each sample
    Rows_Time_val, Cols_Time_val = (10, 1)
    Time_val = [Cols_Time_val]*Rows_Time_val
   
    # Initialise the variables and arrays for the data to be organised into.
    Num_Channels     = 2 
    Num_Samples      = 10
    Num_Values       = Num_Channels*Num_Samples
    Bytes_per_value  = 3
    Total_bytes      = Bytes_per_value*Num_Values*3 ## Why multiply by 3??
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
    
    DEVICE = Device_3
    print("Hexiwear address:"),
    print(DEVICE + '\n')
   
    # Run gatttool interactively.
    print("Running gatttool...")
    child = pexpect.spawn("gatttool -I")
   
    # Connect to the device.
    print("Connecting to :", DEVICE)
    print('')
 
    # Attempt to connect to bluetooth device, loop until connected
    try:
        child.sendline("connect {0}".format(DEVICE))
        child.expect("Connection successful", timeout=0.5)
        print("Connected!" + '\n')
    except Exception:
        print("Cannot connect to bluetooth device")
        while True:
            try:
                child.sendline("connect {0}".format(DEVICE))
                child.expect("Connection successful", timeout=0.5)
                print("Connected!" + '\n')
                break
            except Exception:
                print("Attempting to connect \' \' ")
                time.sleep(0.5)
                print("Attempting to connect ----")
                time.sleep(0.5)
 
    # Set MTU
    child.sendline('mtu 250')
 
    # Stream data
    child.sendline('char-write-req 0x0016 0100')
    child.expect("Notification handle = 0x0015 value:", timeout=5)

    # open the file in the write mode
    f = open('Nanoleq_Nick_20221603_1500.csv', 'w')
   
    # create the csv writer
    writer = csv.writer(f)
   
    # write an initial row to the csv file
    Initial_data=['ecg1', 'ecg2', 'tstamp']
    writer.writerow(Initial_data)
   
    while True:
        # Request and listen for data
        child.expect("Notification handle = 0x0015 value:", timeout=5)
       
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
        data_to_write = [1]*(Num_Channels + 1)
        if WriteCount >= SkipNum:
            for l in range(0,Num_Samples):
                # Write channel data values with a times tamp
                for m in range(0,Num_Channels):
                    data_to_write[m]=CH_val[m,l]
                data_to_write[Num_Channels] = Time_val[l]
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
       
       
 
 
 
 
 

