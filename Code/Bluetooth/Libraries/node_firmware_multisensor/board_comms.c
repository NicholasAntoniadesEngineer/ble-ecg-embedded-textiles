#include "board_comms.h"



#define I2C_FAIL_CODE 0x00;
#define I2C_SUCCESS_CODE 0x01;

#if (SPI_NOT_I2C == 1)

    void comms_init()
    {
        SPI_init();
    }

    uint8_t reg_read(uint8_t reg)
    {        
        return SPI_reg_read(reg);
    }

    int reg_write(uint8_t reg, uint8_t data)
    {
        SPI_reg_write(reg,data);
        return 1;
    }

    int serial_buffer_transfer(uint8_t* buffer, uint8_t txcnt, uint8_t rxcnt)
    {
        return SPI_serial_buffer_transfer(buffer, txcnt, rxcnt);
    }

#else

    void comms_init()
    {
        I2C1_Initialize();
    }

    uint8_t reg_read(uint8_t reg)
    {        
        volatile I2C1_MESSAGE_STATUS I2C_Wflag = I2C1_MESSAGE_PENDING;
        volatile I2C1_MESSAGE_STATUS I2C_Rflag = I2C1_MESSAGE_PENDING;

        uint8_t buffer;
        I2C1_MasterWrite(&reg,1, I2C_ADDRESS_A, &I2C_Wflag);
        if (I2C_Wflag == I2C1_MESSAGE_FAIL)
        {
            return I2C_FAIL_CODE;
        }
        while (I2C_Wflag != I2C1_MESSAGE_COMPLETE);
        I2C1_MasterRead(&buffer,1, I2C_ADDRESS_A, &I2C_Rflag);
        if (I2C_Rflag == I2C1_MESSAGE_FAIL)
        {
            return I2C_FAIL_CODE;
        }
        while (I2C_Rflag != I2C1_MESSAGE_COMPLETE);
        return buffer;
    }

    int reg_write(uint8_t reg, uint8_t data)
    {
        volatile I2C1_MESSAGE_STATUS I2C_Wflag = I2C1_MESSAGE_PENDING;
    
        uint8_t buffer[2] = {reg,data};
        I2C1_MasterWrite(&buffer,2, I2C_ADDRESS_A, &I2C_Wflag);
        if (I2C_Wflag == I2C1_MESSAGE_FAIL)
        {
            return I2C_FAIL_CODE;
        }
        while (I2C_Wflag != I2C1_MESSAGE_COMPLETE);
        return I2C_SUCCESS_CODE;
    }

    int serial_buffer_transfer(uint8_t* buffer, uint8_t txcnt, uint8_t rxcnt)
    {
        
        volatile I2C1_MESSAGE_STATUS I2C_Wflag = I2C1_MESSAGE_PENDING;
        volatile I2C1_MESSAGE_STATUS I2C_Rflag = I2C1_MESSAGE_PENDING;
        if (txcnt>0)
        {
            I2C1_MasterWrite(buffer,txcnt, I2C_ADDRESS_A, &I2C_Wflag);
            if (I2C_Wflag == I2C1_MESSAGE_FAIL)
            {
                return I2C_FAIL_CODE;
            }
            while (I2C_Wflag != I2C1_MESSAGE_COMPLETE);
        }
        if (rxcnt>0)
        {
            usleep(60);
            I2C1_MasterRead(buffer,rxcnt, I2C_ADDRESS_A, &I2C_Rflag);
            if (I2C_Rflag == I2C1_MESSAGE_FAIL)
            {
                return I2C_FAIL_CODE;
            }
            while (I2C_Rflag != I2C1_MESSAGE_COMPLETE);
        }
        return I2C_SUCCESS_CODE;
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