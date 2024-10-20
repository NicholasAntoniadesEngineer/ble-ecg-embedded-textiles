/* 
 * File:   ads1118.h
 * Author: OllaEltiraifi
 *
 * Created on 14 January 2021, 16:06
 */

#ifndef ADS1118_H
#define	ADS1118_H

#include <xc.h>

#define ADC_DATA_LENGTH 24
#define ADC_EEPROM_LENGTH 15
#define ADC_NUM_READINGS 1  

typedef union
{
    struct
    {
        uint8_t ADC_H,ADC_L;

    } READINGS;
    uint8_t asUInt8s[2];
} ADC_READING;


typedef union
{
    struct __attribute__((__packed__)) 
    {
        ADC_READING ADC1;
        ADC_READING ADC2;
        ADC_READING ADC3;
        uint16_t unused0[7];       //padding
        uint8_t headerByte; //<ID 7:4> and <PACKET_TYPE 3:0>
        uint8_t crc;     //for future use
        uint8_t unused1;     //padding OR flags for Acc/Gyro ranges?
        uint8_t unused2;     //padding OR flags for Acc/Gyro ranges?
       
    } sensor;
    
    uint8_t asUInt8s[ADC_DATA_LENGTH];
    
} ADC_DATA_PACKET;


/** Specific settings for this board
 * Size should be multiples of 2 bytes - as it is stored and retrieved from
 *  EEPROM area of this micro
 */
#define FLAG_LITE (0x01)
#define FLAG_MUTE (0x02)

typedef union
{
    uint16_t asUInts[ADC_EEPROM_LENGTH];
    
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
} ADC_BOARD_SETTINGS;


void ADS1118_init();

void ADS1118_getpacket(ADC_DATA_PACKET* readings);

#endif	/* ADS1118_H */

