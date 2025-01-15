import spidev
import RPi.GPIO as GPIO

class ADS1293Driver:
    def __init__(self, cs_pin=24):
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

    def reg_read(self, reg_address):
        GPIO.output(self.cs_pin, 0)
        read_command = reg_address | 0x80
        self.spi.xfer([read_command])
        data = self.spi.xfer([0x0])
        GPIO.output(self.cs_pin, 1)
        return data

    def reg_write(self, reg_address, data):
        GPIO.output(self.cs_pin, 0)
        self.spi.xfer([reg_address, data])
        GPIO.output(self.cs_pin, 1)

    def test_connection(self):
        self.reg_write(0x0, 0x0)
        data = self.reg_read(0x40)
        return str(data[0]) == '1'

    def init_3lead(self):
        # All your initialization code here
        self.reg_write(0x0, 0x0)  # stop data conversion
        self.reg_write(0x01, 0x11)  # connect channel 1
        self.reg_write(0x0A, 0x03)  # enable common-mode detector
        # ... rest of your initialization code ...
        self.reg_write(0x00, 0x01)  # start data conversion
        print('ADS1293 3 lead mode programmed \n')

    def read_ecg_data_ch1_ch2(self):
        GPIO.output(self.cs_pin, 0)
        read_command = 0x50 | 0x80
        self.spi.xfer([read_command])
        data = self.spi.xfer([0x0, 0x0, 0x0, 0x0, 0x0, 0x0])
        GPIO.output(self.cs_pin, 1)
        return data 