#!/usr/bin/env python3
"""
BLE ECG Data Collection Script

This script interfaces with a BLE ECG device to collect ECG data.
It handles device connection, data collection, and CSV file management.

Author: Nicholas Antoniades
"""

import datetime
import sys
from lib.ble_connection import BLEConnection
from lib.data_processor import DataProcessor
from lib.file_manager import FileManager
from lib.constants import (
    DEVICE_3,
    DEVICE_ADDRESSES,
    ECG_SAMPLING_PERIOD,
    NUM_CHANNELS_3LEAD,
    NUM_CHANNELS_6LEAD,
    SAMPLES_PER_CHANNEL_ECG
)

def get_device_config(mode):
    """Configure device settings based on the selected mode."""
    if mode == '3-lead':
        device_id = DEVICE_3
        num_channels = NUM_CHANNELS_3LEAD
    elif mode == '6-lead':
        device_id = "DEVICE_6"  # Assuming DEVICE_6 is defined in constants
        num_channels = NUM_CHANNELS_6LEAD
    else:
        raise ValueError("Invalid mode selected. Choose '3-lead' or '6-lead'.")
    
    device_address = DEVICE_ADDRESSES[device_id]
    return device_address, num_channels, device_id

def initialize_components(device_address, num_channels, device_id):
    """Initialize all required components."""
    file_manager = FileManager('Test', 'Brain-Beta-v1-1', device_id)
    data_processor = DataProcessor(num_channels)
    ble_connection = BLEConnection(device_address)
    
    time_stamp = datetime.datetime.now()
    delta_time = datetime.timedelta(seconds=1/ECG_SAMPLING_PERIOD)
    
    return file_manager, data_processor, ble_connection, time_stamp, delta_time

def main(mode):
    """Main execution function."""
    device_address, num_channels, device_id = get_device_config(mode)
    file_manager, data_processor, ble_connection, time_stamp, delta_time = initialize_components(
        device_address, num_channels, device_id
    )
    
    try:
        # Connect to device
        if not ble_connection.connect():
            print("Failed to connect to device")
            return
            
        # Setup data collection
        write_count, writer, f = file_manager.get_next_available_file(time_stamp)
        
        # Collect data
        ble_connection.collect_data(data_processor, writer, time_stamp, delta_time, f)
        
    except Exception as e:
        print(f"Error during execution: {str(e)}")
    finally:
        if 'f' in locals():
            f.close()

if __name__ == "__main__":
    try:
        mode = sys.argv[1] if len(sys.argv) > 1 else '3-lead'
        main(mode)
    except KeyboardInterrupt:
        print('\nInterrupted')
        sys.exit(0)

