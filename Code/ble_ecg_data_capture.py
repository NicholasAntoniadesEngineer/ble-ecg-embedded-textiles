#!/usr/bin/env python

"""
A Python module that runs on a Raspberry Pi 4B and connects to a BLE ECG device intended for the garment research project.
Connects to selected device and writes all data to a single .csv file.

Author          = "Nicholas Antoniades"
Start Date      = "03/01/2022"
Last Modified   = "23/05/2022"
Version         = "0.0.1"
"""

import pexpect
import time
import csv
import datetime
import sys
import numpy as np
import os.path

# Constants
NUM_CHANNEL_IMU = 9  # Ax, Ay, Az, Gx, Gy, Gz, Mx, My, Mz
SAMPLES_PER_CHANNEL_IMU = 1
SAMPLES_PER_CHANNEL_ECG = 10
BYTES_PER_SAMPLE_ECG = 3
BYTES_PER_SAMPLE_IMU = 2
ECG_SAMPLING_PERIOD = 500
IMU_SCALE_FACTOR = 2048
SKIP_NUM = 10
ADC_MAX = 0xF30000
V_REF = 2.4
NUM_LOD_CHANNELS = 1

MTU_VALUE = 'mtu 250'
STREAM_REQUEST_NEW = 'char-write-req 0x0016 0100'
STREAM_REQUEST_OLD = 'char-write-req 0x001d 0100'
ACK_HANDLE_NEW = "Notification handle = 0x0015 value:"
ACK_HANDLE_OLD = "Notification handle = 0x001c value:"

# Device addresses
DEVICE_ADDRESSES = {
    "DEVICE_1": "48:23:35:00:36:1B",
    "DEVICE_2": "48:23:35:00:36:3E",
    "DEVICE_3": "CC:86:EC:65:E4:DC",
    "DEVICE_4": "00:3C:84:DD:2B:F6",
    "DEVICE_5": "00:3c:84:dd:2c:01",
    "DEVICE_6": "00:3c:84:DA:EA:D1"
}

class BLEDevice:
    def __init__(self, device_address, device_name):
        self.device_address = device_address
        self.device_name = device_name
        self.attempt_counter = 0
        self.bluetooth_data = None

    def connect(self):
        print("\nRunning gatttool...")
        self.bluetooth_data = pexpect.spawn("gatttool -I")
        print(f"Attempting to connect to: {self.device_address}")

        while True:
            try:
                self.bluetooth_data.sendline(f"connect {self.device_address}")
                self.bluetooth_data.expect("Connection successful", timeout=0.5)
                print("Connected!")
                print(" ' ' ")
                print("'---'")
                print()
                break
            except Exception:
                print()
                print(f"Attempting to connect, attempt: {self.attempt_counter}")
                print()
                print(" ' ' ")
                print(".---.")
                self.attempt_counter += 1
                time.sleep(0.05)

        self.bluetooth_data.sendline(MTU_VALUE)
        if self.device_address in [DEVICE_ADDRESSES["DEVICE_3"], DEVICE_ADDRESSES["DEVICE_4"]]:
            self.bluetooth_data.sendline(STREAM_REQUEST_NEW)
            self.bluetooth_data.expect(ACK_HANDLE_NEW, timeout=1)
        else:
            self.bluetooth_data.sendline(STREAM_REQUEST_OLD)
            self.bluetooth_data.expect(ACK_HANDLE_OLD, timeout=1)

    def get_data(self):
        return self.bluetooth_data

class DataProcessor:
    def __init__(self, num_channels_ecg):
        self.num_channels_ecg = num_channels_ecg
        self.single_sample_ECG = [1] * (self.num_channels_ecg * SAMPLES_PER_CHANNEL_ECG)
        self.raw_ADC_ECG = [1] * (self.num_channels_ecg * SAMPLES_PER_CHANNEL_ECG)
        self.converted_voltage_ECG = np.array([[1] * SAMPLES_PER_CHANNEL_ECG] * self.num_channels_ecg, dtype=float)
        self.raw_LOD_ECG = [1]
        self.single_sample_IMU = [1] * (NUM_CHANNEL_IMU * SAMPLES_PER_CHANNEL_IMU)
        self.raw_IMU = np.array([[1] * SAMPLES_PER_CHANNEL_IMU] * NUM_CHANNEL_IMU, dtype=float)
        self.multi_axis_IMU = np.array([[1] * SAMPLES_PER_CHANNEL_ECG] * NUM_CHANNEL_IMU, dtype=float)

    def ADC_to_voltage_ECG(self, ADC_value):
        convert_value = (ADC_value / ADC_MAX) - 0.5
        convert_value *= V_REF * 2
        voltage_ECG = convert_value / 3.5
        return voltage_ECG

    def bytes_to_data_ECG(self, three_bytes):
        return (int(three_bytes[0], 16) << 16) + (int(three_bytes[1], 16) << 8) + int(three_bytes[2], 16)

    def bytes_to_data_IMU(self, two_bytes):
        converted_data = (int(two_bytes[1], 16) << 8) + int(two_bytes[0], 16)
        if converted_data > (2**15):
            converted_data -= 2**16
        return converted_data

    def process_data(self, bluetooth_data):
        ECG_LOD = bluetooth_data.before[1:4]
        self.raw_LOD_ECG[0] = int(ECG_LOD, 16)

        x = 0
        for i in range(4, 183, 9):
            self.single_sample_ECG[x] = (bluetooth_data.before[i:i+2], bluetooth_data.before[i+3:i+5], bluetooth_data.before[i+6:i+8])
            self.raw_ADC_ECG[x] = self.bytes_to_data_ECG(self.single_sample_ECG[x])
            x += 1

        for h in range(self.num_channels_ecg):
            x = 0
            for j in range(h, len(self.single_sample_ECG), self.num_channels_ecg):
                self.converted_voltage_ECG[h, x] = self.ADC_to_voltage_ECG(self.raw_ADC_ECG[j])
                x += 1

        x = 0
        for i in range(184, 238, 6):
            self.single_sample_IMU[x] = (bluetooth_data.before[i:i+2], bluetooth_data.before[i+3:i+5])
            self.raw_IMU[x] = self.bytes_to_data_IMU(self.single_sample_IMU[x])
            for i in range(3):
                self.multi_axis_IMU[i, x] = self.raw_IMU[x] / IMU_SCALE_FACTOR
            x += 1

class CSVWriter:
    def __init__(self, test_name, device_name):
        self.test_name = test_name
        self.device_name = device_name
        self.ver_counter = 0
        self.write_count = 0
        self.writer = None
        self.file_path = None

    def update_file_path(self, time_stamp):
        current_date = str(time_stamp.date())
        current_time = time_stamp.strftime("%-H-%S")
        version = 'v'
        self.file_path = f"{self.test_name}_{self.device_name}_{current_time}_{current_date}_{version}"

    def initialise_CSV(self, selected_device):
        self.ver_counter += 1
        while True:
            if os.path.isfile(f"{self.file_path}{self.ver_counter}.csv"):
                self.ver_counter += 1
            else:
                f = open(f"{self.file_path}{self.ver_counter}.csv", 'w')
                break

        self.writer = csv.writer(f)
        self.writer.writerow(['# Recorded using POD_Data_Capture.py'])
        time_stamp = datetime.datetime.now()
        self.writer.writerow([f'# Recorded on: {time_stamp}'])
        self.writer.writerow([f'# Device address: {self.device_name}'])
        self.writer.writerow([f'# Device ID: {selected_device}'])
        self.writer.writerow([])

        if selected_device == DEVICE_ADDRESSES["DEVICE_1"]:
            data_header = ['ECG_1', 'ECG_2', 'ECG_3', 'ECG_4', 'ECG_5', 'tstamp']
        else:
            data_header = ['ECG_LOD', 'ECG_1', 'ECG_2', 'A_X', 'A_Y', 'A_Z', 'G_X', 'G_Y', 'G_Z', 'M_X', 'M_Y', 'M_Z', 'tstamp']
        self.writer.writerow(data_header)

    def write_data(self, data_to_write):
        self.writer.writerow(data_to_write)

def main():
    device_old = DEVICE_ADDRESSES["DEVICE_5"]
    device_new = ""
    selected_device = device_new if device_new else device_old
    test_name = 'Test'
    num_channels_ecg = 5 if selected_device == DEVICE_ADDRESSES["DEVICE_1"] else 2
    device_name = 'Brain-Beta-v1-1' if selected_device == device_old else 'Older-Version'

    ble_device = BLEDevice(selected_device, device_name)
    data_processor = DataProcessor(num_channels_ecg)
    csv_writer = CSVWriter(test_name, device_name)

    time_stamp = datetime.datetime.now()
    delta_time = datetime.timedelta(seconds=1 / ECG_SAMPLING_PERIOD)
    csv_writer.update_file_path(time_stamp)

    while True:
        ble_device.connect()
        csv_writer.initialise_CSV(selected_device)

        while True:
            try:
                bluetooth_data = ble_device.get_data()
                if selected_device in [DEVICE_ADDRESSES["DEVICE_3"], DEVICE_ADDRESSES["DEVICE_4"]]:
                    bluetooth_data.expect("Notification handle = 0x0015 value:", timeout=1)
                else:
                    bluetooth_data.expect("Notification handle = 0x001c value:", timeout=1)
            except Exception:
                print("\nConnection lost!\n")
                break

            data_processor.process_data(bluetooth_data)

            time_val = [time_stamp + k * delta_time for k in range(SAMPLES_PER_CHANNEL_ECG)]

            if csv_writer.write_count >= SKIP_NUM:
                for l in range(SAMPLES_PER_CHANNEL_ECG):
                    data_to_write = [data_processor.raw_LOD_ECG[0]] + \
                                    [data_processor.converted_voltage_ECG[m, l] for m in range(num_channels_ecg)] + \
                                    [data_processor.multi_axis_IMU[0, m] for m in range(NUM_CHANNEL_IMU)] + \
                                    [time_val[l].isoformat()]
                    csv_writer.write_data(data_to_write)
                    print(bluetooth_data.before[1:180])
            else:
                csv_writer.write_count += 1

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print('\nInterrupted')
            sys.exit(0)

