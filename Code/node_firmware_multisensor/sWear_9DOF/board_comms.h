/* 
 * File:   board_comms.h
 * Author: user
 *
 * Created on 28 September 2018, 10:40
 */

#ifndef board_comms_H
#define	board_comms_H

#include "funcs.h"
#include "typedefs.h"
#include <xc.h>
#include "p24F16KA101.h"
#include <libpic30.h>

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
int spi_transaction(const uint8_t *txdata, int txlen, uint8_t *rxdata, int rxlen);

void comms_init(void);

uint8_t reg_read_bits(uint8_t reg, unsigned pos, unsigned len);
void reg_write_bits(uint8_t reg, uint8_t data, unsigned pos, unsigned len);

uint8_t reg_read(uint8_t reg);
void reg_write(uint8_t reg, uint8_t data);
int serial_buffer_transfer(uint8_t* buffer, uint8_t txcnt, uint8_t rxcnt);

#if (SPI_NOT_I2C == 1)
#include "SPIlib.h"
#else
#include "I2Clib.h"
#endif

#endif	/* board_comms_H */

