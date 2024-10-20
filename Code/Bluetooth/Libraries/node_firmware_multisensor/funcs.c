//Microcontroller  PIC24F16KA101  20pin QFN
#include "funcs.h"
#include "typedefs.h"
#include "board_comms.h"
#include "BMI160BMM150.h"
#include "base64.h"
#include <xc.h>
#include "sensor.h"
#include "ppg.h"

//RB0  - LED   (U2TX for modulation?)       o
//RB2  - URX                                i
//RB4  - UEN                                o
//RB7  - UTX                                i
//RA6  - IMU INT  (INT2)                    i
//RB12 - IMU SCK  (SCK1)                    o
//RB13 - IMU MOSI (SDO1)                    o
//RB14 - IMU MISO (SDI1)                    i
//RB15 - IMU CS                             o

#define _T6IF PIR3bits.TMR6IF
#define LED _LATB0
#define UTXEN _LATB4

#define LEDon() _LATB0=0
#define LEDoff() _LATB0=1

#define uTX(v) {FIFO[fifoHead] = v; fifoHead++; fifoHead&=FIFO_MASK;}

#define txWindowTimerSetup() { T2CON=0x0010; _T2IF=0; TMR2=0; PR2 = (uint16_t)((100 + 300*boardSettings.constellationID)*boardSettings.slotMultiplier); } //Karl: changed to suit new speeds
#define txWindowTimerStart() { TMR2=0; T2CON=0x8010; _T2IF=0; }
#define txWindowTimerStop()  { T2CON=0x0010; }
#define txWindowTimerIF _T2IF

#define FIFO_MASK 0x7f
#define FIFO_SIZE 0x80
unsigned char FIFO[FIFO_SIZE]; //0x1f mask
unsigned char fifoHead, fifoTail;

#define rxFIFO_MASK 0x3f
#define rxFIFO_SIZE 0x40
unsigned char rxFIFO[64];
unsigned char rxHead, rxTail;

BOARD_SETTINGS_T boardSettings;
PROTOCOL_FSM_T protocolFSM;

unsigned int bSendData;
uint16_t doPacing;

uint8_t crc8;
unsigned char accNew;
DATA_PACKET_T currentReadings;
DATA_PACKET_LITE currentReadingsLite;

// see \sa BOARD_SETTINGS_T for layout if int16_t in EEPROM 
eeprom_t eeData[EEPROM_LENGTH] = {0x0003, 0xFFF3, 0x4000, 0,0, 0,0x4000,0, 0,0,0x4000, 0,0,0,8};

unsigned char samplingTimer=0;
unsigned char rxWaiting=1;
unsigned char rxByteCount=0;
unsigned char shouldUpdate=0;

void shortWait(unsigned int us){ unsigned int a,b; for (a=0; a<us; a++) for (b=0; b<2; b++) Nop(); }
void longWait(unsigned int ms) {  unsigned int a,b; for (a=0; a<ms; a++) for (b=0; b<2000; b++) Nop(); }

unsigned char nibbleToASCII(unsigned char v)
{
	v&=0xf;
	if (v>9) return 55+v; else return '0'+v;
}

unsigned char ASCIItoNibble(unsigned char v)
{
	if (v<'0') return 0; else
	if (v<':') return v-'0'; else
	if (v<'A') return 0; else
	if (v<'G') return v-55; else
	if (v<'a') return 0; else
	if (v<'g') return v-87; else return 0;
}

unsigned int isValidASCIIHEX(unsigned char v)
{
    if (v<'0') return 0; else
	if (v<':') return 1; else
	if (v<'A') return 0; else
	if (v<'G') return 1; else
	if (v<'a') return 0; else
	if (v<'g') return 1; else return 0;    
}

//Stolen from http://forum.arduino.cc/index.php?topic=37648.0
unsigned char docrc8(unsigned char value)
{
    unsigned char i,sum;

    for (i=0; i<8; i++)
    {
        sum = (crc8 ^ value) & 1;
        crc8>>=1;
        if (sum) crc8^=0x8c;
        
        value>>=1;
    }  
    
    return crc8;
}

/**
 * \brief Grab uint16_t from EEPROM from a given offset
 * @param ee_addr_offset 0-255 location inside the EEPROM
 * @return uint16_t value from EEPROM
 */
uint16_t ReadEEPROM(uint16_t ee_addr_offset){
    
    uint16_t data, offset;
    
    TBLPAG = __builtin_tblpage(&eeData);
    offset = __builtin_tbloffset(&eeData);
    data = __builtin_tblrdl(offset + ee_addr_offset);
    return (data);
}

/**
 * \brief Write a single uint16_t at a given offset in EEPROM
 * @param ee_addr_offset 0-255 location within the EEPROM area
 * @param ee_data uint16_t value to write into that location
 * \note 
 */
void WriteEEPROM(unsigned int ee_addr_offset, unsigned int ee_data){
    
    unsigned int offset;
    
    /* Do single word erase first */
    NVMCON = 0x4058; // Set up NVMCON to erase one word of data EEPROM
    TBLPAG = __builtin_tblpage(&eeData);
    offset = __builtin_tbloffset(&eeData) + ee_addr_offset;
    __builtin_tblwtl(offset, 0);
    asm volatile ("disi #5"); // disable interrupts for 5 instructions
    __builtin_write_NVM();
    while(NVMCONbits.WR);
    
    /* Now write a single word to the erased location */
    NVMCON = 0x4004; // Set up NVMCON to write one word of data EEPROM
    TBLPAG = __builtin_tblpage(&eeData);
    offset = __builtin_tbloffset(&eeData) + ee_addr_offset;
    __builtin_tblwtl(offset, ee_data);
    asm volatile ("disi #5"); // disable interrupts for 5 instructions
    __builtin_write_NVM();
    while(NVMCONbits.WR);
}

void loadSettingsFromEEPROM(void)
{
    uint16_t i;
    for (i=0; i<EEPROM_LENGTH; i++)
    {
        boardSettings.asUInts[i]=ReadEEPROM(i*2);
    }
    currentReadings.sensor.headerByte = (boardSettings.constellationID << 4) |  SENSOR;
    
    if (!boardSettings.constellationID)
    {
        boardSettings.constellationID = boardSettings.uniqueID & 0xf;
        if (boardSettings.constellationID<2) boardSettings.constellationID+=2;
    }
}
//Configure the chip    Fosc 32MHz    Fcy 16MIPS

void setupPIC()
{
    CLKDIV=0;                // Divide FRCPLL by 1 -> 32MHz
	while(!OSCCONbits.LOCK); //wait for PLL to settle

    //we need to set up IO, pins
#if SENSOR == SENSOR_STRAIN
    AD1PCFG=0xfbff;         //AN10 is analog
#else
    AD1PCFG=0xffff;         //all digital
#endif
    LATA=0; TRISA=0x40;     //A6 INT
    LATB=1; TRISB=0xC304;   //B14 Strain Gauge     B2 URX        (B0 high LED OFF)

	//setup UART for RS485 xceiver ops
	fifoHead=0; fifoTail=0;
	rxHead=0;   rxTail=0;
    U1BRG=1;        //Karl: gives 500kBaud
	U1MODE=0x8800;
    U1STA =0x0400;
    UTXEN =0;
    _U1RXIF=0;  _U1RXIE=1; 

    //ADVANCED LED dimming option - UART2 TX PIN ~ 10kBaud
    U2BRG=99;       // gives 10kBaud
    U2MODE=0x8800; U2STA =0x0400;  
        
    
	//LED=1; accNew=0;


    //TMR2 used as timeout after receiving the ? trigger
	txWindowTimerSetup();

    comms_init();
    
    T1CON=0x8010;   //pre 1:8 gives 2MHz counting rate
    PR1 = (int)(40000/NUM_READINGS);    //gives 20ms nominal, tweak for exact value if needed
    _T1IF=0;
    
    protocolFSM=PROTOCOL_Idle;
    
    //Read EEPROM for default configuration or for user saved calibration data
    loadSettingsFromEEPROM();
    
    txWindowTimerSetup();
    
    doPacing=0;  //if we are NodeID1, we can suppress the transmission if needed
}

/** Add byte to TX FIFO - binary value untouched
 * 
 * @param Byte to load into TX FIFO
 */
void debugTX(unsigned char v)
{
    FIFO[fifoHead] = v;  fifoHead++; fifoHead&=FIFO_MASK;
}

/** Push the Frame Start '?' byte to the bus
 * 
 * \details This function is used by node with ID 1 to kick off a sample frame for the whole bus
 */
void reqFrame(void)
{
    FIFO[fifoHead] = '?';  fifoHead++; fifoHead&=FIFO_MASK;
}

/** 
 * \brief Calculate CRC-8 value
 */
void updateCRC(void)
{
    uint16_t i;
    crc8=0;
    
    for (i=0; i<20; i++) docrc8(currentReadings.asUInt8s[i]);
    currentReadings.sensor.crc = crc8;
}

/**
 *  \brief Send current IMU sample over network using Base64 encoding
 *  
 *  \details Take each in16 member of the current IMU sample, encode to Base64 then push resulting bytes to the TX FIFO buffer
 */
void queue_sensor_as_base_64(void)
{
    uint8_t temp, i;
    
    if (getFlag(FLAG_LITE)!=0)
    {
        for (i=0; i<DATA_LENGTH_LITE; i+=3)
        {
            temp=(currentReadingsLite.asUInt8s[i] >> 2) & 0x3f; 
            FIFO[fifoHead] = base64Lookup[temp];  fifoHead++; fifoHead&=FIFO_MASK;
            temp=(currentReadingsLite.asUInt8s[i] & 0x3) << 4;
            temp|=(currentReadingsLite.asUInt8s[i+1] >> 4);
            FIFO[fifoHead] = base64Lookup[temp];  fifoHead++; fifoHead&=FIFO_MASK;
            temp=(currentReadingsLite.asUInt8s[i+1] & 0xf) << 2;
            temp|=(currentReadingsLite.asUInt8s[i+2] >> 6) & 0x3;
            FIFO[fifoHead] = base64Lookup[temp];  fifoHead++; fifoHead&=FIFO_MASK;
            temp=(currentReadingsLite.asUInt8s[i+2] & 0x3f);
            FIFO[fifoHead] = base64Lookup[temp];  fifoHead++; fifoHead&=FIFO_MASK;
        }        
    }
    else
    { 
        for (i=0; i<DATA_LENGTH; i+=3)
        {
            temp=(currentReadings.asUInt8s[i] >> 2) & 0x3f; 
            FIFO[fifoHead] = base64Lookup[temp];  fifoHead++; fifoHead&=FIFO_MASK;
            temp=(currentReadings.asUInt8s[i] & 0x3) << 4;
            temp|=(currentReadings.asUInt8s[i+1] >> 4);
            FIFO[fifoHead] = base64Lookup[temp];  fifoHead++; fifoHead&=FIFO_MASK;
            temp=(currentReadings.asUInt8s[i+1] & 0xf) << 2;
            temp|=(currentReadings.asUInt8s[i+2] >> 6) & 0x3;
            FIFO[fifoHead] = base64Lookup[temp];  fifoHead++; fifoHead&=FIFO_MASK;
            temp=(currentReadings.asUInt8s[i+2] & 0x3f);
            FIFO[fifoHead] = base64Lookup[temp];  fifoHead++; fifoHead&=FIFO_MASK;
        }
    }
}

/**
 *  \brief Send current IMU sample over network using ASCII HEX encoding
 * 
 *  \details Take each byte within currentReadings and convert both nibble to ASCII HEX then push them to the TX FIFO buffer
 */
void queue_sensor_as_ASCII_HEX(void)
{
    uint8_t i;
    if (getFlag(FLAG_LITE)!=0)
    {
        for (i=0; i<DATA_LENGTH_LITE; i++)
        {
           FIFO[fifoHead] = nibbleToASCII(currentReadingsLite.asUInt8s[i]>>4);   fifoHead++; fifoHead&=FIFO_MASK;
           FIFO[fifoHead] = nibbleToASCII(currentReadingsLite.asUInt8s[i]&0xf);  fifoHead++; fifoHead&=FIFO_MASK;
        }
    }
    else
    {
        for (i=0; i<DATA_LENGTH; i++)
        {
           FIFO[fifoHead] = nibbleToASCII(currentReadings.asUInt8s[i]>>4);   fifoHead++; fifoHead&=FIFO_MASK;
           FIFO[fifoHead] = nibbleToASCII(currentReadings.asUInt8s[i]&0xf);  fifoHead++; fifoHead&=FIFO_MASK;
        }
    }
}

bool deferredFullDump;
void queueEEPROM(void)
{
    uint16_t i,target;
    
    if (deferredFullDump) target = EEPROM_LENGTH; else target = 2;
    for (i=0; i<target; i++)
    {
        FIFO[fifoHead] = nibbleToASCII(boardSettings.asUInts[i]>>12);  fifoHead++; fifoHead&=FIFO_MASK;
        FIFO[fifoHead] = nibbleToASCII(boardSettings.asUInts[i]>>8);   fifoHead++; fifoHead&=FIFO_MASK;
        FIFO[fifoHead] = nibbleToASCII(boardSettings.asUInts[i]>>4);   fifoHead++; fifoHead&=FIFO_MASK;
        FIFO[fifoHead] = nibbleToASCII(boardSettings.asUInts[i]);      fifoHead++; fifoHead&=FIFO_MASK;
    }
}

uint8_t protocolParameters[60];
uint8_t protocolParamCount;
uint16_t candidateUID=0;

 void doProtocolFSM(unsigned char c)
 {
     uint16_t i;
     switch (protocolFSM)
     {                 
         case PROTOCOL_Mute:
             if (isValidASCIIHEX(c))
             {
                protocolParameters[protocolParamCount++]=c;

                if (protocolParamCount==5)
                {
                    candidateUID = ASCIItoNibble(protocolParameters[0]); candidateUID<<=4;
                    candidateUID |= ASCIItoNibble(protocolParameters[1]); candidateUID<<=4;
                    candidateUID |= ASCIItoNibble(protocolParameters[2]); candidateUID<<=4;
                    candidateUID |= ASCIItoNibble(protocolParameters[3]);

                    if (candidateUID==boardSettings.uniqueID)
                    {
                        if (protocolParameters[4] == '1')
                        {
                            setFlag(FLAG_MUTE);
                        }
                        else if (protocolParameters[4]== '0')
                        {
                            clearFlag(FLAG_MUTE);
                        }
                        //WriteEEPROM(15,boardSettings.asUInts[15]);            //update eeprom
                       uTX('!'); uTX(nibbleToASCII(boardSettings.constellationID)) ; uTX('Q'); uTX(protocolParameters[4]);
                        
                    }
                    candidateUID=0;
                }
                break;
        case PROTOCOL_Lite:
            if (isValidASCIIHEX(c))
            {
               protocolParameters[protocolParamCount++]=c;

               if (protocolParamCount==5)
               {
                   candidateUID = ASCIItoNibble(protocolParameters[0]); candidateUID<<=4;
                   candidateUID |= ASCIItoNibble(protocolParameters[1]); candidateUID<<=4;
                   candidateUID |= ASCIItoNibble(protocolParameters[2]); candidateUID<<=4;
                   candidateUID |= ASCIItoNibble(protocolParameters[3]);

                   if (candidateUID==boardSettings.uniqueID)
                   {
                       if (protocolParameters[4] == '1')
                       {
                           setFlag(FLAG_LITE);
                       }
                       else if (protocolParameters[4]== '0')
                       {
                           clearFlag(FLAG_LITE);
                       }
                       //WriteEEPROM(16,boardSettings.asUInts[16]);            //update eeprom
                       uTX('!'); uTX(nibbleToASCII(boardSettings.constellationID)) ; uTX('M'); uTX(protocolParameters[4]); 

                   }
                   candidateUID=0;
               }
            } else protocolFSM=PROTOCOL_Idle;
            break;
             
         case PROTOCOL_SetUID:
             if (isValidASCIIHEX(c))
             {
                protocolParameters[protocolParamCount++]=c;

                if (protocolParamCount==4)
                {
                    candidateUID = ASCIItoNibble(protocolParameters[0]); candidateUID<<=4;
                    candidateUID |= ASCIItoNibble(protocolParameters[1]); candidateUID<<=4;
                    candidateUID |= ASCIItoNibble(protocolParameters[2]); candidateUID<<=4;
                    candidateUID |= ASCIItoNibble(protocolParameters[3]);

                    _TRISA1=1;
                    CNPU1|=0x8; //ENABLE weak pullup on CN3 (RA1)
                }
             } else protocolFSM=PROTOCOL_Idle;
             break;
             
         case PROTOCOL_SetCID:
             
             if (isValidASCIIHEX(c))
             {
                protocolParameters[protocolParamCount++]=c;

                if (protocolParamCount==5)
                {
                    candidateUID = ASCIItoNibble(protocolParameters[0]); candidateUID<<=4;
                    candidateUID |= ASCIItoNibble(protocolParameters[1]); candidateUID<<=4;
                    candidateUID |= ASCIItoNibble(protocolParameters[2]); candidateUID<<=4;
                    candidateUID |= ASCIItoNibble(protocolParameters[3]);

                    if (candidateUID==boardSettings.uniqueID)
                    {
                        boardSettings.constellationID = ASCIItoNibble(protocolParameters[4]);
                        WriteEEPROM(0,boardSettings.asUInts[0]);            //update eeprom
                        txWindowTimerSetup();                               //apply new offset due to CID
                        if (boardSettings.constellationID == 1) doPacing=1; //reenable pacing
                        uTX('!'); uTX(nibbleToASCII(boardSettings.constellationID)); 
                    }
                    candidateUID=0;

                    protocolFSM=PROTOCOL_Idle;
                }
             } else protocolFSM=PROTOCOL_Idle;
             break;

         case PROTOCOL_ReadEE:
             if (ASCIItoNibble(c) == boardSettings.constellationID) queueEEPROM();
             protocolFSM=PROTOCOL_Idle;
             break;

         case PROTOCOL_WriteEE:
             if (isValidASCIIHEX(c))
             {
                protocolParameters[protocolParamCount++]=ASCIItoNibble(c);

                if (protocolParamCount==51)
                {
                    if (protocolParameters[0]==boardSettings.constellationID)
                    {
                        crc8=0;
                        for (i=0; i<24; i++) docrc8(protocolParameters[2*i]<<4 | protocolParameters[2*i+1]);

                        if (crc8 == ((protocolParameters[49]<<4) | protocolParameters[50]))
                        {
                            for (i=0; i<12; i++)
                            {
                                candidateUID = protocolParameters[i*4+1]; candidateUID<<=4;
                                candidateUID |= protocolParameters[i*4+2]; candidateUID<<=4;
                                candidateUID |= protocolParameters[i*4+3]; candidateUID<<=4;
                                candidateUID |= protocolParameters[i*4+4]; 
                                WriteEEPROM(2*i+4,candidateUID);
                                loadSettingsFromEEPROM();
                            }
                            candidateUID=0;
                        }

                        uTX('!'); uTX(nibbleToASCII(crc8>>4)); uTX(nibbleToASCII(crc8)); 

                        protocolFSM=PROTOCOL_Idle;
                    } else
                    protocolFSM=PROTOCOL_Idle;
                }
             } else protocolFSM=PROTOCOL_Idle;
             break;
             
         case PROTOCOL_Idle:
             if ('@'==c) { protocolFSM=PROTOCOL_SetUID; protocolParamCount=0; } else
             if ('#'==c) { protocolFSM=PROTOCOL_SetCID; protocolParamCount=0; } else
             if ('$'==c) { protocolFSM=PROTOCOL_Mute; protocolParamCount=0;} else
             if ('['==c) { protocolFSM=PROTOCOL_Lite; protocolParamCount=0;} else
             if (','==c) { protocolFSM=PROTOCOL_ReadEE; deferredFullDump = 1; } else //complete dump on response
             if (';'==c) { protocolFSM=PROTOCOL_WriteEE; protocolParamCount=0; }
             
             break;
         default: break;    //nothing to do
     }
    }
 }

 int getFlag(char flag)
{
   return boardSettings.flags && flag; 
}

void setFlag(char flag)
{
    boardSettings.flags |= flag;
}

void clearFlag(char flag)
{
    boardSettings.flags &= (~flag);
}
 

void doContinuousRead(int ticks)
{
    sensor_get_packet_full(&currentReadings, ticks);
}

/**
 * \brief Called in the main loop, this is the main comms logic
 * 
 * \details Function checks for incoming characters, looks for '?' only (rev1.4) to kick off sample update, conversion, calibration and start TX offset timer
 * Function also deals with the TX of bytes from TX FIFO. As soon as TX of last byte has finished, the UTXEN signal is dropped and the bus is de-asserted
 */
void ProcessIO()
{
	unsigned char dummy;
	//our RS485
	if (rxHead!=rxTail)
	{
		if (candidateUID) { 
            candidateUID=0;             //cancel action on any reception
            CNPU1&=~0x8;
            LEDblink();
        }
        
        dummy = rxFIFO[rxTail]; rxTail++; rxTail&=rxFIFO_MASK;

        //timed RS485 slot responses come here
        if (dummy=='?' && !getFlag(FLAG_MUTE))             //Karl: Do not respond if we are muted
        {                           //usually we are granted 500uS   to do grab sample and do maths
            protocolFSM=PROTOCOL_Idle;  //ensure we snap out of any protocol
            txWindowTimerStart();
            LEDblink(); bSendData=1;
#if NUM_READINGS == 1
            if(getFlag(FLAG_LITE))
            {
                sensor_get_packet_lite(&currentReadingsLite,1);
            }
            else
            {
                sensor_get_packet_full(&currentReadings,1);
            }
#endif
            updateCRC();
        }
        
        if (dummy=='>')
        {
            if (boardSettings.slotMultiplier < MULT_MAX)
            {
                boardSettings.slotMultiplier+=1;
                txWindowTimerSetup();       //in case our constellationID has changed
                LEDblink();
            }
        }
        
        if (dummy=='<')
        {
            if (boardSettings.slotMultiplier > MULT_MIN)
            {
                boardSettings.slotMultiplier-=1;
                txWindowTimerSetup();       //in case our constellationID has changed
                LEDblink();
            }
        }
        
        if (dummy=='.')             //Karl: Do not respond if we are number 0
        {                           // usually we are granted 500uS to do grab sample and do maths
            //system_swon();
            protocolFSM=PROTOCOL_Idle; //ensure we snap out of any protocol
            loadSettingsFromEEPROM();
            deferredFullDump=0;     //only a short response to fit in TX window
            txWindowTimerSetup();       //in case our constellationID has changed
            txWindowTimerStart();  
            LEDblink(); bSendData=0;
        }
        
        if (dummy==' ')
        {
            protocolFSM=PROTOCOL_Idle;
            if (boardSettings.constellationID==1)
            {
                doPacing=0;
            }
        }
        
        if (dummy=='*'&& getFlag(FLAG_MUTE))        //Karl: if we're in silent mode, report back on "*"
        {                           //  to do grab sample and do maths
            protocolFSM=PROTOCOL_Idle; //ensure we snap out of any protocol
            loadSettingsFromEEPROM();
            deferredFullDump=0;     //only a short response to fit in TX window
            txWindowTimerSetup();       //in case our constellationID has changed
            txWindowTimerStart();  
            LEDblink(); bSendData=0;
        }
        
        if (dummy=='(')
        {
            int lite = getFlag(FLAG_LITE);
            if (lite)
            {
                clearFlag(FLAG_LITE);
            }
            else
            {
                setFlag(FLAG_LITE);
            }
            WriteEEPROM(16,boardSettings.asUInts[16]);            //update eeprom
            LEDblink();
        }
#if SENSOR == SENSOR_IMU
        if (dummy=='%')
        {
            LEDblink();
            BMI160_setAccelOffsetEnabled(1);
            BMI160_setGyroOffsetEnabled(1);
            BMI160_autoCalibrateAll(AXIS_Z);
            msleep(250);
            boardSettings.accX = BMI160_getXAccelOffset();
            boardSettings.accY = BMI160_getYAccelOffset();
            boardSettings.accZ = BMI160_getZAccelOffset();
            boardSettings.gyrX = BMI160_getXGyroOffset();
            boardSettings.gyrY = BMI160_getYGyroOffset();
            boardSettings.gyrZ = BMI160_getZGyroOffset();
            WriteEEPROM(2,boardSettings.asUInts[2]);
            WriteEEPROM(3,boardSettings.asUInts[3]);
            WriteEEPROM(5,boardSettings.asUInts[5]);
            WriteEEPROM(6,boardSettings.asUInts[6]);
            WriteEEPROM(7,boardSettings.asUInts[7]);
            LEDblink();
        }
        if (dummy=='=')
        {            
            BMI160_setOffsets(&boardSettings);
            LEDblink();
        }
#endif
        
        //immediate RS485 responses come here
        doProtocolFSM(dummy);
        
	}

	if (fifoHead!=fifoTail)        //something to send?
	{
		UTXEN |= 1;                 //assert or re-assert bus

		if (!U1STAbits.UTXBF)         //if done with previous, do next
		{
			U1TXREG=FIFO[fifoTail];  fifoTail++; fifoTail&=FIFO_MASK;
		}
	} else
	if (UTXEN)          //we still sending. only undo when TRMT is set
	{
		if (U1STAbits.TRMT) { UTXEN=0; }    //de-assert bus
	}
    
    if (candidateUID)
    {
        //test to see if the pin has been grounded
        if (!_RA1)
        {
            boardSettings.uniqueID = candidateUID;  //save
            WriteEEPROM(2,candidateUID);            //update eeprom
            
            uTX('!');                               //respond
            uTX(nibbleToASCII(candidateUID>>12)); uTX(nibbleToASCII(candidateUID>>8));
            uTX(nibbleToASCII(candidateUID>>4)); uTX(nibbleToASCII(candidateUID));
            candidateUID=0;
            CNPU1&=~0x8;
        }
    }
    

	if (U1STA&0x6) U1STA&=0xF9; //clear errors...
}

/** Called in the main loop, if our time to send, then queue the bytes
 * 
 * \details Function checks for the TX offset timer, if set then queue the data onto the bus
 * This will result in shifting data out as soon as the queueing is complete
 */
void accSend(void)
{
    if (txWindowTimerIF)      //if our window in time to send measurements
    {
        txWindowTimerIF=0;
        txWindowTimerStop();
        if (bSendData)
        {
            queue_sensor_as_base_64();       //Current comms protocol as of uWear 1.0
            //queue_sensor_as_ASCII_HEX();   //Alternative comms as used with SWear up to rev 1.4
        } else
        {
            queueEEPROM();      //send the EEPROM dump at the right time - a rollcall result
        }

    }
}

/** Quick UART RX interrupt 
 */
void __attribute__((__interrupt__, auto_psv)) _U1RXInterrupt(void)
{
	rxFIFO[rxHead]=U1RXREG; 
    rxHead++; rxHead&=rxFIFO_MASK;
    _U1RXIF=0;
}





// FUSES
#pragma config BWRP = OFF    // Boot Segment Write-Protect bit->Boot Segment may be written
#pragma config BSS = OFF    // Boot Segment Protect Control bit->No Boot Segment
#pragma config GWRP = OFF    // General Segment Write-Protect bit->General Segment may be written

// FOSCSEL
#pragma config FNOSC = FRCPLL    // Oscillator Source Selection->Fast RC Oscillator with divide-by-N with PLL module (FRCPLL) 
#pragma config IESO = ON    // Two-speed Oscillator Start-up Enable bit->Start up device with FRC, then switch to user-selected oscillator source

// FOSC
#pragma config POSCMOD = NONE
#pragma config OSCIOFNC = ON
#pragma config SOSCSEL = SOSCLP    // SOSC low power
#pragma config FCKSM = CSECME    // Clock Switching Mode bits->Both Clock switching and Fail-safe Clock Monitor are disabled

// FWDT
#pragma config WDTPS = PS32768    // Watchdog Timer Postscaler bits->1:32768
#pragma config FWPSA = PR128    // Watchdog Timer Prescaler bit->1:128
#pragma config FWDTEN = OFF    // Watchdog Timer Enable bits->WDT and SWDTEN disabled
#pragma config WINDIS = OFF    // Watchdog Timer Window Enable bit->Watchdog Timer in Non-Window mode
#pragma config DSBOREN = OFF
#pragma config DSWDTEN = OFF


// FPOR
#pragma config BOREN = BOR0    // Brown Out Enable bit->Brown Out Disabled
#pragma config PWRTEN = ON      // Power Up Timer enabled (?)

#pragma config MCLRE = OFF      // Use as RA5, no external pullup is necessary then


// FICD
#pragma config ICS = PGx2      //Use PGC/PGD 2

#pragma config RTCOSC = LPRC