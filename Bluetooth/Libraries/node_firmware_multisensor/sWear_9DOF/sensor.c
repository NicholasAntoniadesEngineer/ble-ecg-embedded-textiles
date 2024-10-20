
#include "typedefs.h"
#include "sensor.h"
#include <p24F16KA101.h>
#include <string.h>

void sensor_init()
{
#if (SENSOR == SENSOR_IMU)
    BMI160_init();
#elif (SENSOR == SENSOR_ECG)
    ADS1293_setupExtClockOC();
    ADS1293_init();
#endif
    
}

int sensor_test_connection()
{
#if (SENSOR == SENSOR_IMU)
    return BMI160_testConnection();
#elif (SENSOR == SENSOR_ECG)
    return ADS1293_testConnection();
#elif (SENSOR == SENSOR_IMU_SIMULATED)
    return 1;
#endif
}

void sensor_get_packet_full(DATA_PACKET_T* readings, int index)
{   
#if (SENSOR == SENSOR_IMU)
    BMI160_getMotion9Packet(readings);
#elif (SENSOR == SENSOR_ECG)    
    ADS1293_getPacket(readings, index);
#elif (SENSOR == SENSOR_IMU_SIMULATED)
    memset(readings,0,sizeof(readings));
#endif
}

void sensor_get_packet_lite(DATA_PACKET_LITE* readings, int index)
{    
#if (SENSOR == SENSOR_IMU)
    BMI160_getMotion6Packet(readings);
#elif (SENSOR == SENSOR_ECG)    
    ADS1293_getPacket(readings, index);
#elif (SENSOR == SENSOR_IMU_SIMULATED)
#endif
}