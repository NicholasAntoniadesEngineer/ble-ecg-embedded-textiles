"""
BMI160 Driver Module

This module provides an interface for the BMI160 IMU sensor using SPI communication.
It handles device configuration and data collection for accelerometer and gyroscope.

Author: Nicholas Antoniades
"""

import time
from .spi_driver import SPIDriver
from .constants import BMI160_CONSTANTS as BMI

class BMI160Driver:
    def __init__(self, spi_config):
        """Initialize BMI160 with SPI configuration."""
        self.spi = SPIDriver(spi_config)
        self.cs_pin_name = spi_config['gpio_pins']['cs1']
        self.initialize()
        
    def initialize(self):
        """Initialize the BMI160 sensor."""
        # Soft reset
        self.reg_write(BMI.BMI160_RA_CMD, BMI.BMI160_CMD_SOFT_RESET)
        time.sleep(0.1)
        
        # Force into SPI mode
        self.reg_read(0x7F)
        
        # Power up accelerometer
        self.reg_write(BMI.BMI160_RA_CMD, BMI.BMI160_CMD_ACC_MODE_NORMAL)
        while (0x1 != self.reg_read_bits(
            BMI.BMI160_RA_PMU_STATUS,
            BMI.BMI160_ACC_PMU_STATUS_BIT,
            BMI.BMI160_ACC_PMU_STATUS_LEN)):
            pass
            
        # Power up gyroscope
        self.reg_write(BMI.BMI160_RA_CMD, BMI.BMI160_CMD_GYR_MODE_NORMAL)
        while (0x1 != self.reg_read_bits(
            BMI.BMI160_RA_PMU_STATUS,
            BMI.BMI160_GYR_PMU_STATUS_BIT,
            BMI.BMI160_GYR_PMU_STATUS_LEN)):
            pass
            
        # Configure sensor settings
        self._configure_sensor()
        
    def _configure_sensor(self):
        """Configure sensor settings."""
        # Set gyroscope range
        self.reg_write_bits(
            BMI.BMI160_RA_GYRO_RANGE,
            BMI.BMI160_GYRO_RANGE_1000,
            BMI.BMI160_GYRO_RANGE_SEL_BIT,
            BMI.BMI160_GYRO_RANGE_SEL_LEN
        )
        
        # Set accelerometer range
        self.reg_write_bits(
            BMI.BMI160_RA_ACCEL_RANGE,
            BMI.BMI160_ACCEL_RANGE_16G,
            BMI.BMI160_ACCEL_RANGE_SEL_BIT,
            BMI.BMI160_ACCEL_RANGE_SEL_LEN
        )
        
        # Set output data rates
        self.reg_write_bits(
            BMI.BMI160_RA_ACCEL_CONF,
            BMI.BMI160_ACCEL_RATE_100HZ,
            BMI.BMI160_ACCEL_RATE_SEL_BIT,
            BMI.BMI160_ACCEL_RATE_SEL_LEN
        )
        
        self.reg_write_bits(
            BMI.BMI160_RA_GYRO_CONF,
            BMI.BMI160_GYRO_RATE_100HZ,
            BMI.BMI160_GYRO_RATE_SEL_BIT,
            BMI.BMI160_GYRO_RATE_SEL_LEN
        )
        
    def test_connection(self):
        """Test connection to BMI160."""
        self.reg_read(BMI.Initial_read)
        time.sleep(0.001)
        chip_id = self.reg_read(BMI.BMI160_RA_CHIP_ID)
        return chip_id[0] == 0xD1
        
    def get_motion_6(self):
        """Get 6-axis motion data (gyro XYZ, accel XYZ)."""
        buffer = self.reg_read_12(BMI.BMI160_RA_GYRO_X_L)
        if not buffer:
            return None
            
        data = [0] * 6
        data[0] = ((int(buffer[1]) << 8) | buffer[0])  # gX
        data[1] = ((int(buffer[3]) << 8) | buffer[2])  # gY
        data[2] = ((int(buffer[5]) << 8) | buffer[4])  # gZ
        data[3] = ((int(buffer[7]) << 8) | buffer[6])  # aX
        data[4] = ((int(buffer[9]) << 8) | buffer[8])  # aY
        data[5] = ((int(buffer[11]) << 8) | buffer[10])  # aZ
        
        return data
        
    def get_acceleration(self):
        """Get 3-axis acceleration data."""
        buffer = self.reg_read_6(BMI.BMI160_RA_ACCEL_X_L)
        if not buffer:
            return None
            
        data = [0] * 3
        data[0] = ((int(buffer[1]) << 8) | buffer[0])  # aX
        data[1] = ((int(buffer[3]) << 8) | buffer[2])  # aY
        data[2] = ((int(buffer[5]) << 8) | buffer[4])  # aZ
        
        return data 