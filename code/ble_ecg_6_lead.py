#!/usr/bin/env python3
"""
BLE ECG 6-Lead Data Collection Script

This script interfaces with a BLE ECG device to collect 6-lead ECG data.
It handles device connection, data collection, and CSV file management.

Author: Nicholas Antoniades
"""

import sys
from lib.constants import (
    DEVICE_ADDRESSES,
    SAMPLES_PER_CHANNEL_ECG,
    ECG_SAMPLING_PERIOD,
    SKIP_NUM,
    GPIO_CONFIG
)
from lib.ble_connection import BLEConnection
from lib.data_processor import DataProcessor
from lib.file_manager import FileManager
from lib.gpio_manager import GPIOManager

def get_device_config():
    """Configure device settings based on device ID."""
    device_id = "DEVICE_3"  # 3-lead ECG device, latest hardware
    device_address = DEVICE_ADDRESSES[device_id]
    num_channels = 5 if device_id == "DEVICE_1" else 2
    
    return device_address, num_channels, device_id

def initialize_components(device_address, num_channels, device_id):
    """Initialize all required components."""
    # Initialize GPIO
    gpio_manager = GPIOManager(GPIO_CONFIG)
    gpio_manager.reset_device()
    
    # Initialize other components
    file_manager = FileManager('Nanoleq_Nick', 'Device_3', device_id)
    data_processor = DataProcessor(num_channels)
    ble_connection = BLEConnection(device_address)
    
    return file_manager, data_processor, ble_connection, gpio_manager

def main():
    """Main execution function."""
    device_address, num_channels, device_id = get_device_config()
    
    try:
        # Initialize components
        file_manager, data_processor, ble_connection, gpio_manager = initialize_components(
            device_address, num_channels, device_id
        )
        
        # Connect to device
        if not ble_connection.connect():
            print("Failed to connect to device")
            return
            
        while True:
            # Setup data collection
            write_count, writer, f = file_manager.get_next_available_file()
            
            try:
                # Collect data
                ble_connection.collect_data(
                    data_processor,
                    writer,
                    file_manager.time_stamp,
                    file_manager.delta_time,
                    f
                )
            except Exception as e:
                print(f"\nError during data collection: {str(e)}")
                if f:
                    f.close()
                break
                
    except KeyboardInterrupt:
        print('\nProgram terminated by user')
    finally:
        gpio_manager.cleanup()
        sys.exit(0)

if __name__ == "__main__":
    main()

