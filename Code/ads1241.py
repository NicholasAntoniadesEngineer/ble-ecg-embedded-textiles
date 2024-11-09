"""
ADS1241 Device Interface

This module provides an interface to the ADS1241 device for ADC data collection.
"""

# Constants for ADS1241
ADS1241_P_AIN0 = 0b00000111
ADS1241_P_AIN1 = 0b00010111
ADS1241_BLANK = 0b00000000
ADS1241_READ_ADDRESS = 0b00000001
ADS1241_SETUP_REG = 0b01010000
ADS1241_MUX_CTRL_REG = 0b01010001

ADC_DATA_BYTES = 3

class ADS1241:
    """Class to interface with the ADS1241 device."""

    def __init__(self, spi, gpio, cs_pin):
        self.spi = spi
        self.gpio = gpio
        self.cs_pin = cs_pin

    def program_adc(self):
        """Program the ADC with initial settings."""
        self.gpio.set_output(self.cs_pin, 0)
        self.spi.transfer([ADS1241_SETUP_REG, ADS1241_BLANK, ADS1241_BLANK])
        time.sleep(0.1)
        self.gpio.set_output(self.cs_pin, 1)

    def input_select(self, input_sel):
        """Select the input channel for the ADC."""
        self.gpio.set_output(self.cs_pin, 0)
        self.spi.transfer([ADS1241_MUX_CTRL_REG, ADS1241_BLANK, input_sel, ADS1241_BLANK])
        self.gpio.set_output(self.cs_pin, 1)

    def fetch_adc_data(self):
        """Fetch data from the ADC."""
        self.gpio.set_output(self.cs_pin, 0)
        self.spi.transfer([ADS1241_READ_ADDRESS])
        adc_data = self.spi.transfer([ADS1241_BLANK] * ADC_DATA_BYTES)
        self.gpio.set_output(self.cs_pin, 1)
        return adc_data 