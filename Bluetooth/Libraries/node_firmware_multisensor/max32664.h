/* 
 * File:   max32664.h
 * Author: OllaEltiraifi
 *
 * Created on 11 January 2021, 12:06
 */

#ifndef MAX32664_H
#define	MAX32664_H


#include "I2Clib.h"

// MAX32664 I2C Message Protocol Definitions
//Host command consist of just a Family Byte and Index Byte or a Family Byte, an Index Byte and a Write Byte/s 

//Read Sensor Hub Status 

#define SENSOR_STATUS_1             0x00
#define SENSOR_STATUS_2             0x00

// Read the sensor type

#define SENSOR_TYPE_1               0xFF
#define SENSOR_TYPE_2               0x00
#define MAX32664_ID                 0x01


//Select the Device Operating Mode
#define DEVICE_MODE_1               0x01
#define DEVICE_MODE_2               0x00
#define WRITE_APPLICATION_MODE      0x00
#define DEVICE_SHUTDOWN             0x01
#define DEVICE_RESET                0X02  
#define WRITE_BOOTLOADER_MODE       0X08

//Read the Device Operating Mode
#define READ_MODE_1                 0X02
#define READ_MODE_2                 0X00
#define READ_APPLICATION_MODE       0X00
#define READ_RESET                  0X02
#define READ_BOOTLOADER_MODE        0X08


//Set Output Mode
#define OUTPUT_MODE_1               0X10
#define OUTPUT_MODE_2               0X00
#define NO_DATA_1                   0X00
#define SENSOR_DATA                 0x01
#define ALGORITHM_DATA              0X02
#define SEN_ALGO_DATA               0X03
#define NO_DATA_2                   0X04
#define SC_SENSOR_DATA              0x05
#define SC_ALGORITHM_DATA           0X06
#define SC_SEN_ALGO_DATA            0X07


//Set the Threshold for FIFO
#define FIFO_THRESOLD_1             0X10
#define FIFO_THRESOLD_2             0X01

//Read Output FIFO
//Get the number of samples in the FIFO
#define NUMBER_OF_SAMPLES_1         0X12
#define NUMBER_OF_SAMPLES_2         0X00

//Read Output FIFO
//Read the data stored in the output FIFO
#define FIFO_DATA_1                 0X12
#define FIFO_DATA_2                 0X01

//Write a value to a writable MAX86141 register.
#define WRITE_MAX86141_1            0X40
#define WRITE_MAX86141_2            0X00

//Write a value to a writable accelerometer register.
#define WRITE_ACCELEROMETER_1       0X40
#define WRITE_ACCELEROMETER_2       0X04

//Read the value of a MAX86141 register.
#define READ_MAX86141_1             0X41
#define READ_MAX86141_2             0X00

//Read the value of an accelerometer register.
#define READ_ACCELEROMETER_1        0X41
#define READ_ACCELEROMETER_2        0X04

//Enable the MAX86141 sensor. DELAY = 250ms
#define MODE_MAX86141_1             0X44
#define MODE_MAX86141_2             0X00
#define DISABLE_MAX86141            0x00
#define ENABLE_MAX86141             0x01

//Enable the accelerometer sensor. DELAY = 20ms
#define MODE_ACCELEROMETER_1        0X44
#define MODE_ACCELEROMETER_2        0X04

#define DISABLE_ACCELEROMETER_1     0x00
#define DISABLE_ACCELEROMETER_2     0x00
#define DISABLE_EXT_ACCELEROMETER_1 0x00
#define DISABLE_EXT_ACCELEROMETER_2 0x01

#define ENABLE_ACCELEROMETER_1      0x01
#define ENABLE_ACCELEROMETER_2      0x00
#define ENABLE_EXT_ACCELEROMETER_1  0x01
#define ENABLE_EXT_ACCELEROMETER_2  0x01

#define PPG1_DATA_LENGTH 24
#define PPG1_EEPROM_LENGTH 15
#define PPG1_NUM_READINGS 1  

typedef union
{
    struct
    {
        uint8_t PPG_H,PPG_M,PPG_L;

    } READINGS;
    uint8_t asUInt8s[3];
} PPG1_READING;
    
typedef union
{
    struct __attribute__((__packed__)) 
    {
        PPG1_READING  GLED;      //Green led values (PPG1)
        PPG1_READING  GLED2;     //Green led values (PPG12)
        PPG1_READING  IRLED;     //IR led values (PPG1)
        PPG1_READING  IRLED2;    //IR led values (PPG12)
        PPG1_READING  RLED;      //Red led values (PPG1)
        PPG1_READING  RLED2;     //Red led values (PPG12)
        uint16_t  unused3;          //padding
        uint8_t headerByte; //<ID 7:4> and <PACKET_TYPE 3:0>
        uint8_t crc;     //for future use
        uint8_t unused1;     //padding OR flags for Acc/Gyro ranges?
        uint8_t unused2;     //padding OR flags for Acc/Gyro ranges?
       
    } sensor;
    
    uint8_t asUInt8s[PPG1_DATA_LENGTH];
    
} PPG1_DATA_PACKET;


/** Specific settings for this board
 * Size should be multiples of 2 bytes - as it is stored and retrieved from
 *  EEPROM area of this micro
 */
#define FLAG_LITE (0x01)
#define FLAG_MUTE (0x02)

typedef union
{
    uint16_t asUInts[PPG1_EEPROM_LENGTH];
    
    struct __attribute__((__packed__)) 
    {
        uint8_t constellationID;    //ID in this constellation, default 0 unassigned
        uint8_t flags;              //reserved
        uint16_t uniqueID;          //should be reasonably unique
        
        uint16_t aRot11, aRot12, aRot13;   //Accelerometer calibration data
        uint16_t aRot21, aRot22, aRot23;   //
        uint16_t aRot31, aRot32, aRot33;   // Rotation matrix
        uint16_t aOffX,  aOffY,  aOffZ;    // offset vector
        
        uint16_t slotMultiplier;
        
        //Add additional NV setting here
                
    };
} PPG1_BOARD_SETTINGS;


void max32664_init();

void application_mode();

void set_dev_mode();

void get_dev_mode();

void system_swon();

int MAX32664_testConnection();

void PPG_raw_data();

void MAX32664_getPacket(PPG1_DATA_PACKET *readings);



#endif	/* MAX32664_H */

