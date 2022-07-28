#!/usr/bin/env python

""" A Python module that connects to a Brain/Pod created by the KYMIRA R@D and intended for the Caterpillar garment.
    Connects to selected device and writes all data to a single .csv file/

Author          = "Nicholas Antoniades"
Contact         = "n.antoniades@kymira.co.uk"
Start Date      = "03/01/2022"
Last Modified   = "23/05/2022"
Status          = "Prototype"
Version         = "0.0.1"
Copyright       = "Copyright 2022, KYMIRA LTD"
"""


from re import I
import pexpect
import time
import csv
import datetime
import sys
import numpy as np
import os.path

NUM_CHANNEL_IMU          = 10 
SAMPLES_PER_CHANNEL_IMU  = 1 
SAMPLES_PER_CHANNEL_ECG  = 10
BYTES_PER_SAMPLE_ECG     = 3
BYTES_PER_SAMPLE_IMU     = 2
TOTAL_BYTES_IMU          = 20
ECG_SAMPLING_PERIOD      = 500
HEADER_BYTES_IMU         = 1
IMU_SCALE_FACTOR         = 2048
SKIP_NUM                 = 10
ADC_MAX                  = 0xF30000
V_REF                    = 2.4
NUM_LOD_CHANNELS         = 1

MTU_VALUE          = 'mtu 250'
STREAM_REQUEST_NEW = 'char-write-req 0x0016 0100'
STREAM_REQUEST_OLD = 'char-write-req 0x001d 0100'
ACK_HANDLE_NEW     = "Notification handle = 0x0015 value:"
ACK_HANDLE_OLD     = "Notification handle = 0x001c value:"

# List of previously connected devices 
DEVICE_1    = "48:23:35:00:36:1B" # 6-lead ECG device, old hardware
DEVICE_2    = "48:23:35:00:36:3E" # 6-lead ECG device, old hardware
DEVICE_3    = "CC:86:EC:65:E4:DC" # 3-lead, from Brain Beta v1.1, latest hardware
DEVICE_4    = "00:3C:84:DD:2B:F6" # 3-lead, from Brain Beta v1.1, latest hardware
DEVICE_5    = "00:3c:84:dd:2c:01" # 3-lead, from Brain Beta v1.1, latest hardware
DEVICE_6    = "00:3c:84:DA:EA:D1" # 3-lead, from Brain Beta v1.1, latest hardware
device_old = DEVICE_5

"""
Variables that may be changed start here
"""
# Use a previous device or specifiy a new device 
device_new = "" 
if device_new:
    selected_device = device_new
else:
    selected_device = device_old

# Define the test name
TEST_NAME = 'Test'
"""
Variables that may be changed end here
"""

# Initialising number of ECG channels
if selected_device == DEVICE_1:
    NUM_CHANNELS_ECG     = 5
elif selected_device == DEVICE_4:
    NUM_CHANNELS_ECG     = 2
else:    
    NUM_CHANNELS_ECG     = 2

# Initialise device name
if selected_device == device_old:
    DEVICE_NAME = 'Brain-Beta-v1-1'
else:
    DEVICE_NAME = 'Older-Version'

connection_request       = "connect {0}".format(selected_device)
total_samples_ECG        = NUM_CHANNELS_ECG*SAMPLES_PER_CHANNEL_ECG
total_samples_IMU        = NUM_CHANNEL_IMU*SAMPLES_PER_CHANNEL_IMU
total_bytes_IMU          = BYTES_PER_SAMPLE_ECG*NUM_CHANNELS_ECG*SAMPLES_PER_CHANNEL_ECG
total_bytes_IMU          = total_samples_IMU*BYTES_PER_SAMPLE_IMU
total_bytes              = total_bytes_IMU + total_bytes_IMU
single_sample_ECG        = [1]*total_samples_ECG
ECG_LOD                  = [1]
raw_ADC_ECG              = [1]*total_samples_ECG
raw_LOD_ECG              = [1]
single_sample_IMU        = [1]*total_samples_IMU

converted_voltage_ECG    = np.array([[1]*SAMPLES_PER_CHANNEL_ECG]*NUM_CHANNELS_ECG, dtype=float) 
raw_IMU                  = np.array([[1]*SAMPLES_PER_CHANNEL_IMU]*NUM_CHANNEL_IMU,  dtype=float) 
multi_axis_IMU           = np.array([[1]*SAMPLES_PER_CHANNEL_ECG]*NUM_CHANNEL_IMU,  dtype=float)
data_to_write            = [0]*(NUM_CHANNEL_IMU + NUM_CHANNELS_ECG + 1)
sampling_frequency_ECG   = 1/ECG_SAMPLING_PERIOD
attempt_counter          = 0

# Create array to hold timestamp for each sample
rows_time_val, cols_time_val = (10, 1)
time_val = [cols_time_val]*rows_time_val


def update_file_path(time_stamp):
    '''
    Creates a custom file path in the format (test name)_(device name)_(hours-minutes-sec)_(year-month/day)_(version)'
        
    Parameters:
            time_stamp(datetime): Latest time stamp

    Return:  
            file_path(str): File path as a string
    '''
    current_date = str(time_stamp.date())
    current_time = time_stamp.strftime("%-H-%S")
    version = 'v'
    file_Path = TEST_NAME+'_'+DEVICE_NAME+'_'+current_time+'_'+current_date+'_'+version
    return file_Path

def initialise_CSV(ver_counter, f):
    '''
    Initialise the CSV file for the data to be captured
        
    Parameters:
            ver_counter(int): Counts the version of the test being run 
            f(TextIOWrapper)

    Return:  
            write_count(int): Loop counter, used to skip writing the first n measurements to .csv
            writer(writer): The csv writer objec
    '''
    # Increment version counter
    ver_counter = ver_counter + 1
    # Create the csv writer object
    writer = csv.writer(f)

    # Write header for file
    file_Header=['# Recorded using POD_Data_Capture.py']
    writer.writerow(file_Header)

    # Write data/time
    time_stamp = datetime.datetime.now()
    file_Header=['# Recoreded on:     ' + str(time_stamp)]
    writer.writerow(file_Header)

    # Write device information
    file_Header=['# Device address:   ' + DEVICE_NAME]
    writer.writerow(file_Header)
    file_Header=['# Device ID:        ' + selected_device]
    writer.writerow(file_Header)
    file_Header=[]
    writer.writerow(file_Header)

    # Write header for data
    if selected_device == DEVICE_1:
        data_Header=['ECG_1', 'ECG_2', 'ECG_3','ECG_4', 'ECG_5', 'tstamp']
    else:
        data_Header=['ECG_LOD','ECG_1', 'ECG_2','A_X', 'A_Y', 'A_Z', 'G_X', 'G_Y', 'G_Z', 'M_X', 'M_Y','M_Z','M_rH', 'tstamp']
    writer.writerow(data_Header)
    # Reset write count
    write_count = 0
    return write_count,writer

def bluetooth_connect():
    '''
    Attempts connection to the selected bluetooth device
        
    Return:  
            bluetooth_data(object): Object containing the returned bluetooth data on connect.
    '''
    # Run gatttool interactively.
    print('')
    print("Running gatttool...")
    bluetooth_data = pexpect.spawn("gatttool -I")
    
    # Connect to the device.
    print("Attempting to connect to :", selected_device)
    
    # Attempt to connect to bluetooth device, loop until connected
    try:
        bluetooth_data.sendline(connection_request)
        bluetooth_data.expect("Connection successful", timeout=0.5)
        print("Connected!" + '\n')
    # If device cannot make a connection
    except Exception:
        print("Cannot connect to bluetooth device")
        print('')
        attempt_counter = 0
        while True:
            # Attempt to connect to bluetooth device, loop until connected
            try:
                bluetooth_data.sendline(connection_request)
                bluetooth_data.expect("Connection successful", timeout=0.5)
                print()
                print("Connected!")
                print(" ' ' ")
                print("'---'")
                print()
                break
            # If device cannot make a connection
            except Exception:
                print()
                print("Attempting to connect, attempt: ", attempt_counter)
                print()
                print(" ' ' ")
                print(".---.")
                attempt_counter = attempt_counter + 1
                time.sleep(0.05)
    

    # Once connected set MTU of device
    bluetooth_data.sendline(MTU_VALUE)
        
    # Enable data stream on device by sending the stream command to the device
    if selected_device == DEVICE_3 or DEVICE_4:
        bluetooth_data.sendline(STREAM_REQUEST_NEW)
        bluetooth_data.expect(ACK_HANDLE_NEW, timeout=1)
    else:
        bluetooth_data.sendline(STREAM_REQUEST_OLD)
        bluetooth_data.expect(ACK_HANDLE_OLD, timeout=1)
    return bluetooth_data
  
def ADC_to_voltage_ECG(ADC_value):
    '''
    Converts raw ECG ADC value to Voltage
        
    Parameters:
            ADC_value(int): ADC value received  

    Return:  
            voltage_ECG(double): Converted ECG voltage in mV
    '''
    convert_value = ADC_value/ADC_MAX
    convert_value = convert_value - 0.5
    convert_value = convert_value*V_REF*2
    voltage_ECG = convert_value/3.5
    return voltage_ECG

def bytes_to_data_ECG(three_bytes):
    '''
    Converts 3 bytes into a 24bit value
        
    Parameters:
            three_bytes(int): List containing 3 bytes
    Return:  
            converted_data(int): A single 24 bit value
    '''
    # Combine 3 bytes
    converted_data = (int(three_bytes[0], 16) <<16) + (int(three_bytes[1], 16) <<8) + (int(three_bytes[2], 16))
    return converted_data      
           
def bytes_to_data_IMU(two_bytes):
    '''
    Converts 2 bytes into a signed 16bit value
        
    Parameters:
            three_bytes(int): List containing 2 bytes
    Return:  
            converted_data(int): A single 16 bit value
    '''
    # Combine 2 bytes
    converted_data = (int(two_bytes[1], 16) <<8) + (int(two_bytes[0], 16))
    # 2s compliment for signed numbers
    if (converted_data > (2**15)):
        converted_data = (converted_data - 2**16)
    return converted_data 

def data_Processing(bluetooth_data):
    '''
    Process the raw ECG and ADC data and organsise into data structures 
        
    Parameters:
            bluetooth_data(object): Object containing the bluetooth data to be sorted.
    '''
    # Actual_Data = bluetooth_data.before[1:246]
    # ECG_Data = bluetooth_data.before[4:183]
    # IMU_Data = bluetooth_data.before[184:246]

    # Get lead of detection data
    ECG_LOD = (bluetooth_data.before[1:4])
    # Convert byte to dec
    raw_LOD_ECG[0] = int(ECG_LOD, 16)

    # Convert ECG data from 3 byte values to a single 24 bit value
    x = 0
    for i in range(4,183,9):
        # Grab 3 bytes per sample
        single_sample_ECG[x] = (bluetooth_data.before[i:i+2]),(bluetooth_data.before[i+3:i+5]),(bluetooth_data.before[i+6:i+8])
        # Convert sample to ADC value and add to list of converted ECG values
        raw_ADC_ECG[x] = bytes_to_data_ECG(single_sample_ECG[x])
        x = x + 1      
        
    # Insert ECG values into respective channels while simultaneosly converting it to voltage.
    for h in range(0,NUM_CHANNELS_ECG):
        x = 0
        for j in range(h,total_samples_ECG,NUM_CHANNELS_ECG):
            converted_voltage_ECG[h,x] = ADC_to_voltage_ECG(raw_ADC_ECG[j])
            x = x + 1  
        
    # Convert IMU data from 2 byte values to a single 16 bit value
    x = 0
    for i in range(184,243,6):
        # Grab 2 bytes per sample
        single_sample_IMU[x] = (bluetooth_data.before[i:i+2]),(bluetooth_data.before[i+3:i+5])
        # Convert 2 bytes to raw IMU values and account for signedness
        raw_IMU[x]= bytes_to_data_IMU(single_sample_IMU[x])
        # Convert raw IMU ADC values to accelerationss
        for i in range(0,3,1):
            multi_axis_IMU[i,x] = raw_IMU[x]/IMU_SCALE_FACTOR
        x = x + 1
        
def main():
     # Fetch date and time
    time_stamp = datetime.datetime.now()
    delta_time = (datetime.timedelta(seconds=sampling_frequency_ECG))
    file_Path = update_file_path(time_stamp)
    while True:

        # Loop counter, used to skip writing the first n measurements to .csv
        write_count = 0
        # Counter incrementing data sets
        ver_counter = 0

        bluetooth_data = bluetooth_connect()       

        # open the file in the write mode
        while True: 
            if os.path.isfile(file_Path+str(ver_counter)+'.csv'):
                ver_counter = ver_counter + 1
            else:
                f = open(file_Path+str(ver_counter)+'.csv', 'w')
                break

        write_count, writer = initialise_CSV(ver_counter, f)

        while True:
            # Request and listen for data
            try:
                if selected_device == DEVICE_3 or DEVICE_4:
                    bluetooth_data.expect("Notification handle = 0x0015 value:", timeout=1)
                else:
                    bluetooth_data.expect("Notification handle = 0x001c value:", timeout=1)   
            except Exception:
                print()
                print("Connection lost!  . .  ")
                print("                 .---.")
                print()
                f.close()
                break

            # Print raw data to terminal
            data_Processing(bluetooth_data)
        
            # Create array of time stamps
            for k in range(0,SAMPLES_PER_CHANNEL_ECG):
                time_stamp = time_stamp + delta_time
                time_val[k] = time_stamp.isoformat()    
                    
            # Skip writing first n items to .csv
            if write_count >= SKIP_NUM:
                    
                    for l in range(0,SAMPLES_PER_CHANNEL_ECG):
                        
                        # Add LOD Channel data
                        data_to_write[0]= raw_LOD_ECG[0]
                        
                        # Add ECG data to be written to the CSV file 
                        for m in range(0,NUM_CHANNELS_ECG):
                            data_to_write[NUM_LOD_CHANNELS + m]=converted_voltage_ECG[m,l]

                        # Add IMU data to be written to the CSV file
                        for m in range(0,NUM_CHANNEL_IMU):
                            data_to_write[NUM_CHANNELS_ECG + NUM_LOD_CHANNELS + m]=multi_axis_IMU[0,m]

                        # Add time stamp
                        data_to_write[12] = time_val[l]
                        # Write data to CSV file
                        writer.writerow(data_to_write)    
                        
                        # This may break everything
                        # flush()
                        
                        print(bluetooth_data.before[1:180])

            else:
                write_count = write_count + 1

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print('')
            print('Interrupted')
            sys.exit(0)
       
       
 
 
 
 
 

