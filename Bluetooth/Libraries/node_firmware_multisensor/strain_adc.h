/* 
 * File:   strain_adc.h
 * Author: OllaEltiraifi
 *
 * Created on 25 December 2020, 13:11
 */

#ifndef STRAIN_ADC_H
#define	STRAIN_ADC_H

#include "xc.h"

#ifdef	__cplusplus
extern "C" {
#endif

    
#define Strain_DATA_LENGTH 24
#define Strain_EEPROM_LENGTH 15
#define Strain_NUM_READINGS 1  

  
typedef union
{
    struct __attribute__((__packed__)) 
    {
        int16_t SG1, SG2, SG3;
        uint16_t unused0[7];       //padding
        uint8_t headerByte; //<ID 7:4> and <PACKET_TYPE 3:0>
        uint8_t crc;     //for future use
        uint8_t unused1;     //padding OR flags for Acc/Gyro ranges?
        uint8_t unused2;     //padding OR flags for Acc/Gyro ranges?
       
    } sensor;
    
    uint8_t asUInt8s[Strain_DATA_LENGTH];
    
} Strain_DATA_PACKET;


/** Specific settings for this board
 * Size should be multiples of 2 bytes - as it is stored and retrieved from
 *  EEPROM area of this micro
 */
#define FLAG_LITE (0x01)
#define FLAG_MUTE (0x02)

typedef union
{
    uint16_t asUInts[Strain_EEPROM_LENGTH];
    
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
} Strain_BOARD_SETTINGS;



void adc_init();

int start_sampling();

void Strain_getPacket(Strain_DATA_PACKET* readings);
#endif	/* STRAIN_ADC_H */

