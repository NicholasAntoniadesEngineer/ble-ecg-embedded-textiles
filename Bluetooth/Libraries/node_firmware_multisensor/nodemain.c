#include <xc.h>
#include "sensor.h"
#include "funcs.h"
#include "typedefs.h"
#include <p24F16KA101.h>
#include "SPIlib.h"


int ticks = 0;
//uint8_t response = 0xFF;
int main()
{
	setupPIC();
    //LEDblink();
    sensor_init();
    
    uint16_t config1= 0x446A;
    uint16_t config2= 0x546A;
    uint16_t config3= 0x646A;
    uint16_t ADCValue1, ADCValue2, ADCValue3, ADC1, ADC2, ADC3;
    int success1, success2, success3;
    
    
    success1= SPI_transaction(config1, 1, ADCValue1,1);
    success2= SPI_transaction(config2, 1, ADCValue2,1);
    success3= SPI_transaction(config3, 1, ADCValue3,1);
    

    
    ADC1 = ADCValue1;
    ADC2= ADCValue2;
    ADC3= ADCValue3;
   
    
    
    /*
    if (boardSettings.constellationID == 1)
    {
        unsigned int i,j;
        j=10; while(j--) for (i=25000; i>0; i--) asm("nop");
    }
    
    if (!sensor_test_connection())
    {
        int i,j;
        j=20;
        while(j--)
        { i=0xffff; while(i--) {asm("nop"); asm("nop"); asm("nop"); }; LEDblink(); }
        _LATB0=0;
        while(1);
    }
    
    */
  
	while(1){
		/*
        ProcessIO();
		accSend();
        
#if NUM_READINGS == 1

        if ((boardSettings.constellationID == 1) && !getFlag(FLAG_MUTE))
        {
            if (doPacing)
                if (_T1IF)
                {
                    _T1IF=0;
                    reqFrame();
                }
        }
#else
        if (!getFlag(FLAG_MUTE) && _T1IF)
        {
            _T1IF=0;
            doContinuousRead(ticks++);
            if (ticks == NUM_READINGS)
            {
                ticks = 0;
                /*if ((boardSettings.constellationID == 1) && doPacing)
                {
                    reqFrame();
                }
            }
        }
#endif
      */
	}

	return 0; //should never get here
}
