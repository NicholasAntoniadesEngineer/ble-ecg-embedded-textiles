# Introduction 
The Caterpillar textile is required to measure ECG readings from electrodes placed in specific locations within the textile. Tests need to be done to determine these locations. A testing system was needed to be built with repositionable leads to allow for tests to be run with the electrodes placed in different combinations of locations. The system needed to be robust enough to handle repetitive stretching and allow for data to be captured during each test for analysis. 

Using the pod from the Caterpillar Beta system to capture the ECG and IMU data a Raspberrypi 4B was used to capture the data being sent over Bluetooth and store it.

# Getting Started
TODO: Guide users through getting your code up and running on their own system. In this section you can talk about:
1.	Clone repository from git.
    - sudo git clone https://KYMIRARnD@dev.azure.com/KYMIRARnD/Garment%20Integration%20and%20Prototyping/_git/P01-ECG
2.	Change file permissions
    - sudo chmod -R ugo+rw P01-ECG/
3.	Install libraries


# Build and Test
TODO: Describe and show how to build your code and run the tests. 
1. Optional changes to code
    - Change the device_new variable to the desired Pod ID.
    - Change TEST_NAME variable to the desired test name. 
2. Run from command line
    - python3 ./Pod_data_capture.py 

