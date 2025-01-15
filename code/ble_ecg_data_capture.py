#!/usr/bin/env python3
"""
BLE ECG Data Capture Script

This script runs on a Raspberry Pi 4B and connects to a BLE ECG device.
It handles device connection and data collection for ECG and IMU data.

Author: Nicholas Antoniades
Last Modified: 2024
"""

import datetime
import sys
from lib.constants import ECG_SAMPLING_PERIOD
from lib.ble_connection import BluetoothConnection
from lib.data_processor import DataProcessor
from lib.file_manager import FileManager
from lib.device_config import get_device_config

def initialize_components(selected_device, num_channels_ecg, device_name):
    """Initialize all required components for data collection."""
    test_name = 'Test'
    file_manager = FileManager(test_name, device_name, selected_device)
    data_processor = DataProcessor(num_channels_ecg)
    bluetooth_connection = BluetoothConnection(selected_device)
    
    time_stamp = datetime.datetime.now()
    delta_time = datetime.timedelta(seconds=1/ECG_SAMPLING_PERIOD)
    return file_manager, data_processor, bluetooth_connection, time_stamp, delta_time

def main():
    """Main function to run the BLE ECG data capture."""
    selected_device, device_config = get_device_config()
    
    file_manager, data_processor, bluetooth_connection, time_stamp, delta_time = initialize_components(
        selected_device, 
        device_config['num_channels'], 
        device_config['device_name']
    )
    
    while True:
        try:
            bluetooth_connection.connect()
            write_count, writer, f = file_manager.get_next_available_file(time_stamp)
            bluetooth_connection.collect_data(data_processor, writer, time_stamp, delta_time, f)
        except Exception as e:
            print(f"Error during data collection: {str(e)}")
            if f:
                f.close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nInterrupted')
        sys.exit(0)

