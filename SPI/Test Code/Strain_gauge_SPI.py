#!/usr/bin/env python3
import sys
import spidev
import os
import RPi.GPIO as GPIO
import time

import json

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
@brief Initialises Rpi SPI interface
@note  CS pin for spidev library has issues and oscillates at the end of transmission
       as a solution a GPIO is set as a manual cs pin for each device
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Initialise to GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Set GPIO23 to be CS1 pin
CS1 = 24       
GPIO.setup(23, GPIO.OUT)
# Set GPIO24 to be CS2 pin
CS2 = 23       
GPIO.setup(24, GPIO.OUT)
# Set CS bits high for no transmission  
GPIO.output(CS1,1)   
GPIO.output(CS2,1)    
CSPIN = CS2

# Enable SPI
spi = spidev.SpiDev()       
# Open a connection to the devices
spi.open(0, 0)         
# Set SPI speed
spi.max_speed_hz = 32000    

#time.sleep(0.02)
#Programme the config register
# Set CS bit low for transmission
GPIO.output(CSPIN,0) 

# SPI write new 16 byte register value in 2 bytes
Byte1 = 0b00010100
Byte2 = 0b11101010

returnVAL = spi.xfer([Byte1,Byte2])   
#returnVAL= ((returnVAL[0] & 0xFF) << 8) | (returnVAL[1] & 0xFF)
print('Value: ' , returnVAL)
# Set CS bit high for end of transmission


time.sleep(1)
 
# Set CS bit high for end of transmission
GPIO.output(CSPIN,1) 



while True:


       # Set CS bit low for transmission
       GPIO.output(CSPIN,0) 
       #  spi.xfer([0b00011110,0b11101010])  
       #  data = spi.xfer([0x0,0x0,0x0])
       data1 = spi.xfer([Byte1,Byte2])
       #data1 = spi.xfer([0x0,0x0, Byte1,Byte2])
       # Set CS bit high for end of transmission
       GPIO.output(CSPIN,1) 
       CH1data_raw = ((data1[0] & 0xFF) << 8) | (data1[1] & 0xFF)
       
       print(CH1data_raw)
       time.sleep(0.08)



