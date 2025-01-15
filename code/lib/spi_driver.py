"""
SPI Driver Module

This module provides a unified interface for SPI communication on the Raspberry Pi.
It handles device configuration and data transfer operations.

Author: Nicholas Antoniades
"""

import spidev
import RPi.GPIO as GPIO
import time

class SPIDriver:
    def __init__(self, config):
        """Initialize SPI interface with given configuration."""
        self.config = config
        self.spi = None
        self.setup_spi()
        self.setup_gpio()
        
    def setup_spi(self):
        """Configure SPI interface."""
        self.spi = spidev.SpiDev()
        self.spi.open(
            self.config['bus'],
            self.config['device']
        )
        self.spi.max_speed_hz = self.config['max_speed_hz']
        self.spi.mode = self.config.get('mode', 0)
        self.spi.bits_per_word = self.config.get('bits_per_word', 8)
        
    def setup_gpio(self):
        """Configure GPIO pins for chip select."""
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        for pin_name, pin in self.config['gpio_pins'].items():
            GPIO.setup(pin, GPIO.OUT)
            initial_state = self.config['initial_states'].get(pin_name, 1)
            GPIO.output(pin, initial_state)
            
    def transfer(self, data, cs_pin_name):
        """
        Perform SPI transfer with specified chip select.
        
        Args:
            data: Data to transfer
            cs_pin_name: Name of chip select pin to use
        """
        cs_pin = self.config['gpio_pins'][cs_pin_name]
        GPIO.output(cs_pin, 0)
        time.sleep(0.0001)  # Setup time
        
        if isinstance(data, (list, tuple)):
            result = self.spi.xfer2(data)
        else:
            result = self.spi.xfer2([data])[0]
            
        GPIO.output(cs_pin, 1)
        time.sleep(0.0001)  # Hold time
        
        return result
        
    def write_register(self, cs_pin_name, reg_addr, value):
        """Write to a device register."""
        return self.transfer([reg_addr, value], cs_pin_name)
        
    def read_register(self, cs_pin_name, reg_addr):
        """Read from a device register."""
        return self.transfer([reg_addr | 0x80, 0x00], cs_pin_name)[1]
        
    def cleanup(self):
        """Clean up resources."""
        if self.spi:
            self.spi.close()
        GPIO.cleanup() 