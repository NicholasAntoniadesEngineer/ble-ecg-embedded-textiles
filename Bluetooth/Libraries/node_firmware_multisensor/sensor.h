/* 
 * File:   sensor.h
 * Author: KarlSainzMartinez
 *
 * Created on 21 April 2020, 16:34
 */

#ifndef SENSOR_H
#define	SENSOR_H
#include "typedefs.h"

#define SENSOR_IMU 1
#define SENSOR_ECG 2
#define SENSOR_STRAIN 3
#define SENSOR_PPG 4


#define SENSOR SENSOR_STRAIN


#if SENSOR == SENSOR_IMU

#include "bmi160bmm150.h"
#define NUM_READINGS 1
#define EEPROM_LENGTH IMU_EEPROM_LENGTH

#define DATA_PACKET_T IMU_DATA_PACKET_T
#define DATA_PACKET_LITE IMU_DATA_PACKET_LITE

#define DATA_LENGTH IMU_DATA_LENGTH
#define DATA_LENGTH_LITE IMU_DATA_LENGTH_LITE
#define BOARD_SETTINGS_T IMU_BOARD_SETTINGS_T

#elif SENSOR == SENSOR_ECG

#include "ads1293.h"
#define NUM_READINGS ECG_NUM_READINGS
#define EEPROM_LENGTH ECG_EEPROM_LENGTH
#define DATA_PACKET_T ECG_DATA_PACKET
#define DATA_PACKET_LITE ECG_DATA_PACKET

#define DATA_LENGTH ECG_DATA_LENGTH
#define DATA_LENGTH_LITE ECG_DATA_LENGTH_LITE

#define BOARD_SETTINGS_T ECG_BOARD_SETTINGS_T

#elif SENSOR == SENSOR_STRAIN

#include "strain_adc.h"


#define NUM_READINGS Strain_NUM_READINGS
#define EEPROM_LENGTH Strain_EEPROM_LENGTH
#define DATA_PACKET_T Strain_DATA_PACKET
#define DATA_PACKET_LITE Strain_DATA_PACKET

#define DATA_LENGTH Strain_DATA_LENGTH
#define DATA_LENGTH_LITE Strain_DATA_LENGTH

#define BOARD_SETTINGS_T Strain_BOARD_SETTINGS

#elif SENSOR == SENSOR_PPG

#include "max32664.h"
#define NUM_READINGS PPG1_NUM_READINGS
#define EEPROM_LENGTH PPG1_EEPROM_LENGTH
#define DATA_PACKET_T PPG1_DATA_PACKET
#define DATA_PACKET_LITE PPG1_DATA_PACKET

#define DATA_LENGTH PPG1_DATA_LENGTH
#define DATA_LENGTH_LITE PPG1_DATA_LENGTH

#define BOARD_SETTINGS_T PPG1_BOARD_SETTINGS


#endif



#define MULT_MIN 6
#define MULT_MAX 10

#define FLAG_LITE (0x01)
#define FLAG_MUTE (0x02)

typedef enum
{
    PROTOCOL_Idle = 0,
    PROTOCOL_SetUID,
    PROTOCOL_SetCID,
    PROTOCOL_ReadEE,
    PROTOCOL_WriteEE,
    PROTOCOL_Mute,
    PROTOCOL_Lite,
} PROTOCOL_FSM_T;

extern uint16_t doPacing;
extern BOARD_SETTINGS_T boardSettings;

int sensor_init();
int sensor_test_connection();
void sensor_get_packet_full(DATA_PACKET_T* readings, int index);
void sensor_get_packet_lite(DATA_PACKET_LITE* readings, int index);

#endif