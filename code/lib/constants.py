"""Constants for BLE ECG data capture."""

# Device Configuration
DEVICE_ADDRESSES = {
    "DEVICE_1": "48:23:35:00:36:1B",  # 6-lead ECG device, old hardware
    "DEVICE_2": "48:23:35:00:36:3E",  # 6-lead ECG device, old hardware
    "DEVICE_3": "CC:86:EC:65:E4:DC",  # 3-lead ECG device, latest hardware
    "DEVICE_4": "00:3C:84:DD:2B:F6",
    "DEVICE_5": "00:3c:84:dd:2c:01",
    "DEVICE_6": "00:3c:84:DA:EA:D1"
}

# Sampling Configuration
NUM_CHANNEL_IMU = 9  # Ax, Ay, Az, Gx, Gy, Gz, Mx, My, Mz
SAMPLES_PER_CHANNEL_IMU = 1
SAMPLES_PER_CHANNEL_ECG = 10
BYTES_PER_SAMPLE_ECG = 3
BYTES_PER_SAMPLE_IMU = 2
ECG_SAMPLING_PERIOD = 500
IMU_SCALE_FACTOR = 2048
SKIP_NUM = 10

# ADC Configuration
ADC_MAX = 0xF30000
V_REF = 2.4
NUM_LOD_CHANNELS = 1

# BLE Configuration
MTU_VALUE = 'mtu 250'
STREAM_REQUEST_NEW = 'char-write-req 0x0016 0100'
STREAM_REQUEST_OLD = 'char-write-req 0x001d 0100'
ACK_HANDLE_NEW = "Notification handle = 0x0015 value:"
ACK_HANDLE_OLD = "Notification handle = 0x001c value:" 

DEVICE_1 = DEVICE_ADDRESSES["DEVICE_1"]
DEVICE_OLD = DEVICE_ADDRESSES["DEVICE_5"] 