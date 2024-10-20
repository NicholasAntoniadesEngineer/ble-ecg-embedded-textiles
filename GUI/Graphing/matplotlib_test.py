
import time
import os
from time import sleep
from datetime import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pexpect
import time
import RPi.GPIO as GPIO

#create csv file to save the data
# file = open("/home/pi/Accelerometer_data.csv", "a")
# i=0
# if os.stat("/home/pi/Accelerometer_data.csv").st_size == 0:
#         file.write("Time,X,Y,Z\n")

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

# Initialise to GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Set GPIO24 to be CS1 pin
CS1 = 18     
GPIO.setup(CS1, GPIO.OUT)
# Toggle power to device reseting the bluetooth connection
GPIO.output(CS1,0) 
time.sleep(0.1)
GPIO.output(CS1,1) 
time.sleep(0.1)
 
DEVICE = "48:23:35:00:36:1B"
print("Hexiwear address:"),
print(DEVICE + '\n')
 
# Run gatttool interactively.
print("Running gatttool...")
child = pexpect.spawn("gatttool -I")
 
# Connect to the device.
print("Connecting to ")
print(DEVICE + '\n')
child.sendline("connect {0}".format(DEVICE))
child.expect("Connection successful", timeout=5)
print("Connected!" + '\n')

# Stream data
child.sendline('char-write-req 0x001d 0100')
child.expect("Notification handle = 0x001c value:", timeout=10)

print('Outside_1')
def animate(i, xs, ys):
    print('Inside_0')
    child.expect("Notification handle = 0x001c value:", timeout=10)
    print('Inside_1')
    #  CH1_S1 = child.before[1:9]
    CH1_S1_bytes = [(child.before[1:3]),
                    (child.before[4:6]),
                    (child.before[7:9])]
    CH1_S1_Decoded = (int(CH1_S1_bytes[0], 16) <<16) + (int(CH1_S1_bytes[1], 16) <<8) + (int(CH1_S1_bytes[2], 16))
    
    #  CH2_S1 = child.before[10:18]
    CH2_S1_bytes = [(child.before[10:12]),
                    (child.before[13:15]),
                    (child.before[16:18])]
    CH2_S1_Decoded = (int(CH2_S1_bytes[0], 16) <<16) + (int(CH2_S1_bytes[1], 16) <<8) + (int(CH2_S1_bytes[2], 16))
   
    #  CH3_S1 = child.before[19:27]
    CH3_S1_bytes = [(child.before[19:21]),
                    (child.before[22:24]),
                    (child.before[25:27])]
    CH3_S1_Decoded = (int(CH3_S1_bytes[0], 16) <<16) + (int(CH3_S1_bytes[1], 16) <<8) + (int(CH3_S1_bytes[2], 16))
    
    #CH1_S2 = child.before[28:36]
    CH1_S2_bytes = [(child.before[28:30]),
                    (child.before[31:33]),
                    (child.before[34:36])]
    CH1_S2_Decoded = (int(CH1_S2_bytes[0], 16) <<16) + (int(CH1_S2_bytes[1], 16) <<8) + (int(CH1_S2_bytes[2], 16))
    
    #CH2_S2 = child.before[37:45]
    CH2_S2_bytes = [(child.before[37:39]),
                    (child.before[40:42]),
                    (child.before[43:45])]
    CH2_S2_Decoded = (int(CH2_S2_bytes[0], 16) <<16) + (int(CH2_S2_bytes[1], 16) <<8) + (int(CH2_S2_bytes[2], 16))
    
    #CH3_S2 = child.before[46:54]
    CH3_S2_bytes = [(child.before[46:48]),
                    (child.before[49:51]),
                    (child.before[52:54])]
    CH3_S2_Decoded = (int(CH3_S2_bytes[0], 16) <<16) + (int(CH3_S2_bytes[1], 16) <<8) + (int(CH3_S2_bytes[2], 16))
    
    ramaining_bytes = child.before[55:60]
    ramaining_data = child.before[60:]
    
    
    # Print all data read in
    # print(child.before[1:])
        
    # Print decode values
    print(CH1_S1_Decoded, CH2_S1_Decoded, CH3_S1_Decoded)
    time.sleep(0.01)
    print(CH1_S2_Decoded, CH2_S2_Decoded, CH3_S2_Decoded)
    
    # Print byte values
    # print('S1',CH1_S1_bytes, CH2_S1_bytes, CH3_S1_bytes)
    # print('S2',CH1_S2_bytes, CH2_S2_bytes, CH3_S2_bytes)

    # Read acceleration from MPU6050
    
    
    #append data on the csv file
    # i=i+1
    # now = dt.now()
    # file.write(str(now)+","+str(accel_data['x'])+","+str(accel_data['y'])+","+str(accel_data['z'])+"\n")
    # file.flush()

    # Add x and y to lists
    xs.append(dt.now().strftime('%H:%M:%S.%f'))
    ys.append(CH1_S1_Decoded)
    
    # Limit x and y lists to 20 items
    xs = xs[-10:]
    ys = ys[-10:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('MPU6050 X Acceleration over Time')
    plt.ylabel('X-Acceleration')



while True:
    #show real-time graph
    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
    plt.show()