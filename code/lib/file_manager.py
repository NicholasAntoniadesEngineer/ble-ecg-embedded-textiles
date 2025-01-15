import csv
import datetime
import os

class FileManager:
    def __init__(self, test_name, device_name, device_id):
        self.test_name = test_name
        self.device_name = device_name
        self.device_id = device_id
        self.counter = 0
        
    def get_next_available_file(self, timestamp):
        """Create and return next available file for writing."""
        filename = f"{self.device_name}_{timestamp.strftime('%Y%m%d_%H%M')}_Device_{self.device_id}_v{self.counter}.csv"
        self.counter += 1
        
        f = open(filename, 'w')
        writer = csv.writer(f)
        writer.writerow(['ecg1', 'ecg2', 'ecg3', 'ecg4', 'ecg5', 'imu_data', 'tstamp'])
        
        return 0, writer, f 