#!/usr/bin/env python3
"""
BLE ECG 3-Lead Data Collection Script

This script interfaces with a BLE ECG device to collect 3-lead ECG data.
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
    ECG_SAMPLING_PERIOD,
    NUM_CHANNELS_3LEAD,
    SAMPLES_PER_CHANNEL_ECG
)

def initialize_components():
    """Initialize all required components."""
    file_manager = FileManager('Test', 'Brain-Beta-v1-1', DEVICE_3)
    data_processor = DataProcessor(NUM_CHANNELS_3LEAD)
    ble_connection = BLEConnection(DEVICE_3)
    
    time_stamp = datetime.datetime.now()
    delta_time = datetime.timedelta(seconds=1/ECG_SAMPLING_PERIOD)
    
    return file_manager, data_processor, ble_connection, time_stamp, delta_time

def main():
    """Main execution function."""
    file_manager, data_processor, ble_connection, time_stamp, delta_time = initialize_components()
    
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
        main()
    except KeyboardInterrupt:
        print('\nInterrupted')
        sys.exit(0)

