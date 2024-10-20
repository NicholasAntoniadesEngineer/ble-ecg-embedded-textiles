#include "board_comms.h"

#define SPI_NOT_I2C 0
#define I2C_ADDRESS_A 0x40

#if SPI_NOT_I2C == 0
void comms_init()
{
    I2C_SWini();
    I2C_HWini();
}

uint8_t reg_read(uint8_t reg)
{
    uint8_t buffer;
    I2C1_M_Read(I2C_ADDRESS_A, reg, 1, &buffer);
    return buffer;
}

void reg_write(uint8_t reg, uint8_t data)
{
    I2C1_M_Write(I2C_ADDRESS_A,reg,1,&data);
}

int serial_buffer_transfer(uint8_t* buffer, uint8_t txcnt, uint8_t rxcnt)
{
    uint8_t reg = 0x3F | buffer[0];
    uint8_t result;
    result = I2C1_M_Read(I2C_ADDRESS_A, reg, rxcnt, buffer);
    return result;
}
#else
void comms_init()
{
    SPI_init();
}

uint8_t reg_read(uint8_t reg)
{
    SPI_reg_read(reg);
}

void reg_write(uint8_t reg, uint8_t data)
{
    SPI_reg_write(reg,data);
}

int serial_buffer_transfer(uint8_t* buffer, uint8_t txcnt, uint8_t rxcnt)
{
    SPI_serial_buffer_transfer(buffer, txcnt, rxcnt);
}

#endif

void reg_write_bits(uint8_t reg, uint8_t data, unsigned pos, unsigned len)
{
    uint8_t b = reg_read(reg);
    uint8_t mask = ((1 << len) - 1) << pos;
    data <<= pos; // shift data into correct position
    data &= mask; // zero all non-important bits in data
    b &= ~(mask); // zero all important bits in existing byte
    b |= data; // combine data with existing byte
    reg_write(reg, b);
}

uint8_t reg_read_bits(uint8_t reg, unsigned pos, unsigned len)
{
    uint8_t b = reg_read(reg);
    uint8_t mask = (1 << len) - 1;
    b >>= pos;
    b &= mask;
    return b;
}