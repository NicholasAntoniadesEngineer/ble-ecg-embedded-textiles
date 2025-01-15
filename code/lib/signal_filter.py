from scipy.signal import butter, lfilter
import numpy as np

class ECGFilter:
    def __init__(self, fs=200.0, lowcut=0.5, highcut=40):
        self.fs = fs
        self.lowcut = lowcut
        self.highcut = highcut
        
    def butter_bandpass(self, order=5):
        nyq = 0.5 * self.fs
        low = self.lowcut / nyq
        high = self.highcut / nyq
        b, a = butter(order, [low, high], btype='band')
        return b, a

    def apply_filter(self, data, order=5):
        b, a = self.butter_bandpass(order=order)
        y = lfilter(b, a, data)
        return y 