import RPi.GPIO as GPIO
import time

class GPIOManager:
    def __init__(self, config):
        """Initialize GPIO with the given configuration."""
        self.config = config
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        # Setup GPIO pins
        for pin, initial_state in config['initial_states'].items():
            GPIO.setup(config['pins'][pin], GPIO.OUT)
            GPIO.output(config['pins'][pin], initial_state)
    
    def reset_device(self):
        """Reset the device by toggling the CS pin."""
        cs_pin = self.config['pins']['cs1']
        GPIO.output(cs_pin, 0)
        time.sleep(0.1)
        GPIO.output(cs_pin, 1)
        time.sleep(0.1)
    
    def cleanup(self):
        """Clean up GPIO resources."""
        GPIO.cleanup() 