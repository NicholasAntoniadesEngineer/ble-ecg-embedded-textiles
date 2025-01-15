#!/usr/bin/env python3
"""
BMI160 Data Collection Script

This script interfaces with the BMI160 IMU sensor to collect motion data.
It uses SPI for communication and prints the data to the console.

Author: Nicholas Antoniades
"""

import time
from lib.bmi160_driver import BMI160Driver

# SPI Configuration
SPI_CONFIG = {
    'bus': 0,
    'device': 0,
    'max_speed_hz': 32000,
    'mode': 0,
    'gpio_pins': {
        'cs1': 18
    },
    'initial_states': {
        'cs1': 1
    }
}

def main():
    # Initialize BMI160
    bmi160 = BMI160Driver(SPI_CONFIG)
    
    if not bmi160.test_connection():
        print("BMI160 connection failed!")
        return
        
    print("BMI160 connected successfully!")
    
    try:
        while True:
            motion_data = bmi160.get_motion_6()
            if motion_data:
                print(f"Accel: {motion_data[3:]}")
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\nProgram terminated by user")
        
if __name__ == "__main__":
    main()
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        