/* 
 * File:   ppg.h
 * Author: KarlSainzMartinez
 *
 * Created on 16 November 2020, 13:27
 */

#ifndef PPG_H
#define	PPG_H

#include "typedefs.h"

#ifdef	__cplusplus
extern "C" {
#endif

#define REG_INTR_STATUS_1 0x00
#define REG_INTR_STATUS_2 0x01
#define REG_INTR_ENABLE_1 0x02
#define REG_INTR_ENABLE_2 0x03
#define REG_FIFO_WR_PTR 0x04
#define REG_OVF_COUNTER 0x05
#define REG_FIFO_RD_PTR 0x06
#define REG_FIFO_DATA 0x07
#define REG_FIFO_CONFIG 0x08
#define REG_MODE_CONFIG 0x09
#define REG_SPO2_CONFIG 0x0A
#define REG_LED1_PA 0x0C
#define REG_LED2_PA 0x0D
#define REG_PILOT_PA 0x10
#define REG_MULTI_LED_CTRL1 0x11
#define REG_MULTI_LED_CTRL2 0x12
#define REG_TEMP_INTR 0x1F
#define REG_TEMP_FRAC 0x20
#define REG_TEMP_CONFIG 0x21
#define REG_PROX_INT_THRESH 0x30
#define REG_REV_ID 0xFE
#define REG_PART_ID 0xFF

    
#define PPG_DATA_LENGTH 24
#define PPG_EEPROM_LENGTH 15
#define PPG_NUM_READINGS 1  

typedef union
{
    struct
    {
        uint8_t ppg_h,ppg_m,ppg_l;

    } READINGS;
    uint8_t asUInt8s[3];
} PPG_READING;
    
typedef union
{
    struct __attribute__((__packed__)) 
    {
        PPG_READING  rled[2]; //int24 red led & IR led values
        PPG_READING  irled[2]; //int24 red led & IR led values
        uint16_t unused0[4];       //padding
        uint8_t headerByte; //<ID 7:4> and <PACKET_TYPE 3:0>
        uint8_t crc;     //for future use
        uint8_t unused1;     //padding OR flags for Acc/Gyro ranges?
        uint8_t unused2;     //padding OR flags for Acc/Gyro ranges?
       
    } sensor;
    
    uint8_t asUInt8s[PPG_DATA_LENGTH];
    
} PPG_DATA_PACKET;


/** Specific settings for this board
 * Size should be multiples of 2 bytes - as it is stored and retrieved from
 *  EEPROM area of this micro
 */
#define FLAG_LITE (0x01)
#define FLAG_MUTE (0x02)

typedef union
{
    uint16_t asUInts[PPG_EEPROM_LENGTH];
    
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
} PPG_BOARD_SETTINGS;

#ifdef	__cplusplus
}
#endif

#endif	/* PPG_H */

