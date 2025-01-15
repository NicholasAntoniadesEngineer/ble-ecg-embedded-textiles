from .constants import (
    DEVICE_ADDRESSES,
    DEVICE_1,
    DEVICE_OLD
)

def get_device_config():
    """Configure device settings based on the selected device."""
    device_new = ""
    selected_device = device_new if device_new else DEVICE_OLD
    
    num_channels = 5 if selected_device == DEVICE_1 else 2
    device_name = 'Brain-Beta-v1-1' if selected_device == DEVICE_OLD else 'Older-Version'
    
    config = {
        'num_channels': num_channels,
        'device_name': device_name,
        'test_name': 'Test',
        'file_prefix': 'ble_ecg'
    }
    
    return selected_device, config 