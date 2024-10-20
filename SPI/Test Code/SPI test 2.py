
import spidev
import time

# Initialise SPI
CSL = 0                     # Device is the chip select pin. Set to 0 or 1.
spi_channel = 1             # Set SPI channel, either 0 or 1.
spi = spidev.SpiDev()       # Enable SPI
spi.open(spi_channel, CSL)  # Open a connection to the device
spi.max_speed_hz = 32000	

while True:
		spi.xfer([10,20])
		time.sleep(0.1)
		spi.xfer([30,40])
		time.sleep(0.1)
