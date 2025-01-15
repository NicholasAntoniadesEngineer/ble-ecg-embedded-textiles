#!/usr/bin/env python3
from lib.ads1241 import ADS1241
from lib.hardware_interfaces import SPIInterface, GPIOInterface
import time
import datetime
import csv
import sys

def initialize_hardware():
    """Initialize and configure hardware interfaces."""
    spi = SPIInterface(bus=0, device=0, max_speed_hz=32000)
    gpio = GPIOInterface(mode='BCM')
    
    device_config = {
        'cs_pin': 'cs2',
        'gpio_pins': {
            'cs2': 23
        }
    }
    
    ads = ADS1241(spi, gpio, device_config)
    print('Initializing ADS1241')
    ads.program_adc()
    
    return ads

def collect_data(ads):
    """Collect and process ADC data."""
    with open('Strain_gauge_data.csv', 'a') as f:
        writer = csv.writer(f)
        
        while True:
            try:
                # Request Data for P_AIN0
                ads.input_select(ADS1241.P_AIN0)
                adc_data = ads.fetch_adc_data()
                p_ain0_raw = ((adc_data[0] & 0xFF) << 16) | \
                            ((adc_data[1] & 0xFF) << 8) | \
                            (adc_data[2] & 0xFF)
                
                timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S:%f')
                print(p_ain0_raw, 0)
                
                writer.writerow([timestamp, p_ain0_raw])
                time.sleep(0.05)
                
            except KeyboardInterrupt:
                print('\nData collection interrupted')
                break
            except Exception as e:
                print(f'\nError during data collection: {str(e)}')
                break

def main():
    """Main function to run the ADC data capture."""
    try:
        # Initialize hardware
        ads = initialize_hardware()
        
        print('Reading data packets')
        collect_data(ads)
        
    except Exception as e:
        print(f"Error in main: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nInterrupted')
        sys.exit(0)

