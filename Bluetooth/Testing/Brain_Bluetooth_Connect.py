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
   
    DEVICE = "48:23:35:00:36:1B"
    print("Hexiwear address:"),
    print(DEVICE + '\n')
   
    # Run gatttool interactively.
    print("Running gatttool...")
    child = pexpect.spawn("gatttool -I")
   
    # Connect to the device.
    print("Connecting to ")
    print(DEVICE + '\n')
 
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
                print("Error \' \' ")
                time.sleep(0.5)
                print("Error ----")
                time.sleep(0.5)
 
    # Set MTU
    child.sendline('mtu 240')
 
    # Stream data
    child.sendline('char-write-req 0x001d 0100')
    child.expect("Notification handle = 0x001c value:", timeout=1)
 
    # open the file in the write mode
    f = open('Sticky_Hips_EP4_20222202_1044.csv', 'w')
   
    # create the csv writer
    writer = csv.writer(f)
   
    # write an initial row to the csv file
    Initial_data=['ecg1', 'ecg2', 'ecg3','ecg4', 'ecg5', 'tstamp']
    writer.writerow(Initial_data)
   
    # Fetch date and time
    time_stamp = datetime.datetime.now()
    deltaTime = (datetime.timedelta(seconds=(1 / 500)))
    
    # Create array to hold timestamp for each sample
    Rows_Time_val, Cols_Time_val = (10, 1)
    Time_val = [Cols_Time_val]*Rows_Time_val
   
    # Initialise the arrays for the data to be organised into.
    Rows_CH_bytes, Cols_CH_bytes = (50, 1)
    CH_bytes = [Cols_CH_bytes]*Rows_CH_bytes
    CH_converted_val = [Cols_CH_bytes]*Rows_CH_bytes
   
    # Make scaleable
    CH_Num, Rows_CH_val, Cols_CH_val = (5, 10, 1)
    CH_val = np.array([[Cols_CH_val]*Rows_CH_val]*CH_Num, dtype=float)
    
    # Loop counter, used to skip writing the first n measurements to .csv
    counter = 0
    n = 10

    while True:
        # Request and listen for data
        child.expect("Notification handle = 0x001c value:", timeout=10)
        
        x, i = (0,0)
        
        # Convert data from 3 byte values to a single 24 bit value
        for i in range(1,450,9):
            CH_bytes[x] = (child.before[i:i+2]),(child.before[i+3:i+5]),(child.before[i+6:i+8])
            CH_converted_val[x] = bytes_to_data(CH_bytes[x])
            x = x + 1      
       
       # Insert values into respective channels while simultaneosly converting it to voltage.
        for h in range(0,CH_Num):
            x = 0
            for j in range(h,50,5):
                CH_val[h,x] = raw_to_ecg(CH_converted_val[j])
                x = x + 1  
       
        # Create array of time stamps
        for i in range(0,10):
            time_stamp = time_stamp + deltaTime
            Time_val[i] = time_stamp.isoformat()
           
        # Write all the data to a csv
        data_to_write = [1]*6

        # Skip writing first n items to .csv
        if counter >= n:
            for i in range(0,10):
                # Write channel data values with a times tamp
                for j in range(0,CH_Num):
                    data_to_write[j]=CH_val[j,i]
                data_to_write[CH_Num] = Time_val[i]
                print(data_to_write)
                writer.writerow(data_to_write)    
        else:
            counter = counter + 1
           
if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print('')
            print('Interrupted')
            sys.exit(0)
       
       
 
 
 
 
 

