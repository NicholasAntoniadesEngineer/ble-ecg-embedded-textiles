#include "ads1118.h"
#include "SPIlib.h"

#define FCY 32000000
#include <libpic30.h>

//ADC init
void ADS1118_init()
{
    __delay_us(50);
  
}

void ADS1118_getpacket(ADC_DATA_PACKET* readings)
{
    uint8_t config1[]= {0x44, 0x6A};
    uint8_t config2[]= {0x54, 0x6A};
    uint8_t config3[]= {0x64, 0x6A};
    uint8_t ADCValue1[2], ADCValue2[2], ADCValue3[2];
    int success1, success2, success3;
    
    /*
    success1= SPI_transaction(config1, 2, ADCValue1,2);
    success2= SPI_transaction(config2, 2, ADCValue2,2);
    success3= SPI_transaction(config3, 2, ADCValue3,2);
    

    
    readings->sensor.ADC1.READINGS.ADC_H = ADCValue1[0];
    readings->sensor.ADC1.READINGS.ADC_L = ADCValue1[1];
    readings->sensor.ADC2.READINGS.ADC_H = ADCValue2[0];
    readings->sensor.ADC2.READINGS.ADC_L = ADCValue2[1];
    readings->sensor.ADC3.READINGS.ADC_H = ADCValue3[0];
    readings->sensor.ADC3.READINGS.ADC_L = ADCValue3[1];
    */
}

