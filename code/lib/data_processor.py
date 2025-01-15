"""
ECG Data Processing Module

This module handles the processing of raw ECG data from the BLE device.
"""

import numpy as np
from .constants import (
    SAMPLES_PER_CHANNEL_ECG,
    ECG_SAMPLING_PERIOD
)

class DataProcessor:
    def __init__(self, num_channels):
        """Initialize data processor with number of channels."""
        self.num_channels = num_channels
        self.ch_val = np.zeros((num_channels, SAMPLES_PER_CHANNEL_ECG), dtype=float)
        
    def raw_to_ecg(self, value):
        """Convert raw ECG ADC value to Voltage."""
        ADC_MAX = 0xF30000
        V_REF = 2.4
        raw_value = value/ADC_MAX
        raw_value = raw_value - 0.5 + 0.16
        raw_value = raw_value*V_REF*2
        return raw_value/3.5
        
    def bytes_to_data(self, bytes_data):
        """Convert 3 bytes into a 24bit value."""
        return (int(bytes_data[0], 16) << 16) + \
               (int(bytes_data[1], 16) << 8) + \
               int(bytes_data[2], 16)
               
    def process_channel_data(self, raw_data):
        """Process raw channel data into voltage values."""
        num_values = self.num_channels * SAMPLES_PER_CHANNEL_ECG
        ch_bytes = [None] * num_values
        ch_converted_val = [None] * num_values
        
        # Convert bytes to values
        x = 0
        total_bytes = 3 * num_values * 3  # 3 bytes per value, times 3 for formatting
        for i in range(1, total_bytes, 9):
            ch_bytes[x] = (
                raw_data[i:i+2],
                raw_data[i+3:i+5],
                raw_data[i+6:i+8]
            )
            ch_converted_val[x] = self.bytes_to_data(ch_bytes[x])
            x += 1
            
        # Convert to voltage values
        for h in range(self.num_channels):
            x = 0
            for j in range(h, num_values, self.num_channels):
                self.ch_val[h,x] = self.raw_to_ecg(ch_converted_val[j])
                x += 1
                
        return self.ch_val 