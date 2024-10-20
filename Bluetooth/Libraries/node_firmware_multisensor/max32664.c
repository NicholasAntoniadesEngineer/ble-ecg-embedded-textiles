#include "max32664.h"

#define FCY 32000000
#include <libpic30.h>

volatile I2C1_MESSAGE_STATUS I2C_Wflag = I2C1_MESSAGE_PENDING;
volatile I2C1_MESSAGE_STATUS I2C_Rflag = I2C1_MESSAGE_PENDING;

void max32664_init()
{
    application_mode();
    set_dev_mode();
    __delay_ms(400);
}

void application_mode()
{
//Enter application_mode
    
  TRISAbits.TRISA4= 0;  // Reset pin
  TRISBbits.TRISB14= 0;  // MFIO pin
      
  PORTAbits.RA4 = 0; //Reset Low
  PORTBbits.RB14 = 0; // MFIO Low
    
  __delay_ms(5);
 
  PORTAbits.RA4 = 1; //Reset High
  __delay_ms(750);
  
}


//Set device mode to application mode
void set_dev_mode()
{
   
    uint8_t command[3] = {DEVICE_MODE_1, DEVICE_MODE_2, WRITE_APPLICATION_MODE};
     
     I2C1_MasterWrite( command, 3, I2C_ADDRESS_A, &I2C_Wflag);
     
    while (I2C_Wflag != I2C1_MESSAGE_COMPLETE);
    
}

// Get device mode 
void get_dev_mode()
{
    
    uint8_t command[2] = {READ_MODE_1, READ_MODE_2};
    uint8_t data[2];
    
    I2C1_MasterWrite( command, 2, I2C_ADDRESS_A, &I2C_Wflag);
    while (I2C_Wflag != I2C1_MESSAGE_COMPLETE);

    
    I2C1_MasterRead(  data,2, I2C_ADDRESS_A, &I2C_Rflag);
    while (I2C_Rflag != I2C1_MESSAGE_COMPLETE);; 
}


// Check the sensor ID = 0x01 to test sensor connection
int MAX32664_testConnection()
{
    uint8_t command[2] = {SENSOR_TYPE_1, SENSOR_TYPE_2};
    uint8_t data[2];
   
    I2C1_MasterWrite( command, 2, I2C_ADDRESS_A, &I2C_Wflag);
    while (I2C_Wflag != I2C1_MESSAGE_COMPLETE);

    
    I2C1_MasterRead(  data,2, I2C_ADDRESS_A, &I2C_Rflag);
   while (I2C_Rflag != I2C1_MESSAGE_COMPLETE);
   
    if (data[1] == MAX32664_ID)
    {
        return 1;
    }
    else
    {
        return 0;            
    }
}


// Raw Data mode  

void PPG_raw_data()
{    
    //Set the output mode to Sensor Only.
    
    uint8_t command1[3] = {OUTPUT_MODE_1,OUTPUT_MODE_2,SENSOR_DATA};
    uint8_t data1[1];
  
    I2C1_MasterWrite( command1,3, I2C_ADDRESS_A, &I2C_Wflag);
    while (I2C_Wflag != I2C1_MESSAGE_COMPLETE);
    
    
    I2C1_MasterRead(  data1,1, I2C_ADDRESS_A, &I2C_Rflag);
    while (I2C_Rflag != I2C1_MESSAGE_COMPLETE);
    
    //Set the sensor hub interrupt threshold.
    
    uint8_t command2[3] = {FIFO_THRESOLD_1,FIFO_THRESOLD_2,0x01};
    uint8_t data2[1];
  
    
    I2C1_MasterWrite( command2, 3, I2C_ADDRESS_A, &I2C_Wflag);
    while (I2C_Wflag != I2C1_MESSAGE_COMPLETE);
    
    I2C1_MasterRead(  data2,1, I2C_ADDRESS_A, &I2C_Rflag);
    while (I2C_Rflag != I2C1_MESSAGE_COMPLETE);
    
    //Disable the accelerometer 
    
    uint8_t command3[4] = {MODE_ACCELEROMETER_1,MODE_ACCELEROMETER_2,DISABLE_EXT_ACCELEROMETER_1, DISABLE_EXT_ACCELEROMETER_2};
    uint8_t data3[1];
  
    
    I2C1_MasterWrite( command3, 4, I2C_ADDRESS_A, &I2C_Wflag);
    while (I2C_Wflag != I2C1_MESSAGE_COMPLETE);
    
    __delay_ms(15);
    
    I2C1_MasterRead(  data3,1, I2C_ADDRESS_A, &I2C_Rflag);
    while (I2C_Rflag != I2C1_MESSAGE_COMPLETE);
  
    
    //Enable AFE
   
    
    uint8_t command4[3] = {MODE_MAX86141_1,MODE_MAX86141_2,ENABLE_MAX86141};
    uint8_t data4[1];
  
    
    I2C1_MasterWrite( command4, 3, I2C_ADDRESS_A, &I2C_Wflag);
    while (I2C_Wflag != I2C1_MESSAGE_COMPLETE);
    
    __delay_ms(150);
    
    I2C1_MasterRead(  data4,1, I2C_ADDRESS_A, &I2C_Rflag);
    while (I2C_Rflag != I2C1_MESSAGE_COMPLETE);
  
  
    //Delay before changing the sensor's registers  
    __delay_ms(50);
    
 
    FIFO_CONFIG();
   
    //Set the sample rate  to 50Hz with 1 sampling average 
 
    uint8_t command5[4] = {WRITE_MAX86141_1, WRITE_MAX86141_2, 0x12, 0x08};
    uint8_t data5[1];
    
    I2C1_MasterWrite( command5, 4, I2C_ADDRESS_A, &I2C_Wflag);
    while (I2C_Wflag != I2C1_MESSAGE_COMPLETE);
    
    __delay_us(50);
    
    I2C1_MasterRead(  data5,1, I2C_ADDRESS_A, &I2C_Rflag);
    while (I2C_Rflag != I2C1_MESSAGE_COMPLETE);
    
        
    //Set the MAX86141 LED1 current to half of full scale.

    uint8_t command6[4] = {WRITE_MAX86141_1, WRITE_MAX86141_2, 0x23, 0x7F};
    uint8_t data6[1];
  
    I2C1_MasterWrite( command6, 4, I2C_ADDRESS_A, &I2C_Wflag);
    while (I2C_Wflag != I2C1_MESSAGE_COMPLETE);
    
    __delay_us(50);
    
    I2C1_MasterRead(  data6,1, I2C_ADDRESS_A, &I2C_Rflag);
    while (I2C_Rflag != I2C1_MESSAGE_COMPLETE);
    
    
    //Set the MAX86141 LED2 current to half of full scale.

    uint8_t command7[4] = {WRITE_MAX86141_1, WRITE_MAX86141_2, 0x24, 0x7F};
    uint8_t data7[1];
  
    
    I2C1_MasterWrite( command7, 4, I2C_ADDRESS_A, &I2C_Wflag);
    while (I2C_Wflag != I2C1_MESSAGE_COMPLETE);
    
   __delay_us(50);
   
    I2C1_MasterRead(  data7,1, I2C_ADDRESS_A, &I2C_Rflag);
    while (I2C_Rflag != I2C1_MESSAGE_COMPLETE);
        
       
    //Set the MAX86141 LED3 current to half of full scale..
    
    uint8_t command8[4] = {WRITE_MAX86141_1, WRITE_MAX86141_2, 0x25, 0x7F};
    uint8_t data8[1];
  
    
    I2C1_MasterWrite( command8, 4, I2C_ADDRESS_A, &I2C_Wflag);
    while (I2C_Wflag != I2C1_MESSAGE_COMPLETE);
    
    __delay_us(50);
    
    I2C1_MasterRead(  data8,1, I2C_ADDRESS_A, &I2C_Rflag);
    while (I2C_Rflag != I2C1_MESSAGE_COMPLETE); 
    system_shdn();
}

//Changed FIFO config so that The FIFO stops on full.
void FIFO_CONFIG()
{
   
    uint8_t command8[4] = {0x40, 0x00, 0x2A, 0x15};
    uint8_t data8[1];
  
    
    I2C1_MasterWrite( command8, 4,I2C_ADDRESS_A, &I2C_Wflag);
    while (I2C_Wflag != I2C1_MESSAGE_COMPLETE);
    
    __delay_us(50);
    
    I2C1_MasterRead(  data8,1, I2C_ADDRESS_A, &I2C_Rflag);
   

    while (I2C_Rflag != I2C1_MESSAGE_COMPLETE); 
}

//Power-save mode. The registers retain their values but the FIFO is not being filled.

void system_shdn()
{
   
    uint8_t command8[4] = {0x40, 0x00, 0x0D, 0x06};
    uint8_t data8[1];
  
    
    I2C1_MasterWrite( command8, 4,I2C_ADDRESS_A, &I2C_Wflag);
    while (I2C_Wflag != I2C1_MESSAGE_COMPLETE);
    
    __delay_us(50);
    
    I2C1_MasterRead(  data8,1, I2C_ADDRESS_A, &I2C_Rflag);
   

    while (I2C_Rflag != I2C1_MESSAGE_COMPLETE); 
}

//Normal operation 

void system_swon()
{
   
    uint8_t command8[4] = {0x40, 0x00, 0x0D, 0x04};
    uint8_t data8[1];
  
    
    I2C1_MasterWrite( command8, 4,I2C_ADDRESS_A, &I2C_Wflag);
    while (I2C_Wflag != I2C1_MESSAGE_COMPLETE);
    
    __delay_us(50);
    
    I2C1_MasterRead(  data8,1, I2C_ADDRESS_A, &I2C_Rflag);
   

    while (I2C_Rflag != I2C1_MESSAGE_COMPLETE); 
}

void MAX32664_getPacket(PPG1_DATA_PACKET *readings)
{
    
    uint8_t command1[2] = {SENSOR_STATUS_1,SENSOR_STATUS_2};
    uint8_t data1[2];
  
    
    I2C1_MasterWrite( command1, 2, I2C_ADDRESS_A, &I2C_Wflag);
    while (I2C_Wflag != I2C1_MESSAGE_COMPLETE);

    
    I2C1_MasterRead(  data1,2, I2C_ADDRESS_A, &I2C_Rflag); //The value we want is data1= 0x00 0x08
    while (I2C_Rflag != I2C1_MESSAGE_COMPLETE);
    
    
    //Read number of samples
    
    uint8_t ns;
    
    uint8_t command2[2] = {NUMBER_OF_SAMPLES_1,NUMBER_OF_SAMPLES_2};
    uint8_t data2[2];
   
    I2C1_MasterWrite( command2, 2, I2C_ADDRESS_A, &I2C_Wflag);
    while (I2C_Wflag != I2C1_MESSAGE_COMPLETE);
 
    
    I2C1_MasterRead(  data2,2, I2C_ADDRESS_A, &I2C_Rflag);
    while (I2C_Rflag != I2C1_MESSAGE_COMPLETE);
    
    ns= data2[1];
    
    //Read fifo
    
    uint8_t command3[2] = {FIFO_DATA_1,FIFO_DATA_2};
    uint8_t sample= (18*ns) + 1;
    uint8_t data3[sample];
    
    I2C1_MasterWrite( command3, 2, I2C_ADDRESS_A, &I2C_Wflag);
    while (I2C_Wflag != I2C1_MESSAGE_COMPLETE);
    
    
    I2C1_MasterRead(  data3,sample, I2C_ADDRESS_A, &I2C_Rflag);
    while (I2C_Rflag != I2C1_MESSAGE_COMPLETE);
    
    uint8_t status;
    status= data3[0];
 
    readings->sensor.GLED.READINGS.PPG_H = data3[1];
    readings->sensor.GLED.READINGS.PPG_M = data3[2];
    readings->sensor.GLED.READINGS.PPG_L = data3[3]; 
    readings->sensor.GLED2.READINGS.PPG_H = data3[4];
    readings->sensor.GLED2.READINGS.PPG_M = data3[5];
    readings->sensor.GLED2.READINGS.PPG_L = data3[6];
    readings->sensor.IRLED.READINGS.PPG_H = data3[7];
    readings->sensor.IRLED.READINGS.PPG_M = data3[8];
    readings->sensor.IRLED.READINGS.PPG_L = data3[9]; 
    readings->sensor.IRLED2.READINGS.PPG_H = data3[10];
    readings->sensor.IRLED2.READINGS.PPG_M = data3[11];
    readings->sensor.IRLED2.READINGS.PPG_L = data3[12];
    readings->sensor.RLED.READINGS.PPG_H = data3[13];
    readings->sensor.RLED.READINGS.PPG_M = data3[14];
    readings->sensor.RLED.READINGS.PPG_L = data3[15];
    readings->sensor.RLED2.READINGS.PPG_H = data3[16];
    readings->sensor.RLED2.READINGS.PPG_M = data3[17];
    readings->sensor.RLED2.READINGS.PPG_L = data3[18];
    
}



