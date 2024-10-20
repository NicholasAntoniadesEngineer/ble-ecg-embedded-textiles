#include <xc.h>
#include "sensor.h"
#include "funcs.h"
#include "typedefs.h"
#include <p24F16KA101.h>

// This is just a test comment to see how commits work through MPLAB X part 3

int main()
{
    int ticks = 0;
	setupPIC(); 
    LEDblink();
	sensor_init();

    if (boardSettings.constellationID == 1)
    {
        unsigned int i,j;
        j=10; while(j--) for (i=25000; i>0; i--) asm("nop");
    }
    
    //If can't talk to sensor - panic
    if (!sensor_test_connection())
    {
        int i,j;
        j=20;
        while(j--)
        { i=0xffff; while(i--) {asm("nop"); asm("nop"); asm("nop"); }; LEDblink(); }
        _LATB0=0;
        while(1);
    } 
    
  
	while(1){
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
                if ((boardSettings.constellationID == 1) && doPacing)
                {
                    reqFrame();
                }
            }
        }
#endif
	}

	return 0; //should never get here
}
