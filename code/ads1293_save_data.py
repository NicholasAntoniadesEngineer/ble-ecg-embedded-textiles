#!/usr/bin/env python3
from lib.ads1293_driver import ADS1293
from lib.data_processor import DataProcessor
import spidev
import RPi.GPIO as GPIO
import time
import datetime
import csv
import sys

class SPIInterface:
    def __init__(self, bus, device, max_speed_hz):
        self.spi = spidev.SpiDev()
        self.spi.open(bus, device)
        self.spi.max_speed_hz = max_speed_hz

    def transfer(self, data):
        return self.spi.xfer2(data)

    def close(self):
        self.spi.close()

class GPIOInterface:
    def __init__(self, mode):
        GPIO.setmode(GPIO.BCM if mode == 'BCM' else GPIO.BOARD)
        GPIO.setwarnings(False)

    def setup(self, pin, direction, initial=GPIO.LOW):
        GPIO.setup(pin, GPIO.OUT if direction == 'OUT' else GPIO.IN, initial=initial)

    def output(self, pin, state):
        GPIO.output(pin, GPIO.HIGH if state else GPIO.LOW)

    def cleanup(self):
        GPIO.cleanup()

def initialize_hardware():
    """Initialize and configure hardware interfaces."""
    spi = SPIInterface(bus=0, device=0, max_speed_hz=32000)
    gpio = GPIOInterface(mode='BCM')
    
    device_config = {
        'cs_pin': 'cs1',
        'gpio_pins': {
            'cs1': 24
        }
    }
    
    ads = ADS1293(spi, gpio, device_config)
    processor = DataProcessor(num_channels_ecg=2)  # 2 channels for ECG
    
    return ads, processor

def check_device_connection(ads):
    """Check if device is connected and initialize it."""
    print('Checking device on CS1')
    if not ads.test_connection():
        print('Cannot detect device!')
        time.sleep(0.1)
        return False
        
    print('Initialize Device 1 to 3 lead mode')
    ads.init_1lead()
    return True

def collect_data(ads, processor):
    """Collect and process ECG data."""
    with open('test.csv', 'w') as f:
        writer = csv.writer(f)
        
        while True:
            data = ads.read_ecg_data_ch1_ch2()
            ch1_raw, ch2_raw = processor.process_raw_data(data)
            ch1_ecg = processor.convert_to_ecg_value(ch1_raw)
            
            timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S:%f')
            print(ch1_raw)
            
            writer.writerow([timestamp, ch1_raw])
            time.sleep(0.005)

def main():
    # Initialize hardware
    ads, processor = initialize_hardware()
    
    # Check device connection
    if not check_device_connection(ads):
        return
        
    # Start data collection
    collect_data(ads, processor)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nInterrupted')
        sys.exit(0)
    



            
    