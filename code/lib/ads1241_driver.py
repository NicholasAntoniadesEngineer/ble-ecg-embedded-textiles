import spidev
import RPi.GPIO as GPIO
import time

# Constants for ADS1241
ADS1241_P_AIN0 = 0b00000111
ADS1241_P_AIN1 = 0b00010111
ADS1241_BLANK = 0b00000000
ADS1241_READ_ADDRESS = 0b00000001
ADS1241_SETUP_REG = 0b01010000
ADS1241_MUX_CTRL_REG = 0b01010001

ADC_DATA_BYTES = 3

class ADS1241Driver:
    def __init__(self, cs_pin=23):
        # Initialize GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        self.cs_pin = cs_pin
        GPIO.setup(self.cs_pin, GPIO.OUT)
        GPIO.output(self.cs_pin, 1)
        
        # Initialize SPI
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 32000
        print('SPI initialised\n')

    def reg_write(self, reg_address, data):
        """Write data to a register."""
        GPIO.output(self.cs_pin, 0)
        self.spi.xfer([reg_address, data])
        GPIO.output(self.cs_pin, 1)

    def reg_read(self, reg_address):
        """Read data from a register."""
        GPIO.output(self.cs_pin, 0)
        read_command = reg_address | 0x80
        self.spi.xfer([read_command])
        data = self.spi.xfer([0x0])
        GPIO.output(self.cs_pin, 1)
        return data

    def program_adc(self):
        """Program the ADC with initial settings."""
        GPIO.output(self.cs_pin, 0)
        self.spi.xfer([ADS1241_SETUP_REG, ADS1241_BLANK, ADS1241_BLANK])
        time.sleep(0.1)
        GPIO.output(self.cs_pin, 1)
        print('ADS1241 programmed\n')

    def input_select(self, input_sel):
        """Select the input channel for the ADC."""
        GPIO.output(self.cs_pin, 0)
        self.spi.xfer([ADS1241_MUX_CTRL_REG, ADS1241_BLANK, input_sel, ADS1241_BLANK])
        GPIO.output(self.cs_pin, 1)

    def fetch_adc_data(self):
        """Fetch data from the ADC."""
        GPIO.output(self.cs_pin, 0)
        self.spi.xfer([ADS1241_READ_ADDRESS])
        adc_data = self.spi.xfer([ADS1241_BLANK] * ADC_DATA_BYTES)
        GPIO.output(self.cs_pin, 1)
        return adc_data

    def process_adc_data(self, adc_data):
        """Process raw ADC data into a single value."""
        return ((adc_data[0] & 0xFF) << 16) | \
               ((adc_data[1] & 0xFF) << 8) | \
               (adc_data[2] & 0xFF)

    def cleanup(self):
        """Clean up GPIO and SPI resources."""
        self.spi.close()
        GPIO.cleanup() 