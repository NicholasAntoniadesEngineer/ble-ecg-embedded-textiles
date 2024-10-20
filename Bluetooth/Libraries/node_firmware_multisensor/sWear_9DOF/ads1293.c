#include "ads1293.h"
#include "funcs.h"
#include "typedefs.h"
#include <xc.h>
#include "board_comms.h"


uint8_t ecg_buffer[10];

// Configure TMR3 to drive ~409Hz clock for AFE
void ADS1293_setupExtClockOC()
{
    OC1CON = 0;
    OC1R = 19;
    OC1RS = 19;
    OC1CON = 0x0E;
    PR3 = 38;
    _T3IE = 0;
    T3CONbits.TON = 1; 
}

int ADS1293_testConnection()
{
    int result;
    result = reg_read(ADS1293_REVID);
    if (result == REG_REVID)
    {
        return 1;
    }
    else
    {
        return 0;            
    }
}

void ADS1293_init()
{
    //connect channel 1 pos to IN2 and neg to IN1
    reg_write(ADS1293_FLEX_CH1_CN, ADS1293_P2_N1);
    //connect channel 2 pos to IN3 and neg to IN1
    reg_write(ADS1293_FLEX_CH2_CN, ADS1293_P3_N1);
    //enable common-mode detector on input pins IN1,IN2 and IN3
    reg_write(ADS1293_CMDET_EN, 0x07);
    //connect output of RLD amplifier to IN4
    reg_write(ADS1293_RLD_CN, 0x04);
    //use external clock
    reg_write(ADS1293_OSC_CN, 0x02);
    //enable clock to digital
    reg_write(ADS1293_OSC_CN, 0x06);
    //shut down channel 3
    reg_write(ADS1293_AFE_SHDN_CN, 0x24);
    reg_write(ADS1293_AFE_RES, 0x38);
    //reg_write(ADS1293_R1_RATE,0x07);
    //configure R2 decimation rate as 5 for all channels
    reg_write(ADS1293_R2_RATE,0x02);
    //configure R3 decimation rate as 6 for channels 1 and 2
    reg_write(ADS1293_R3_RATE_CH1,0x02);
    reg_write(ADS1293_R3_RATE_CH2,0x02);
    //configure DRDYB source to channel 1 ECG
    reg_write(ADS1293_DRDYB_SRC, 0x08);
    //enable channel 1 ECG and channel 2 ECG for loop read-back mode
    reg_write(ADS1293_CH_CNFG, 0x30);
    //start data conversion
    reg_write(ADS1293_CONFIG, 0x01);    
}

void ADS1293_getPacket(ECG_DATA_PACKET* current, int index)
{   
    int i;
    for (i = 0;i<ECG_NUM_READINGS;i++)
    {
        ecg_buffer[i] = 0;       
    }
    ecg_buffer[0] = ADS1293_DATA_LOOP;
    serial_buffer_transfer(ecg_buffer,1,ECG_DATA_LENGTH+1);
    current->sensor.ECG1[index].READINGS.ECG_H = ecg_buffer[0];    
    current->sensor.ECG1[index].READINGS.ECG_M = ecg_buffer[1];    
    current->sensor.ECG1[index].READINGS.ECG_L = ecg_buffer[2];    
    current->sensor.ECG2[index].READINGS.ECG_H = ecg_buffer[3];    
    current->sensor.ECG2[index].READINGS.ECG_M = ecg_buffer[4];    
    current->sensor.ECG2[index].READINGS.ECG_L = ecg_buffer[5];
}