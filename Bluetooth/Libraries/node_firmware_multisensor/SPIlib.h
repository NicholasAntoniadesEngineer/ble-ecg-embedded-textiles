/* 
 * File:   SPIlib.h
 * Author: KarlSainzMartinez
 *
 * Created on 20 May 2020, 11:26
 */

#ifndef SPILIB_H
#define	SPILIB_H

#define SPI_READBACK_ALL (-1)

#define EC_SUCCESS 0
#define SENSOR_CS _LATB15 

#include "board_comms.h"
//#include <xc.h>

//#define I2C_ADDRESS_A 0x57

#define I2C_FAIL_CODE 0x00;
#define I2C_SUCCESS_CODE 0x01;


void SPI_init(void);
int SPI_transaction(const uint16_t *txdata, int txlen,
                    uint16_t *rxdata, int rxlen);

uint8_t SPI_reg_read (uint8_t reg);

int SPI_reg_write(uint8_t reg, uint8_t data);

int SPI_serial_buffer_transfer(uint8_t* buffer, uint8_t txcnt, uint8_t rxcnt);

#endif