import spidev
from time import sleep
import os
import RPi.GPIO as GPIO
import time


# Initialise SPI
CSL = 0                     # Device is the chip select pin. Set to 0 or 1.
spi_channel = 1             # Set SPI channel, either 0 or 1.
spi = spidev.SpiDev()       # Enable SPI
spi.open(spi_channel, CSL)  # Open a connection to the device
spi.max_speed_hz = 32000    # Set SPI speed	
spi.mode= 0b00               # Mode 0b0 has clock inactive low    

# Check SPI connection
data=0 
spi.xfer([0x0,0x0])                     # Stop data conversion
REVID_Read_command = 0x40|0x80          # Addres | 0x80 to indicate a read
data = spi.xfer([REVID_Read_command])   # Read value of ADS1293 REVID
spi.xfer([0x0,0x0])  					# Keep the clock line going for MISO signal
print(data)

