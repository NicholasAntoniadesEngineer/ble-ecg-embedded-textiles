import spidev
from time import sleep
import os
import RPi.GPIO as GPIO
import time

# Initialise CS 1 pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
CS1_pin = 24             # Set GPIO24 to be CS pin
GPIO.output(CS1_pin,1)   # Set CS bit high for no transmission 

# Initialise CS 2 pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
CS2_pin = 23             # Set GPIO24 to be CS pin
GPIO.output(CS2_pin,1)   # Set CS bit high for no transmission 



# Initialise SPI
CSL = 0                     # Device is the chip select pin. Set to 0 or 1.
spi_channel = 1             # Set SPI channel, either 0 or 1.
spi = spidev.SpiDev()       # Enable SPI
spi.open(spi_channel, CSL)  # Open a connection to the device
spi.max_speed_hz = 32000    # Set SPI speed	
spi.mode= 0b00               # Mode 0b0 has clock inactive low    

# Check SPI connection CS 1
data=0 

GPIO.output(CS1_pin,0)   # Set cs bit low for transmission 
spi.xfer([0x0,0x0])                     # Stop data conversion
GPIO.output(CS1_pin,1)   # Set CS bit high for no transmission 



GPIO.output(CS1_pin,0)   # Set cs bit low for transmission 
REVID_Read_command = 0x40|0x80          # Addres | 0x80 to indicate a read
spi.xfer([REVID_Read_command])   # Read value of ADS1293 REVID
data = spi.xfer([0x0])  					# Keep the clock line going for MISO signal
GPIO.output(CS1_pin,0005)   # Set CS bit high for no transmission 

print(data)

# Check SPI connection CS 2
data=0 

GPIO.output(CS2_pin,0)   # Set cs bit low for transmission 
spi.xfer([0x0,0x0])                     # Stop data conversion
GPIO.output(CS2_pin,1)   # Set CS bit high for no transmission 



GPIO.output(CS2_pin,0)   # Set cs bit low for transmission 
REVID_Read_command = 0x40|0x80          # Addres | 0x80 to indicate a read
spi.xfer([REVID_Read_command])   # Read value of ADS1293 REVID
data = spi.xfer([0x0])  					# Keep the clock line going for MISO signal
GPIO.output(CS2_pin,0005)   # Set CS bit high for no transmission 

print(data)

