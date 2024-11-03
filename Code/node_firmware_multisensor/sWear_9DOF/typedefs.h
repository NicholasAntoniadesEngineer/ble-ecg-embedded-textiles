/* 
 * File:   typedefs.h
 * Author: B Janko
 *
 * Libraries that drive BMI/BMM chips require cross compiler type defs
 * Microchip compilers don't by default provide these types
 *
 * Created on 09 May 2019, 07:59
 */

#ifndef TYPEDEFS_H
#define	TYPEDEFS_H

#define bool char
#define uint8_t unsigned char
#define int8_t signed char
#define uint16_t unsigned int
#define int16_t signed int

#define q11_t int16_t
#define q12_t int16_t
#define q14_t int16_t
#define q15_t int16_t

#define eeprom_t uint16_t __attribute__ ((space(eedata)))

#endif	/* TYPEDEFS_H */

