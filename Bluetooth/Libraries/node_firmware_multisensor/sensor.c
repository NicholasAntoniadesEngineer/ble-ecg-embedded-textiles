
#include "typedefs.h"
#include "sensor.h"
#include <p24F16KA101.h>

int sensor_init(BOARD_SETTINGS_T *settings)
{
#if (SENSOR == SENSOR_IMU)
    BMI160_init();
    BMI160_setOffsets(settings);
    return 1;
#elif (SENSOR == SENSOR_ECG)
    ADS1293_setupExtClockOC();
    ADS1293_init();
#elif (SENSOR == SENSOR_STRAIN)
    adc_init();
#elif (SENSOR == SENSOR_PPG)
    max32664_init();
    PPG_raw_data();
#endif
    return 1;    
}

int sensor_test_connection()
{
#if (SENSOR == SENSOR_IMU)
    BMI160_init();
    return BMI160_testConnection();
#elif (SENSOR == SENSOR_ECG)
    return ADS1293_testConnection();
#elif (SENSOR == SENSOR_STRAIN)
    return 1;
#elif (SENSOR == SENSOR_PPG)
    return MAX32664_testConnection();
#else
    return 1;
#endif
}

void sensor_get_packet_full(DATA_PACKET_T* readings, int index)
{   
#if (SENSOR == SENSOR_IMU)
    BMI160_getMotion9Packet(readings);
#elif (SENSOR == SENSOR_ECG)    
    ADS1293_getPacket(readings, index);
#elif (SENSOR == SENSOR_STRAIN)
    Strain_getPacket(readings);
#elif (SENSOR == SENSOR_PPG)
    MAX32664_getPacket(readings);
#endif
}

void sensor_get_packet_lite(DATA_PACKET_LITE* readings, int index)
{    
#if (SENSOR == SENSOR_IMU)
    BMI160_getMotion6Packet(readings);
#elif (SENSOR == SENSOR_ECG)    
    ADS1293_getPacket(readings, index);
#elif (SENSOR == SENSOR_STRAIN)
    Strain_getPacket(readings);
#elif (SENSOR == SENSOR_PPG)
    MAX32664_getPacket(readings);
#endif
}