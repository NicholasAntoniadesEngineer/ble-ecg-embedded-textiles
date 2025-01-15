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

## Software Components

1. **Data Acquisition**
   - BLE communication handling
   - ECG and IMU data sampling
   - Real-time data processing

2. **Signal Processing**
   - Bandpass filtering
   - R-peak detection
   - Noise reduction algorithms

