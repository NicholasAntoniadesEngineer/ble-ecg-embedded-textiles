# Introduction 
The Caterpillar textile is required to measure ECG readings from electrodes placed in specific locations within the textile. Tests need to be done to determine these locations. A testing system was needed to be built with repositionable leads to allow for tests to be run with the electrodes placed in different combinations of locations. The system needed to be robust enough to handle repetitive stretching and allow for data to be captured during each test for analysis. 

Using the pod from the Caterpillar Beta system to capture the ECG and IMU data a Raspberrypi 4B was used to capture the data being sent over Bluetooth and store it.

The firmware running on the P01-ECG pos can be find in the P01-ECG-pod-firmware repository

# Current Raspberry PI4 login details
- Username: protopi
- Password: kymira 

# Getting Started

1.  Connect the Raspberry Pi to the local network
    - Start raspi-config with: sudo raspi-config.
    - Go into System Options > Wireless LAN.
    - Type your SSID and your password.
    - Exit the tool. After a few seconds, your Pi is now connected to the wireless network you chose.
2.  Clone repository from git.
    - sudo git clone https://KYMIRARnD@dev.azure.com/KYMIRARnD/Garment%20Integration%20and%20Prototyping/_git/P01-ECG
3.	Change file permissions
    - sudo chmod -R ugo+rw P01-ECG/
    - sudo chown -R protopi:root P01-ECG/
4.	Install libraries


# Build and Test

1. Optional changes to code
    - Change the device_new variable to the desired Pod ID.
    - Change TEST_NAME variable to the desired test name. 
2. Run from command line
    - python3 ./Pod_data_capture.py 


# Optional plotting using jupyter notebook

1. Install modules
    - Open /P01-ECG/Signal Processing/read_ecg_data
    - Run sudo pip install -e ./
    - Open /P01-ECG/Signal Processing/ECG_data_processing_modules_gen1/modules/kymira_ecg
    - Run sudo pip install -e ./
2. Run jupyter notebook
    - run 'jupyter notebook' in the command line
    - navigate to /P01-ECG/Signal Processing/ECG_data_processing_modules_gen1/notebook_projects/ecg_dq_dashboard
    - run kymira_ecg_dq.ipynb
    - Change the location variable to that of the test to be plotted.show a value error otherwise.  




