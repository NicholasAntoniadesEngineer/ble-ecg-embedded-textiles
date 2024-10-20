/* Microchip Technology Inc. and its subsidiaries.  You may use this software 
 * and any derivatives exclusively with Microchip products. 
 * 
 * THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS".  NO WARRANTIES, WHETHER 
 * EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED 
 * WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A 
 * PARTICULAR PURPOSE, OR ITS INTERACTION WITH MICROCHIP PRODUCTS, COMBINATION 
 * WITH ANY OTHER PRODUCTS, OR USE IN ANY APPLICATION. 
 *
 * IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE, 
 * INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND 
 * WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS 
 * BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE.  TO THE 
 * FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS 
 * IN ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF 
 * ANY, THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
 *
 * MICROCHIP PROVIDES THIS SOFTWARE CONDITIONALLY UPON YOUR ACCEPTANCE OF THESE 
 * TERMS. 
 */

/* 
 * File:   
 * Author: 
 * Comments:
 * Revision history: 
 */

// This is a guard condition so that contents of this file are not included
// more than once.  
#ifndef ADS1293_H
#define	ADS1293_H
#include "typedefs.h"

#define flex_ch(pos,neg) ((neg)+(pos<<3))

#define ECG_BUF_SIZE 0x6
#define ERROR_BUF_SIZE 0x7

#define REG_REVID 0x40

#define ADS1293_P2_N1 flex_ch(2,1)
#define ADS1293_P3_N1 flex_ch(3,1)

#define ADS1293_CMDET_1_2_3 0x07

/********** Define for ADS1293 REGISTERS *************/

#define ADS1293_CONFIG 0x00

//Input Channel Selection Registers

#define ADS1293_FLEX_CH1_CN     0x01
#define ADS1293_FLEX_CH2_CN     0x02
#define ADS1293_FLEX_CH3_CN     0x03
#define ADS1293_FLEX_PACE_CN    0x04
#define ADS1293_VBAT_PACE_CN    0x05

//Lead-off Detect Control Registers

#define ADS1293_LOD_CN          0x06
#define ADS1293_LOD_EN          0x07
#define ADS1293_LOD_CURRENT     0x08
#define ADS1293_LOD_AC_CN       0x09

//Common-Mode Detection and Right-Leg Drive FB Control Registers

#define ADS1293_CMDET_EN        0x0A
#define ADS1293_CMDET_CN        0x0B
#define ADS1293_RLD_CN          0x0C

//Wilson Control Registers

#define ADS1293_WILSON_EN1      0x0D
#define ADS1293_WILSON_EN2      0x0E
#define ADS1293_WILSON_EN3      0x0F
#define ADS1293_WILSON_CN       0x10

//Reference Registers

#define ADS1293_REF_CN          0x11

//OSC Control Registers

#define ADS1293_OSC_CN          0x12

//AFE Control Registers

#define ADS1293_AFE_RES         0x13
#define ADS1293_AFE_SHDN_CN     0x14
#define ADS1293_AFE_FAULT_CN    0x15
#define ADS1293_AFE_PACE_CON    0x17

//Error Status Registers

#define ADS1293_ERROR_LOD       0x18
#define ADS1293_ERROR_STATUS    0x19
#define ADS1293_ERROR_RANGE1    0x1A
#define ADS1293_ERROR_RANGE2    0x1B
#define ADS1293_ERROR_RANGE3    0x1C
#define ADS1293_ERROR_SYNC      0x1D
#define ADS1293_ERROR_MISC      0x1E

//Digital Registers

#define ADS1293_DIGO_STRENGTH   0x1F
#define ADS1293_R2_RATE         0x21
#define ADS1293_R3_RATE_CH1        0x22
#define ADS1293_R3_RATE_CH2        0x23
#define ADS1293_R3_RATE_CH3        0x24
#define ADS1293_R1_RATE         0x25
#define ADS1293_DIS_EFILTER     0x26
#define ADS1293_DRDYB_SRC       0x27
#define ADS1293_SYNCB_CN        0x28
#define ADS1293_MASK_DRDYB      0x29
#define ADS1293_MASK_ERR        0x2A
#define ADS1293_ALARM_FILTER    0x33
#define ADS1293_CH_CNFG         0x2F

//Pace and ECG Read Back Registers

#define ADS1293_DATA_STATUS     0x30
#define ADS1293_DATA_CH1_PACE_H   0x31
#define ADS1293_DATA_CH1_PACE_L   0x32
#define ADS1293_DATA_CH2_PACE_H   0x33
#define ADS1293_DATA_CH2_PACE_L   0x34
#define ADS1293_DATA_CH3_PACE_H   0x35
#define ADS1293_DATA_CH3_PACE_L   0x36

#define ADS1293_DATA_CH1_ECG_H   0x37
#define ADS1293_DATA_CH1_ECG_M   0x38
#define ADS1293_DATA_CH1_ECG_L   0x39
#define ADS1293_DATA_CH2_ECG_H   0x3A
#define ADS1293_DATA_CH2_ECG_M   0x3B
#define ADS1293_DATA_CH2_ECG_L   0x3C
#define ADS1293_DATA_CH3_ECG_H   0x3D
#define ADS1293_DATA_CH3_ECG_M   0x3E
#define ADS1293_DATA_CH3_ECG_L   0x3F

#define ADS1293_REVID            0x40
#define ADS1293_DATA_LOOP        0x50



///////THINGS

#define ECG_NUM_READINGS 10

#define ECG_DATA_LENGTH 6
#define ECG_DATA_LENGTH_LITE ECG_DATA_LENGTH
#define ECG_EEPROM_LENGTH 15
#define ECG_PACKET_SIZE ((ECG_NUM_READINGS*6)+3)
#define ECG_DATA_PACKET_LITE ECG_DATA_PACKET

typedef union
{
    struct
    {
        uint8_t ECG_H,ECG_M,ECG_L;

    } READINGS;
    uint8_t asUInt8s[3];
} ECG_READING;

typedef union
{
    struct __attribute__((__packed__)) 
    {
        ECG_READING  ECG1[ECG_NUM_READINGS];
        ECG_READING  ECG2[ECG_NUM_READINGS];
        uint8_t headerByte; //<ID 7:4> and <PACKET_TYPE 3:0>
        uint8_t crc;     //for future use
        uint8_t ready;
       
    } sensor;
    
    uint8_t asUInt8s[ECG_PACKET_SIZE];
    
} ECG_DATA_PACKET;


/** Specific settings for this board
 * Size should be multiples of 2 bytes - as it is stored and retrieved from
 *  EEPROM area of this micro
 */
#define FLAG_LITE (0x01)
#define FLAG_MUTE (0x02)

typedef union
{
    uint16_t asUInts[ECG_EEPROM_LENGTH];
    
    struct __attribute__((__packed__)) 
    {
        uint8_t constellationID;    //ID in this constellation, default 0 unassigned
        uint8_t flags;              //reserved
        uint16_t uniqueID;          //should be reasonably unique
        
        q14_t aRot11, aRot12, aRot13;   //Accelerometer calibration data
        q14_t aRot21, aRot22, aRot23;   //
        q14_t aRot31, aRot32, aRot33;   // Rotation matrix
        q11_t aOffX,  aOffY,  aOffZ;    // offset vector
        
        uint16_t slotMultiplier;
        
        //Add additional NV setting here
                
    };
} ECG_BOARD_SETTINGS_T;

#endif	/* XC_HEADER_TEMPLATE_H */


void ADS1293_init();

int ADS1293_testConnection();

void ADS1293_setupExtClockOC();

void ADS1293_getPacket(ECG_DATA_PACKET* current, int index);