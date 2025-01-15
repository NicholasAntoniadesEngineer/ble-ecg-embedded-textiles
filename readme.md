# ECG IMU Garment Prototype (2021)

A garment was required to measure ECG readings from electrodes placed in specific locations within the textile. Tests need to be done to determine these locations. A testing system was needed to be built with repositionable leads to allow for tests to be run with the electrodes placed in different combinations of locations. The system needed to be robust enough to handle repetitive stretching and allow for data to be captured during each test for analysis.

The project involves integrating with an existing BLE ECG device from another product in research to capture the ECG and IMU data. A Raspberry Pi 4B was used to capture the data being sent over Bluetooth to be stored and analyzed.

## Project Goals

- Determine optimal electrode placement within the garment for accurate ECG readings.
- Develop a robust testing system that can withstand repetitive stretching.
- Integrate with existing BLE ECG devices for data capture.
- Ensure reliable data capture and analysis during each test.

## Hardware Components

- Raspberry Pi 4B (main controller)
- BLE ECG device
- Repositionable leads for electrode placement
- Textile-based electrodes
- Bluetooth Low Energy (BLE) communication module

## Getting Started

1. **Connect the Raspberry Pi to the local network**
   - Start `raspi-config` with: `sudo raspi-config`.
   - Go into System Options > Wireless LAN.
   - Type your SSID and your password.
   - Exit the tool. After a few seconds, your Pi is now connected to the wireless network you chose.

2. **Clone the repository from git**
   - `sudo git clone ../repo`

3. **Change file permissions**
   - `sudo chmod -R ugo+rw ../repo`
   - `sudo chown -R protopi:root ../repo`

4. **Install libraries**
   - Ensure all necessary Python libraries are installed for data capture and processing.

## Build and Test

1. **Optional changes to code**
   - Change the `device_new` variable to the desired Pod ID.
   - Change `TEST_NAME` variable to the desired test name.

2. **Run from command line**
   - `python3 ./Pod_data_capture.py`

## Optional Plotting using Jupyter Notebook

1. **Install modules**
   - Open `/P01-ECG/Signal Processing/read_ecg_data`
   - Run `sudo pip install -e ./`
   - Open `/P01-ECG/Signal Processing/ECG_data_processing_modules_gen1/modules/_ecg`
   - Run `sudo pip install -e ./`

2. **Run Jupyter Notebook**
   - Run `jupyter notebook` in the command line.
   - Navigate to `/P01-ECG/Signal Processing/ECG_data_processing_modules_gen1/notebook_projects/ecg_dq_dashboard`
   - Run `kymira_ecg_dq.ipynb`
   - Change the location variable to that of the test to be plotted. A value error will be shown otherwise.

## Additional Information

- The system architecture includes a Raspberry Pi 4B as the main controller, similar to the ECG Driver Monitoring Steering Wheel project.
- The project aims to ensure robust data capture and analysis, accommodating the unique challenges of textile-based ECG measurement.




