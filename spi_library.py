import spidev
import RPi.GPIO as GPIO
import time

class SPILibrary:
    def __init__(self, spi_channel=1, max_speed_hz=32000, mode=0b00):
        self.spi = spidev.SpiDev()
        self.spi.open(spi_channel, 0)
        self.spi.max_speed_hz = max_speed_hz
        self.spi.mode = mode
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    def setup_cs_pin(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 1)  # Set CS high for no transmission

    def spi_transfer(self, cs_pin, data):
        GPIO.output(cs_pin, 0)  # Set CS low for transmission
        response = self.spi.xfer(data)
        GPIO.output(cs_pin, 1)  # Set CS high for no transmission
        return response

    def read_register(self, cs_pin, reg_address):
        read_command = reg_address | 0x80
        return self.spi_transfer(cs_pin, [read_command, 0x0])

    def write_register(self, cs_pin, reg_address, data):
        self.spi_transfer(cs_pin, [reg_address, data])

    def cleanup(self):
        GPIO.cleanup()

# Example usage
if __name__ == "__main__":
    spi_lib = SPILibrary()
    cs_pin = 24
    spi_lib.setup_cs_pin(cs_pin)

    # Example read and write
    spi_lib.write_register(cs_pin, 0x01, 0x11)
    data = spi_lib.read_register(cs_pin, 0x40)
    print("Read data:", data)

    spi_lib.cleanup()
