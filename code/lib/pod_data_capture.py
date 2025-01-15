#!/usr/bin/env python

"""
A Python module that connects to a BLE ECG device intended for the ECG IMU Garment Prototype.
Connects to selected device and writes all data to a single .csv file.

Author: Nicholas Antoniades
Start Date: 03/01/2022
Last Modified: 23/05/2022
"""

import datetime
import sys
import csv
import numpy as np
import pexpect
import time
from lib.constants import (
    DEVICE_ADDRESSES,
    SAMPLES_PER_CHANNEL_ECG,
    ECG_SAMPLING_PERIOD,
    SKIP_NUM
)
from lib.ble_connection import BLEConnection
from lib.data_processor import DataProcessor
from lib.file_manager import FileManager

# Configuration
device_new = ""
selected_device = device_new if device_new else DEVICE_ADDRESSES['DEVICE_5']
TEST_NAME = 'Test'
NUM_CHANNELS_ECG = 5 if selected_device == DEVICE_ADDRESSES['DEVICE_1'] else 2
DEVICE_NAME = 'Brain-Beta-v1-1' if selected_device == DEVICE_ADDRESSES['DEVICE_5'] else 'Older-Version'

def update_file_path(time_stamp):
    """Creates a custom file path."""
    current_date = str(time_stamp.date())
    current_time = time_stamp.strftime("%-H-%S")
    version = 'v'
    return f"{TEST_NAME}_{DEVICE_NAME}_{current_time}_{current_date}_{version}"

def initialize_csv(file_manager):
    """Initialize the CSV file for data capture."""
    f, writer = file_manager.get_next_available_file()
    writer.writerow(['# Recorded using POD_Data_Capture.py'])
    writer.writerow([f'# Recorded on: {datetime.datetime.now()}'])
    writer.writerow([f'# Device address: {DEVICE_NAME}'])
    writer.writerow([f'# Device ID: {selected_device}'])
    writer.writerow([])
    data_header = ['ECG_1', 'ECG_2', 'A_X', 'A_Y', 'A_Z', 'G_X', 'G_Y', 'G_Z', 'M_X', 'M_Y', 'M_Z', 'M_rH', 'tstamp']
    writer.writerow(data_header)
    return writer

def main():
    """Main function to run the POD data capture."""
    file_manager = FileManager(TEST_NAME, DEVICE_NAME, selected_device)
    data_processor = DataProcessor(NUM_CHANNELS_ECG)
    bluetooth_connection = BLEConnection(selected_device)

    writer = initialize_csv(file_manager)
    if not bluetooth_connection.connect():
        return

    try:
        while True:
            raw_data = bluetooth_connection.get_data()
            processed_data = data_processor.process_channel_data(raw_data)
            timestamp = datetime.datetime.now().isoformat()
            writer.writerow(processed_data + [timestamp])
            time.sleep(1 / ECG_SAMPLING_PERIOD)
    except KeyboardInterrupt:
        print("\nData capture interrupted")
    finally:
        file_manager.close_file()

if __name__ == "__main__":
    main()

