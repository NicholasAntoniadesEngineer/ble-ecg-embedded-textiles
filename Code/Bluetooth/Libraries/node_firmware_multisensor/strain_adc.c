#include "strain_adc.h"


void adc_init()
{
    AD1CON1= 0x01E0;       //Data output format is signed integer (ssss sssd dddd dddd) 
                           //SSRC= 111 (Internal counter ends sampling and starts conversion(auto-conversion))
    
     AD1CON2 = 0x040C;     //Voltage Reference VR+= VDD, VR-= VSS
                           //Scan inputs selected by the AD1CSSL register as the MUX A input
                           // Set AD1IF after every 3 samples    
    AD1CON3= 0x0100;       // Configure sample time = 1Tad,  A/D conversion clock as Tcy
    AD1CHS= 0x0;          // Negative input pin is VR- = Vss,
                          //Interrupts at the completion of conversion for each sample/convert sequence
                          // Always uses MUX A input multiplexer settings
    
    //AD1CSSL= 0x1C00;      //AN10, AN11 and AN12 are scanned  
    AD1CSSL= 0x1400;      //AN10 and AN12 are scanned 
    AD1CON1bits.ADON = 1; // Turn on A/D
   
}

// There are currently only two SGs instead of the expected three SG.

void Strain_getPacket(Strain_DATA_PACKET* readings)
{
    int ADCValue1, ADCValue2,ADCValue3;
    int *ADC16Ptr1, *ADC16Ptr2;
    
    ADC16Ptr1 = &ADC1BUF0; // initialise ADC1BUF0 pointer
    ADC16Ptr2 = &ADC1BUF1; // initialise ADC1BUF1 pointer
    //ADC16Ptr3 = &ADC1BUF2; // initialise ADC1BUF2 pointer
    
    
    IFS0bits.AD1IF = 0; // clear ADC interrupt flag
    AD1CON1bits.ASAM = 1; // auto start sampling for 1Tad
    // then go to conversion
    while (!IFS0bits.AD1IF){}; // conversion done?
    AD1CON1bits.ASAM = 0; // yes then stop sample/convert
    
    ADCValue1 =*ADC16Ptr1;
    ADCValue2 =*ADC16Ptr2;
    ADCValue3 =0;
     
    readings->sensor.SG1= ADCValue1;
    readings->sensor.SG2= ADCValue2;
    readings->sensor.SG3= ADCValue3;
    
  
}

