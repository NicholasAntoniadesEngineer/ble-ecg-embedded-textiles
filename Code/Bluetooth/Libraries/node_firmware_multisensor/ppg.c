#include "ppg.h"

/** \file max30102.cpp ******************************************************
*
* Project: MAXREFDES117#
* Filename: max30102.cpp
* Description: This module is an embedded controller driver for the MAX30102
*
* Revision History:
*\n 1-18-2016 Rev 01.00 GL Initial release.
*\n
*
* --------------------------------------------------------------------
*
* This code follows the following naming conventions:
*
* char              ch_pmod_value
* char (array)      s_pmod_s_string[16]
* float             f_pmod_value
* int32_t           n_pmod_value
* int32_t (array)   an_pmod_value[16]
* int16_t           w_pmod_value
* int16_t (array)   aw_pmod_value[16]
* uint16_t          uw_pmod_value
* uint16_t (array)  auw_pmod_value[16]
* uint8_t           uch_pmod_value
* uint8_t (array)   auch_pmod_buffer[16]
* uint32_t          un_pmod_value
* int32_t *         pn_pmod_value
*
* ------------------------------------------------------------------------- */
/*******************************************************************************
* Copyright (C) 2016 Maxim Integrated Products, Inc., All Rights Reserved.
*
* Permission is hereby granted, free of charge, to any person obtaining a
* copy of this software and associated documentation files (the "Software"),
* to deal in the Software without restriction, including without limitation
* the rights to use, copy, modify, merge, publish, distribute, sublicense,
* and/or sell copies of the Software, and to permit persons to whom the
* Software is furnished to do so, subject to the following conditions:
*
* The above copyright notice and this permission notice shall be included
* in all copies or substantial portions of the Software.
*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
* OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
* MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
* IN NO EVENT SHALL MAXIM INTEGRATED BE LIABLE FOR ANY CLAIM, DAMAGES
* OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
* ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
* OTHER DEALINGS IN THE SOFTWARE.
*
* Except as contained in this notice, the name of Maxim Integrated
* Products, Inc. shall not be used except as stated in the Maxim Integrated
* Products, Inc. Branding Policy.
*
* The mere transfer of this software does not imply any licenses
* of trade secrets, proprietary technology, copyrights, patents,
* trademarks, maskwork rights, or any other form of intellectual
* property whatsoever. Maxim Integrated Products, Inc. retains all
* ownership rights.
*******************************************************************************
*/
//#include "max30102.h"
//#include "SoftI2CMaster.h"
//#include "algorithm.h"

#include "board_comms.h"
#include "ppg.h"
#include <xc.h>

#define VAL_PART_ID 0x15

uint8_t PPG_testConnection()
{
    uint8_t response = 0;
    response = reg_read(REG_PART_ID);
    return response==VAL_PART_ID;
}

uint8_t PPG_init()
{
  if(!reg_write(REG_INTR_ENABLE_1,0xc0)) // INTR setting
    return false;
  if(!reg_write(REG_INTR_ENABLE_2,0x00))
    return false;
  if(!reg_write(REG_FIFO_WR_PTR,0x00))  //FIFO_WR_PTR[4:0]
    return false;
  if(!reg_write(REG_OVF_COUNTER,0x00))  //OVF_COUNTER[4:0]
    return false;
  if(!reg_write(REG_FIFO_RD_PTR,0x00))  //FIFO_RD_PTR[4:0]
    return false;
  if(!reg_write(REG_FIFO_CONFIG,0x4f))  //sample avg = 4, fifo rollover=false, fifo almost full = 17
    return false;
  if(!reg_write(REG_MODE_CONFIG,0x03))   //0x02 for Red only, 0x03 for SpO2 mode 0x07 multimode LED
    return false;
  if(!reg_write(REG_SPO2_CONFIG,0x2f))  // SPO2_ADC range = 4096nA, SPO2 sample rate (100 Hz), LED pulseWidth (411uS)
    return false;
  if(!reg_write(REG_LED1_PA,0x3f))   //Choose value for ~ 7mA for LED1
    return false;
  if(!reg_write(REG_LED2_PA,0x24))   // Choose value for ~ 7mA for LED2
    return false;
  if(!reg_write(REG_PILOT_PA,0x7f))   // Choose value for ~ 25mA for Pilot LED
      return false;
  return true;
}



void PPG_getPacket(PPG_DATA_PACKET *readings, uint8_t index)
{    
    uint8_t in_buffer[12] ={REG_FIFO_DATA,0,0,0,0,0,0,0,0,0,0,0};
    uint8_t uch_temp;
    uch_temp = reg_read(REG_INTR_STATUS_1);
    uch_temp = reg_read(REG_INTR_STATUS_2);
    serial_buffer_transfer(in_buffer, 1,12);
    
    readings->sensor.rled[0].READINGS.ppg_h = in_buffer[0];
    readings->sensor.rled[0].READINGS.ppg_m = in_buffer[1];
    readings->sensor.rled[0].READINGS.ppg_l = in_buffer[2];    
    readings->sensor.irled[0].READINGS.ppg_h = in_buffer[3];
    readings->sensor.irled[0].READINGS.ppg_m = in_buffer[4];
    readings->sensor.irled[0].READINGS.ppg_l = in_buffer[5];
    readings->sensor.rled[1].READINGS.ppg_h = in_buffer[6];
    readings->sensor.rled[1].READINGS.ppg_m = in_buffer[7];
    readings->sensor.rled[1].READINGS.ppg_l = in_buffer[8];    
    readings->sensor.irled[1].READINGS.ppg_h = in_buffer[9];
    readings->sensor.irled[1].READINGS.ppg_m = in_buffer[10];
    readings->sensor.irled[1].READINGS.ppg_l = in_buffer[11];
}

#ifdef PPG
bool maxim_max30102_reset()
/**
* \brief        Reset the MAX30102
* \par          Details
*               This function resets the MAX30102
*
* \param        None
*
* \retval       true on success
*/
{
    if(!maxim_max30102_write_reg(REG_MODE_CONFIG,0x40))
        return false;
    else
        return true;    
}
#endif
