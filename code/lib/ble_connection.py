import pexpect
import time
import RPi.GPIO as GPIO

class BLEConnection:
    def __init__(self, device_address, cs_pin=18):
        self.device_address = device_address
        self.cs_pin = cs_pin
        self.child = None
        self._setup_gpio()
        
    def _setup_gpio(self):
        """Initialize GPIO settings."""
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.cs_pin, GPIO.OUT)
        
    def reset_connection(self):
        """Reset the BLE connection via GPIO toggle."""
        GPIO.output(self.cs_pin, 0)
        time.sleep(0.1)
        GPIO.output(self.cs_pin, 1)
        time.sleep(0.1)
        
    def connect(self):
        """Attempts connection to the selected Bluetooth device."""
        print("\nRunning gatttool...")
        self.child = pexpect.spawn("gatttool -I")
        print(f"Attempting to connect to: {self.device_address}")
        try:
            self.child.sendline(f"connect {self.device_address}")
            self.child.expect("Connection successful", timeout=0.5)
            print("Connected!\n")
        except Exception:
            print("Cannot connect to Bluetooth device")
            self.child = None
        return self.child is not None
        
    def get_data(self):
        """Get next data packet from device."""
        self.child.expect("Notification handle = 0x001c value:", timeout=10)
        return self.child.before 