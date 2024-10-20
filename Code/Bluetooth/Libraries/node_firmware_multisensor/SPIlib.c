#include "board_comms.h"
#include "SPIlib.h"

#define FCY 32000000
#include <libpic30.h>

/* Initialise SPI1 for BMI160
 *
 * Enable master mode for SPI1, CKE=1
 * Fcy = 16MHz  BMI160 fSPI max = 10MHz
 */
void SPI_init(void)
{
    /*
    //SPI for IMU communications
    SENSOR_CS=1;               //idle high
    //SPI1CON1=0x0123;    //MstEN, CKE, Sec=8, Pri1
    SPI1CON1=0x013b;    //MstEN, CKE, Sec=2, Pri1
    SPI1STAT=0x8000;    //EN, 
    */
            
    //SPI for ADS1118
    
    SENSOR_CS=0;               //idle low
    SPI1CON1=0x063B;           //Mode16= 1, SMP= 1,  CKE= 0, CKP=0, MSTEN= 1,  Sec=2:1, Pri=1:1
    SPI1CON2=  0x0000;         //SPIBEN= 1
    SPI1STAT=0x8000;           //EN, Interrupt when the SPI1 receive buffer is full (SPIRBF bit set)
    
    SENSOR_CS=1;               //idle low
}

/* Issue a SPI transaction.  Assumes SPI port has already been enabled.
 *
 * Transmits <txlen> bytes from <txdata>, throwing away the corresponding
 * received data, then transmits <rxlen> dummy bytes, saving the received data
 * in <rxdata>.
 * If SPI_READBACK_ALL is set in <rxlen>, the received data during transmission
 * is recorded in rxdata buffer and it assumes that the real <rxlen> is equal
 * to <txlen>.
 *
 * @param txdata  buffer to transmit
 * @param txlen  number of bytes in txdata.
 * @param rxdata  receive buffer.
 * @param rxlen  number of bytes in rxdata or SPI_READBACK_ALL.
 */
int SPI_transaction(const uint16_t *txdata, int txlen,
                    uint16_t *rxdata, int rxlen)
{
    unsigned int i,d;
    
    SENSOR_CS=0; 
    __delay_us(1);
    
    if (SPI_READBACK_ALL==rxlen)
    {
       for (i=0; i<txlen; i++) 
       {
           SPI1BUF=*txdata++;
           while(!_SPIRBF);
           *rxdata++=SPI1BUF;           
       }        
    } else
    {
        for (i=0; i<txlen; i++)
        {
            SPI1BUF=*txdata++;
            while(!_SPIRBF);
            d=SPI1BUF;
        }
        for (i=0; i<rxlen; i++)
        {
            SPI1BUF=0x00;
            while(!_SPIRBF);
            *rxdata++=SPI1BUF;
        }
    }
    __delay_us(1);
    SENSOR_CS=1;      
    return EC_SUCCESS;
}

uint8_t SPI_reg_read (uint8_t reg)
{
    uint8_t r;
    SENSOR_CS=0; 
        SPI1BUF=0x80 | (reg&0x7f); while(!_SPIRBF); r=SPI1BUF; //cmd MSb set
        SPI1BUF=0x00; while(!_SPIRBF); r=SPI1BUF; //byteBack
    SENSOR_CS=1;
    return r;
}

int SPI_reg_write(uint8_t reg, uint8_t data)
{
    unsigned int r;
    SENSOR_CS=0; 
        SPI1BUF=(reg&0x7f); while(!_SPIRBF); r=SPI1BUF; //cmd MSb clear
        SPI1BUF=(data&0xff); while(!_SPIRBF); r=SPI1BUF; //byteBackDUMMY
    SENSOR_CS=1;
}

/*
int SPI_serial_buffer_transfer(uint8_t* buffer, uint8_t txcnt, uint8_t rxcnt)
{
    uint8_t cmd = 0x80 | buffer[0];
    return SPI_transaction(&cmd, 1, buffer, rxcnt);
}
 */ 