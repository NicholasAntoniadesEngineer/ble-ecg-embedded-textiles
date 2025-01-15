import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pexpect
import RPi.GPIO as GPIO
from datetime import datetime as dt

# Constants
DEVICE = "48:23:35:00:36:1B"
CS1_PIN = 18

# Initialize GPIO
def initialize_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(CS1_PIN, GPIO.OUT)
    GPIO.output(CS1_PIN, 0)
    time.sleep(0.1)
    GPIO.output(CS1_PIN, 1)
    time.sleep(0.1)

# Connect to Bluetooth device
def connect_to_device(device):
    print(f"Connecting to {device}...")
    child = pexpect.spawn("gatttool -I")
    try:
        child.sendline(f"connect {device}")
        child.expect("Connection successful", timeout=5)
        print("Connected!")
        return child
    except pexpect.exceptions.TIMEOUT:
        print("Cannot connect to Bluetooth device")
        return None

# Decode data from Bluetooth
def decode_data(child):
    child.expect("Notification handle = 0x001c value:", timeout=10)
    data = child.before.decode('utf-8').strip().split()
    decoded_values = [int(data[i], 16) << 16 | int(data[i+1], 16) << 8 | int(data[i+2], 16) for i in range(0, len(data), 3)]
    return decoded_values

# Animation function
def animate(i, xs, ys, child):
    decoded_values = decode_data(child)
    print(decoded_values)
    xs.append(dt.now().strftime('%H:%M:%S.%f'))
    ys.append(decoded_values[0])  # Assuming CH1_S1_Decoded is the first value
    xs, ys = xs[-10:], ys[-10:]
    ax.clear()
    ax.plot(xs, ys)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('MPU6050 X Acceleration over Time')
    plt.ylabel('X-Acceleration')

# Main function
def main():
    initialize_gpio()
    child = connect_to_device(DEVICE)
    if not child:
        return

    fig = plt.figure()
    global ax
    ax = fig.add_subplot(1, 1, 1)
    xs, ys = [], []

    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, child), interval=1000)
    plt.show()

if __name__ == "__main__":
    main()