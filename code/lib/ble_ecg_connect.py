#!/usr/bin/env python3
import datetime
import csv
import sys
from lib.ble_connection import BLEConnection
from lib.data_processor import DataProcessor
from lib.constants import (
    DEVICE_ADDRESSES,
    SAMPLES_PER_CHANNEL_ECG,
    ECG_SAMPLING_PERIOD,
    SKIP_NUM
)

def get_device_config(device_id="DEVICE_1"):
    """Get device configuration based on device ID."""
    device_address = DEVICE_ADDRESSES[device_id]
    num_channels = 5 if device_id == "DEVICE_1" else 2
    return device_address, num_channels

def initialize_components(device_address, num_channels):
    """Initialize all required components."""
    ble = BLEConnection(device_address)
    processor = DataProcessor(num_channels)
    
    time_stamp = datetime.datetime.now()
    delta_time = datetime.timedelta(seconds=1/ECG_SAMPLING_PERIOD)
    
    return ble, processor, time_stamp, delta_time

def setup_csv_file(filename, num_channels):
    """Setup CSV file with appropriate headers."""
    headers = ['ecg1', 'ecg2', 'ecg3', 'ecg4', 'ecg5', 'tstamp'][:num_channels + 1]
    f = open(filename, 'w')
    writer = csv.writer(f)
    writer.writerow(headers)
    return f, writer

def collect_data(ble, processor, writer, time_stamp, delta_time):
    """Collect and process data from BLE device."""
    counter = 0
    
    while True:
        raw_data = ble.get_data()
        ch_val = processor.process_channel_data(raw_data)
        
        # Update timestamps
        time_vals = [time_stamp + (i * delta_time) for i in range(SAMPLES_PER_CHANNEL_ECG)]
        time_stamp = time_vals[-1]
        
        if counter >= SKIP_NUM:
            for i in range(SAMPLES_PER_CHANNEL_ECG):
                data_row = [ch_val[j,i] for j in range(processor.num_channels)]
                data_row.append(time_vals[i].isoformat())
                writer.writerow(data_row)
        else:
            counter += 1

def main():
    try:
        # Get device configuration
        device_address, num_channels = get_device_config("DEVICE_1")
        
        # Initialize components
        ble, processor, time_stamp, delta_time = initialize_components(
            device_address, 
            num_channels
        )
        
        # Reset and connect BLE device
        ble.reset_connection()
        ble.connect()
        
        # Setup CSV file
        f, writer = setup_csv_file(
            'ECG_Data_{}.csv'.format(
                datetime.datetime.now().strftime('%Y%m%d_%H%M')
            ),
            num_channels
        )
        
        try:
            # Start data collection
            collect_data(ble, processor, writer, time_stamp, delta_time)
        finally:
            f.close()
            
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nInterrupted')
        sys.exit(0)
 
 
 
 
 

