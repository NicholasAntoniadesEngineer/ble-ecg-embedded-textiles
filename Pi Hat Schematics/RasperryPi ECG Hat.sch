EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A3 16535 11693
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Text Notes 900  4600 0    55   ~ 0
ECG
$Comp
L pspice:INDUCTOR L1
U 1 1 6180537B
P 1550 1200
F 0 "L1" H 1550 1415 50  0000 C CNN
F 1 "INDUCTOR" H 1550 1324 50  0000 C CNN
F 2 "Resistor_SMD:R_0402_1005Metric" H 1550 1200 50  0001 C CNN
F 3 "~" H 1550 1200 50  0001 C CNN
	1    1550 1200
	1    0    0    -1  
$EndComp
Wire Wire Line
	1300 1200 1200 1200
Text Notes 900  650  0    55   ~ 0
Power Management
Wire Wire Line
	3350 5750 5050 5750
Wire Wire Line
	3350 5600 4750 5600
$Comp
L power:Earth #PWR032
U 1 1 618E1B04
P 4450 5000
F 0 "#PWR032" H 4450 4750 50  0001 C CNN
F 1 "Earth" H 4450 4850 50  0001 C CNN
F 2 "" H 4450 5000 50  0001 C CNN
F 3 "~" H 4450 5000 50  0001 C CNN
	1    4450 5000
	1    0    0    -1  
$EndComp
Text GLabel 4800 5600 2    50   Input ~ 0
IN3
Wire Wire Line
	5300 5000 5250 5000
Wire Wire Line
	4900 5150 5050 5150
Connection ~ 4900 5150
Wire Wire Line
	4900 5000 4950 5000
Connection ~ 4900 5000
Wire Wire Line
	4900 5000 4900 5150
Wire Wire Line
	4850 5000 4900 5000
$Comp
L Jumper:SolderJumper_2_Open JP6
U 1 1 618D174F
P 5100 5000
F 0 "JP6" H 5100 4900 50  0000 C CNN
F 1 "Jumper" H 5100 5100 50  0000 C CNN
F 2 "Resistor_SMD:R_0402_1005Metric" H 5100 5000 50  0001 C CNN
F 3 "~" H 5100 5000 50  0001 C CNN
	1    5100 5000
	1    0    0    -1  
$EndComp
Wire Wire Line
	5050 5750 5100 5750
Connection ~ 5050 5750
Connection ~ 4750 5600
Wire Wire Line
	4750 5600 4800 5600
Wire Wire Line
	5050 5150 5050 5200
Wire Wire Line
	4750 5150 4900 5150
Wire Wire Line
	4750 5200 4750 5150
Wire Wire Line
	5050 5750 5050 5500
Wire Wire Line
	4750 5500 4750 5600
$Comp
L Device:R R12
U 1 1 618D173E
P 5050 5350
F 0 "R12" H 5120 5396 50  0000 L CNN
F 1 "10M" H 5120 5305 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" V 4980 5350 50  0001 C CNN
F 3 "~" H 5050 5350 50  0001 C CNN
	1    5050 5350
	1    0    0    -1  
$EndComp
$Comp
L Device:R R11
U 1 1 618D1738
P 4750 5350
F 0 "R11" H 4820 5396 50  0000 L CNN
F 1 "10M" H 4820 5305 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" V 4680 5350 50  0001 C CNN
F 3 "~" H 4750 5350 50  0001 C CNN
	1    4750 5350
	1    0    0    -1  
$EndComp
Text GLabel 5300 5000 2    50   Input ~ 0
RLDOUT
Connection ~ 1850 7400
Wire Wire Line
	1850 7400 2000 7400
Wire Wire Line
	1700 7400 1850 7400
Connection ~ 2000 7400
Wire Wire Line
	1850 7700 2000 7700
Connection ~ 1850 7700
Wire Wire Line
	1700 7700 1850 7700
Wire Wire Line
	4150 4700 4100 4700
Wire Wire Line
	3750 4850 3900 4850
Connection ~ 3750 4850
Wire Wire Line
	3750 4700 3800 4700
Wire Wire Line
	3750 4700 3750 4850
$Comp
L Jumper:SolderJumper_2_Open JP3
U 1 1 618A9C52
P 3950 4700
F 0 "JP3" H 3950 4600 50  0000 C CNN
F 1 "Jumper" H 3950 4800 50  0000 C CNN
F 2 "Resistor_SMD:R_0402_1005Metric" H 3950 4700 50  0001 C CNN
F 3 "~" H 3950 4700 50  0001 C CNN
	1    3950 4700
	1    0    0    -1  
$EndComp
Wire Wire Line
	3900 5450 3950 5450
Connection ~ 3900 5450
Wire Wire Line
	3350 5450 3900 5450
Connection ~ 3600 5300
Wire Wire Line
	3600 5300 3650 5300
Wire Wire Line
	3900 4850 3900 4900
Wire Wire Line
	3600 4850 3750 4850
Wire Wire Line
	3600 4900 3600 4850
Wire Wire Line
	3900 5450 3900 5200
Wire Wire Line
	3600 5200 3600 5300
Wire Wire Line
	3350 5300 3600 5300
$Comp
L Device:R R5
U 1 1 61893D03
P 3900 5050
F 0 "R5" H 3970 5096 50  0000 L CNN
F 1 "10M" H 3970 5005 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" V 3830 5050 50  0001 C CNN
F 3 "~" H 3900 5050 50  0001 C CNN
	1    3900 5050
	1    0    0    -1  
$EndComp
$Comp
L Device:R R4
U 1 1 6189297D
P 3600 5050
F 0 "R4" H 3670 5096 50  0000 L CNN
F 1 "10M" H 3670 5005 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" V 3530 5050 50  0001 C CNN
F 3 "~" H 3600 5050 50  0001 C CNN
	1    3600 5050
	1    0    0    -1  
$EndComp
Text GLabel 4150 4700 2    50   Input ~ 0
RLDOUT
Connection ~ 4300 6600
Wire Wire Line
	4300 6600 4400 6600
Text GLabel 4400 6600 2    50   Input ~ 0
RLDOUT
Wire Wire Line
	3350 6450 4800 6450
Wire Wire Line
	4800 6450 4800 6500
Wire Wire Line
	4800 6900 4800 6800
Wire Wire Line
	4300 6900 4800 6900
Wire Wire Line
	3850 6600 4300 6600
Wire Wire Line
	3850 6900 4300 6900
Wire Wire Line
	3850 6900 3750 6900
Connection ~ 3850 6900
Connection ~ 3850 6600
Connection ~ 4300 6900
$Comp
L Device:R R1
U 1 1 6186689D
P 1600 7150
F 0 "R1" V 1700 7150 50  0000 L CNN
F 1 "1M" V 1700 7050 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" V 1530 7150 50  0001 C CNN
F 3 "~" H 1600 7150 50  0001 C CNN
	1    1600 7150
	0    -1   -1   0   
$EndComp
Text GLabel 2250 6850 0    50   Input ~ 0
WCT_OUT
Wire Wire Line
	1750 7150 2250 7150
Wire Wire Line
	1350 7150 1450 7150
Wire Wire Line
	1350 7100 1350 7150
Wire Wire Line
	2250 7450 2150 7450
Wire Wire Line
	2250 7300 2150 7300
Wire Wire Line
	2150 7300 2150 7400
Wire Wire Line
	2150 7400 2150 7450
Connection ~ 2150 7400
Wire Wire Line
	2000 7400 2150 7400
$Comp
L power:Earth #PWR02
U 1 1 618463AA
P 1850 7700
F 0 "#PWR02" H 1850 7450 50  0001 C CNN
F 1 "Earth" H 1850 7550 50  0001 C CNN
F 2 "" H 1850 7700 50  0001 C CNN
F 3 "~" H 1850 7700 50  0001 C CNN
	1    1850 7700
	1    0    0    -1  
$EndComp
$Comp
L Device:C C1
U 1 1 61842970
P 1700 7550
F 0 "C1" H 1750 7650 50  0000 L CNN
F 1 "100n" H 1750 7450 50  0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 1738 7400 50  0001 C CNN
F 3 "~" H 1700 7550 50  0001 C CNN
	1    1700 7550
	1    0    0    -1  
$EndComp
$Comp
L Device:C C3
U 1 1 61841DE9
P 2000 7550
F 0 "C3" H 2050 7650 50  0000 L CNN
F 1 "100n" H 2050 7450 50  0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 2038 7400 50  0001 C CNN
F 3 "~" H 2000 7550 50  0001 C CNN
	1    2000 7550
	1    0    0    -1  
$EndComp
Wire Wire Line
	3350 7050 3550 7050
Wire Wire Line
	3350 6900 3550 6900
Wire Wire Line
	3350 7600 3750 7600
Wire Wire Line
	3350 7450 3850 7450
Wire Wire Line
	2150 7800 2250 7800
Wire Wire Line
	2150 7950 2150 8100
Connection ~ 2150 7950
Wire Wire Line
	2150 7800 2150 7950
Wire Wire Line
	2250 7950 2150 7950
$Comp
L power:Earth #PWR04
U 1 1 61832B23
P 2150 8100
F 0 "#PWR04" H 2150 7850 50  0001 C CNN
F 1 "Earth" H 2150 7950 50  0001 C CNN
F 2 "" H 2150 8100 50  0001 C CNN
F 3 "~" H 2150 8100 50  0001 C CNN
	1    2150 8100
	1    0    0    -1  
$EndComp
Wire Wire Line
	3350 7950 3500 7950
$Comp
L power:Earth #PWR07
U 1 1 618315B5
P 3500 8250
F 0 "#PWR07" H 3500 8000 50  0001 C CNN
F 1 "Earth" H 3500 8100 50  0001 C CNN
F 2 "" H 3500 8250 50  0001 C CNN
F 3 "~" H 3500 8250 50  0001 C CNN
	1    3500 8250
	1    0    0    -1  
$EndComp
$Comp
L Device:C C6
U 1 1 618315AF
P 3500 8100
F 0 "C6" H 3550 8200 50  0000 L CNN
F 1 "1u" H 3550 8000 50  0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 3538 7950 50  0001 C CNN
F 3 "~" H 3500 8100 50  0001 C CNN
	1    3500 8100
	1    0    0    -1  
$EndComp
Wire Wire Line
	3550 7000 3550 6900
Connection ~ 3550 7000
Wire Wire Line
	3550 7000 3700 7000
$Comp
L power:Earth #PWR08
U 1 1 6182FD8F
P 3700 7300
F 0 "#PWR08" H 3700 7050 50  0001 C CNN
F 1 "Earth" H 3700 7150 50  0001 C CNN
F 2 "" H 3700 7300 50  0001 C CNN
F 3 "~" H 3700 7300 50  0001 C CNN
	1    3700 7300
	1    0    0    -1  
$EndComp
$Comp
L Device:C C7
U 1 1 6182C768
P 3700 7150
F 0 "C7" H 3750 7250 50  0000 L CNN
F 1 "100n" H 3750 7050 50  0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 3738 7000 50  0001 C CNN
F 3 "~" H 3700 7150 50  0001 C CNN
	1    3700 7150
	1    0    0    -1  
$EndComp
Wire Wire Line
	3550 7050 3550 7000
Wire Wire Line
	3750 6750 3350 6750
Wire Wire Line
	3750 6900 3750 6750
Wire Wire Line
	3350 6600 3850 6600
$Comp
L Device:C C9
U 1 1 61825EE9
P 4300 6750
F 0 "C9" H 4200 6850 50  0000 L CNN
F 1 "1n" H 4200 6650 50  0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 4338 6600 50  0001 C CNN
F 3 "~" H 4300 6750 50  0001 C CNN
	1    4300 6750
	1    0    0    -1  
$EndComp
$Comp
L Device:R R2
U 1 1 61825868
P 3850 6750
F 0 "R2" H 3900 6850 50  0000 L CNN
F 1 "10M" H 3900 6650 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" V 3780 6750 50  0001 C CNN
F 3 "~" H 3850 6750 50  0001 C CNN
	1    3850 6750
	1    0    0    -1  
$EndComp
Wire Wire Line
	4950 7750 4950 8150
Wire Wire Line
	4400 7750 4400 8000
$Comp
L Device:R R3
U 1 1 6181EC69
P 4800 6650
F 0 "R3" H 4870 6696 50  0000 L CNN
F 1 "10k" H 4870 6605 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" V 4730 6650 50  0001 C CNN
F 3 "~" H 4800 6650 50  0001 C CNN
	1    4800 6650
	1    0    0    -1  
$EndComp
Connection ~ 4950 7750
Connection ~ 4400 7750
Wire Wire Line
	4950 7450 5250 7450
Wire Wire Line
	4850 7750 4950 7750
Connection ~ 4950 7450
Wire Wire Line
	4100 7450 4400 7450
$Comp
L Device:C C10
U 1 1 61813756
P 4400 7600
F 0 "C10" H 4450 7700 50  0000 L CNN
F 1 "18p" H 4450 7500 50  0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 4438 7450 50  0001 C CNN
F 3 "~" H 4400 7600 50  0001 C CNN
	1    4400 7600
	1    0    0    -1  
$EndComp
Wire Wire Line
	4400 7750 4550 7750
Connection ~ 4400 7450
Wire Wire Line
	4400 7450 4700 7450
Wire Wire Line
	4700 7450 4950 7450
Connection ~ 4700 7450
$Comp
L power:Earth #PWR010
U 1 1 6181A665
P 5250 7750
F 0 "#PWR010" H 5250 7500 50  0001 C CNN
F 1 "Earth" H 5250 7600 50  0001 C CNN
F 2 "" H 5250 7750 50  0001 C CNN
F 3 "~" H 5250 7750 50  0001 C CNN
	1    5250 7750
	1    0    0    -1  
$EndComp
$Comp
L power:Earth #PWR09
U 1 1 6181A1BB
P 4100 7750
F 0 "#PWR09" H 4100 7500 50  0001 C CNN
F 1 "Earth" H 4100 7600 50  0001 C CNN
F 2 "" H 4100 7750 50  0001 C CNN
F 3 "~" H 4100 7750 50  0001 C CNN
	1    4100 7750
	1    0    0    -1  
$EndComp
$Comp
L Device:C C11
U 1 1 6181884A
P 4950 7600
F 0 "C11" H 5000 7700 50  0000 L CNN
F 1 "18p" H 5000 7500 50  0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 4988 7450 50  0001 C CNN
F 3 "~" H 4950 7600 50  0001 C CNN
	1    4950 7600
	1    0    0    -1  
$EndComp
$Comp
L Device:C C12
U 1 1 61818844
P 5250 7600
F 0 "C12" H 5300 7700 50  0000 L CNN
F 1 "100n" H 5300 7500 50  0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 5288 7450 50  0001 C CNN
F 3 "~" H 5250 7600 50  0001 C CNN
	1    5250 7600
	1    0    0    -1  
$EndComp
$Comp
L Device:C C8
U 1 1 61815832
P 4100 7600
F 0 "C8" H 4100 7700 50  0000 L CNN
F 1 "100n" H 4100 7500 50  0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 4138 7450 50  0001 C CNN
F 3 "~" H 4100 7600 50  0001 C CNN
	1    4100 7600
	1    0    0    -1  
$EndComp
$Comp
L Device:Crystal Y1
U 1 1 61811E90
P 4700 7750
F 0 "Y1" H 4700 7900 50  0000 C CNN
F 1 "4.096" H 4700 7600 50  0000 C CNN
F 2 "RasperryPi ECG Hat:SMD_Crystal_2_pin_11.3_4.5" H 4700 7750 50  0001 C CNN
F 3 "~" H 4700 7750 50  0001 C CNN
	1    4700 7750
	1    0    0    -1  
$EndComp
Text GLabel 2250 6550 0    50   Input ~ 0
ALARMB
Text GLabel 2250 6400 0    50   Input ~ 0
SYNCB
Text GLabel 2250 6250 0    50   Input ~ 0
DRDYB
Text GLabel 2250 5750 0    50   Input ~ 0
MOSI
Text GLabel 2250 5600 0    50   Input ~ 0
MISO
Text GLabel 2250 5450 0    50   Input ~ 0
SCLK
Text GLabel 2250 5300 0    50   Input ~ 0
CSB1
Text GLabel 3350 6050 2    50   Input ~ 0
IN6
Text GLabel 3350 5900 2    50   Input ~ 0
IN5
Text GLabel 5100 5750 2    50   Input ~ 0
IN4
Text GLabel 3950 5450 2    50   Input ~ 0
IN2
Text GLabel 3650 5300 2    50   Input ~ 0
IN1
Wire Wire Line
	4450 5000 4550 5000
$Comp
L Jumper:SolderJumper_2_Open JP4
U 1 1 618D1755
P 4700 5000
F 0 "JP4" H 4700 4900 50  0000 C CNN
F 1 "Jumper" H 4700 5100 50  0000 C CNN
F 2 "Resistor_SMD:R_0402_1005Metric" H 4700 5000 50  0001 C CNN
F 3 "~" H 4700 5000 50  0001 C CNN
	1    4700 5000
	1    0    0    -1  
$EndComp
Connection ~ 3750 4700
Wire Wire Line
	3700 4700 3750 4700
Wire Wire Line
	3300 4700 3400 4700
$Comp
L power:Earth #PWR011
U 1 1 618BDAE2
P 3300 4700
F 0 "#PWR011" H 3300 4450 50  0001 C CNN
F 1 "Earth" H 3300 4550 50  0001 C CNN
F 2 "" H 3300 4700 50  0001 C CNN
F 3 "~" H 3300 4700 50  0001 C CNN
	1    3300 4700
	1    0    0    -1  
$EndComp
$Comp
L Jumper:SolderJumper_2_Open JP2
U 1 1 618B4784
P 3550 4700
F 0 "JP2" H 3550 4600 50  0000 C CNN
F 1 "Jumper" H 3550 4800 50  0000 C CNN
F 2 "Resistor_SMD:R_0402_1005Metric" H 3550 4700 50  0001 C CNN
F 3 "~" H 3550 4700 50  0001 C CNN
	1    3550 4700
	1    0    0    -1  
$EndComp
$Comp
L power:Earth #PWR031
U 1 1 6193805A
P 4250 7250
F 0 "#PWR031" H 4250 7000 50  0001 C CNN
F 1 "Earth" H 4250 7100 50  0001 C CNN
F 2 "" H 4250 7250 50  0001 C CNN
F 3 "~" H 4250 7250 50  0001 C CNN
	1    4250 7250
	1    0    0    -1  
$EndComp
Wire Wire Line
	4700 7250 4750 7250
Connection ~ 4700 7250
Wire Wire Line
	4650 7250 4700 7250
$Comp
L Jumper:SolderJumper_2_Open JP5
U 1 1 61938064
P 4900 7250
F 0 "JP5" H 4900 7150 50  0000 C CNN
F 1 "Jumper" H 4900 7350 50  0000 C CNN
F 2 "Resistor_SMD:R_0402_1005Metric" H 4900 7250 50  0001 C CNN
F 3 "~" H 4900 7250 50  0001 C CNN
	1    4900 7250
	1    0    0    -1  
$EndComp
Wire Wire Line
	4250 7250 4350 7250
$Comp
L Jumper:SolderJumper_2_Open JP1
U 1 1 6193806B
P 4500 7250
F 0 "JP1" H 4500 7150 50  0000 C CNN
F 1 "Jumper" H 4500 7350 50  0000 C CNN
F 2 "Resistor_SMD:R_0402_1005Metric" H 4500 7250 50  0001 C CNN
F 3 "~" H 4500 7250 50  0001 C CNN
	1    4500 7250
	1    0    0    -1  
$EndComp
Wire Wire Line
	4700 7250 4700 7450
Wire Wire Line
	3850 8000 4400 8000
Wire Wire Line
	3850 7450 3850 8000
Wire Wire Line
	3750 8150 4950 8150
Wire Wire Line
	3750 7600 3750 8150
Wire Notes Line
	850  4450 850  8400
Text Notes 9450 1050 0    55   ~ 0
Raspberry Pi Headers and connectors\n
Text GLabel 6300 7950 0    50   Input ~ 0
WCT_OUT
Text GLabel 6300 7700 0    50   Input ~ 0
ALARMB
Text GLabel 6300 7450 0    50   Input ~ 0
SYNCB
Text GLabel 6300 7200 0    50   Input ~ 0
DRDYB
$Comp
L Connector:Raspberry_Pi_2_3 J1
U 1 1 61978622
P 10900 3000
F 0 "J1" H 10250 4250 50  0000 C CNN
F 1 "Raspberry_Pi_4" H 10100 1700 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x20_P2.54mm_Vertical" H 10900 3000 50  0001 C CNN
F 3 "https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/rpi_SCH_3bplus_1p0_reduced.pdf" H 10900 3000 50  0001 C CNN
	1    10900 3000
	1    0    0    -1  
$EndComp
Text GLabel 11700 3400 2    50   Input ~ 0
MOSI
Text GLabel 11700 3500 2    50   Input ~ 0
SCLK
Text GLabel 10100 3400 0    50   Input ~ 0
CSB1
Text GLabel 10100 3300 0    50   Input ~ 0
CSB2
Text GLabel 11700 3300 2    50   Input ~ 0
MISO
NoConn ~ 2250 5900
Wire Wire Line
	6300 7450 6350 7450
Wire Wire Line
	6350 7450 6350 7400
Wire Wire Line
	6300 7200 6350 7200
Wire Wire Line
	6350 7700 6300 7700
Wire Wire Line
	6350 7950 6300 7950
Wire Wire Line
	6350 7400 6450 7400
Wire Wire Line
	6450 7400 6450 7450
Wire Wire Line
	6450 7450 6550 7450
Wire Wire Line
	6350 7650 6450 7650
Wire Wire Line
	6450 7650 6450 7550
Wire Wire Line
	6450 7550 6550 7550
Wire Wire Line
	6350 7650 6350 7700
Wire Wire Line
	6350 7900 6500 7900
Wire Wire Line
	6500 7900 6500 7650
Wire Wire Line
	6500 7650 6550 7650
Wire Wire Line
	6350 7900 6350 7950
Wire Wire Line
	6350 7200 6350 7150
Wire Wire Line
	6350 7150 6500 7150
Wire Wire Line
	6500 7150 6500 7350
Wire Wire Line
	6500 7350 6550 7350
$Comp
L Device:R R6
U 1 1 61B0BB19
P 4100 1250
F 0 "R6" H 4170 1296 50  0000 L CNN
F 1 "600" H 4170 1205 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" V 4030 1250 50  0001 C CNN
F 3 "~" H 4100 1250 50  0001 C CNN
	1    4100 1250
	1    0    0    -1  
$EndComp
$Comp
L power:Earth #PWR027
U 1 1 61B24997
P 4100 1400
F 0 "#PWR027" H 4100 1150 50  0001 C CNN
F 1 "Earth" H 4100 1250 50  0001 C CNN
F 2 "" H 4100 1400 50  0001 C CNN
F 3 "~" H 4100 1400 50  0001 C CNN
	1    4100 1400
	1    0    0    -1  
$EndComp
$Comp
L power:Earth #PWR015
U 1 1 61B6D580
P 1850 9200
F 0 "#PWR015" H 1850 8950 50  0001 C CNN
F 1 "Earth" H 1850 9050 50  0001 C CNN
F 2 "" H 1850 9200 50  0001 C CNN
F 3 "~" H 1850 9200 50  0001 C CNN
	1    1850 9200
	1    0    0    -1  
$EndComp
$Comp
L Device:C C16
U 1 1 61B6D586
P 1850 9050
F 0 "C16" H 1900 9150 50  0000 L CNN
F 1 "100n" H 1900 8950 50  0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 1888 8900 50  0001 C CNN
F 3 "~" H 1850 9050 50  0001 C CNN
	1    1850 9050
	1    0    0    -1  
$EndComp
Wire Wire Line
	1650 8900 1850 8900
$Comp
L Device:C C15
U 1 1 61B8D6FD
P 1650 10500
F 0 "C15" H 1700 10600 50  0000 L CNN
F 1 "100n" H 1700 10400 50  0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 1688 10350 50  0001 C CNN
F 3 "~" H 1650 10500 50  0001 C CNN
	1    1650 10500
	1    0    0    -1  
$EndComp
Wire Wire Line
	1450 10350 1650 10350
Wire Wire Line
	2400 9450 2650 9450
$Comp
L Device:C C13
U 1 1 61BA15F3
P 1000 9850
F 0 "C13" H 1050 9950 50  0000 L CNN
F 1 "18p" H 1050 9750 50  0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 1038 9700 50  0001 C CNN
F 3 "~" H 1000 9850 50  0001 C CNN
	1    1000 9850
	1    0    0    -1  
$EndComp
$Comp
L Device:C C14
U 1 1 61BA15FA
P 1550 9850
F 0 "C14" H 1600 9950 50  0000 L CNN
F 1 "18p" H 1600 9750 50  0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 1588 9700 50  0001 C CNN
F 3 "~" H 1550 9850 50  0001 C CNN
	1    1550 9850
	1    0    0    -1  
$EndComp
$Comp
L Device:Crystal Y2
U 1 1 61BA1600
P 1300 9700
F 0 "Y2" H 1300 9850 50  0000 C CNN
F 1 "4.096" H 1300 9550 50  0000 C CNN
F 2 "RasperryPi ECG Hat:SMD_Crystal_2_pin_11.3_4.5" H 1300 9700 50  0001 C CNN
F 3 "~" H 1300 9700 50  0001 C CNN
	1    1300 9700
	1    0    0    -1  
$EndComp
Wire Wire Line
	1000 9700 1150 9700
Wire Wire Line
	1450 9700 1550 9700
$Comp
L power:Earth #PWR013
U 1 1 61BD515C
P 1550 10000
F 0 "#PWR013" H 1550 9750 50  0001 C CNN
F 1 "Earth" H 1550 9850 50  0001 C CNN
F 2 "" H 1550 10000 50  0001 C CNN
F 3 "~" H 1550 10000 50  0001 C CNN
	1    1550 10000
	1    0    0    -1  
$EndComp
$Comp
L power:Earth #PWR012
U 1 1 61BDB6C8
P 1000 10000
F 0 "#PWR012" H 1000 9750 50  0001 C CNN
F 1 "Earth" H 1000 9850 50  0001 C CNN
F 2 "" H 1000 10000 50  0001 C CNN
F 3 "~" H 1000 10000 50  0001 C CNN
	1    1000 10000
	1    0    0    -1  
$EndComp
Wire Wire Line
	1850 8900 2400 8900
Wire Wire Line
	2400 8900 2400 9450
Connection ~ 1850 8900
$Comp
L power:Earth #PWR022
U 1 1 61C0DF90
P 2400 9550
F 0 "#PWR022" H 2400 9300 50  0001 C CNN
F 1 "Earth" H 2400 9400 50  0001 C CNN
F 2 "" H 2400 9550 50  0001 C CNN
F 3 "~" H 2400 9550 50  0001 C CNN
	1    2400 9550
	1    0    0    -1  
$EndComp
Wire Wire Line
	2400 9550 2650 9550
Wire Wire Line
	2650 9650 2450 9650
Wire Wire Line
	2450 9650 2450 9700
Wire Wire Line
	1000 9400 1000 9700
Connection ~ 1000 9700
Wire Wire Line
	1900 9400 1900 9700
Wire Wire Line
	1900 9700 2450 9700
Wire Wire Line
	1000 9400 1900 9400
Wire Wire Line
	1550 9700 1550 9650
Wire Wire Line
	1550 9650 1800 9650
Wire Wire Line
	1800 9650 1800 9750
Wire Wire Line
	1800 9750 2650 9750
Connection ~ 1550 9700
$Comp
L power:Earth #PWR014
U 1 1 61B8D6F7
P 1650 10650
F 0 "#PWR014" H 1650 10400 50  0001 C CNN
F 1 "Earth" H 1650 10500 50  0001 C CNN
F 2 "" H 1650 10650 50  0001 C CNN
F 3 "~" H 1650 10650 50  0001 C CNN
	1    1650 10650
	1    0    0    -1  
$EndComp
$Comp
L power:Earth #PWR018
U 1 1 61C7F261
P 2050 10150
F 0 "#PWR018" H 2050 9900 50  0001 C CNN
F 1 "Earth" H 2050 10000 50  0001 C CNN
F 2 "" H 2050 10150 50  0001 C CNN
F 3 "~" H 2050 10150 50  0001 C CNN
	1    2050 10150
	1    0    0    -1  
$EndComp
$Comp
L pspice:INDUCTOR L2
U 1 1 61CD7BEF
P 1550 2200
F 0 "L2" H 1550 2415 50  0000 C CNN
F 1 "INDUCTOR" H 1550 2324 50  0000 C CNN
F 2 "Resistor_SMD:R_0402_1005Metric" H 1550 2200 50  0001 C CNN
F 3 "~" H 1550 2200 50  0001 C CNN
	1    1550 2200
	1    0    0    -1  
$EndComp
Wire Wire Line
	1300 2200 1200 2200
$Comp
L Device:R R7
U 1 1 61CD7C29
P 4100 2500
F 0 "R7" H 4170 2546 50  0000 L CNN
F 1 "600" H 4170 2455 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" V 4030 2500 50  0001 C CNN
F 3 "~" H 4100 2500 50  0001 C CNN
	1    4100 2500
	1    0    0    -1  
$EndComp
$Comp
L power:Earth #PWR028
U 1 1 61CD7C36
P 4100 2650
F 0 "#PWR028" H 4100 2400 50  0001 C CNN
F 1 "Earth" H 4100 2500 50  0001 C CNN
F 2 "" H 4100 2650 50  0001 C CNN
F 3 "~" H 4100 2650 50  0001 C CNN
	1    4100 2650
	1    0    0    -1  
$EndComp
$Comp
L pspice:INDUCTOR L3
U 1 1 61D12407
P 1600 3400
F 0 "L3" H 1600 3615 50  0000 C CNN
F 1 "INDUCTOR" H 1600 3524 50  0000 C CNN
F 2 "Resistor_SMD:R_0402_1005Metric" H 1600 3400 50  0001 C CNN
F 3 "~" H 1600 3400 50  0001 C CNN
	1    1600 3400
	1    0    0    -1  
$EndComp
Wire Wire Line
	1350 3400 1250 3400
$Comp
L Device:R R8
U 1 1 61D1243E
P 4100 3650
F 0 "R8" H 4170 3696 50  0000 L CNN
F 1 "600" H 4170 3605 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" V 4030 3650 50  0001 C CNN
F 3 "~" H 4100 3650 50  0001 C CNN
	1    4100 3650
	1    0    0    -1  
$EndComp
$Comp
L power:Earth #PWR029
U 1 1 61D1244A
P 4100 3800
F 0 "#PWR029" H 4100 3550 50  0001 C CNN
F 1 "Earth" H 4100 3650 50  0001 C CNN
F 2 "" H 4100 3800 50  0001 C CNN
F 3 "~" H 4100 3800 50  0001 C CNN
	1    4100 3800
	1    0    0    -1  
$EndComp
Text GLabel 3550 1200 2    50   Input ~ 0
ECG_3v3
Text GLabel 4100 650  0    50   Input ~ 0
ECG_3v3
Text GLabel 3550 2200 2    50   Input ~ 0
Strain_3v3
Text GLabel 4100 3200 1    50   Input ~ 0
ADC_3v3
Text GLabel 4100 2050 1    50   Input ~ 0
Strain_3v3
Text GLabel 3600 3400 2    50   Input ~ 0
ADC_3v3
$Comp
L power:Earth #PWR01
U 1 1 6180AA32
P 1950 1500
F 0 "#PWR01" H 1950 1250 50  0001 C CNN
F 1 "Earth" H 1950 1350 50  0001 C CNN
F 2 "" H 1950 1500 50  0001 C CNN
F 3 "~" H 1950 1500 50  0001 C CNN
	1    1950 1500
	1    0    0    -1  
$EndComp
$Comp
L power:Earth #PWR03
U 1 1 6180A77F
P 2250 1500
F 0 "#PWR03" H 2250 1250 50  0001 C CNN
F 1 "Earth" H 2250 1350 50  0001 C CNN
F 2 "" H 2250 1500 50  0001 C CNN
F 3 "~" H 2250 1500 50  0001 C CNN
	1    2250 1500
	1    0    0    -1  
$EndComp
$Comp
L power:Earth #PWR05
U 1 1 6180A3CD
P 2700 1500
F 0 "#PWR05" H 2700 1250 50  0001 C CNN
F 1 "Earth" H 2700 1350 50  0001 C CNN
F 2 "" H 2700 1500 50  0001 C CNN
F 3 "~" H 2700 1500 50  0001 C CNN
	1    2700 1500
	1    0    0    -1  
$EndComp
$Comp
L power:Earth #PWR06
U 1 1 61809434
P 3250 1500
F 0 "#PWR06" H 3250 1250 50  0001 C CNN
F 1 "Earth" H 3250 1350 50  0001 C CNN
F 2 "" H 3250 1500 50  0001 C CNN
F 3 "~" H 3250 1500 50  0001 C CNN
	1    3250 1500
	1    0    0    -1  
$EndComp
Wire Wire Line
	3250 1200 3550 1200
Wire Wire Line
	3000 1200 3250 1200
Connection ~ 3250 1200
$Comp
L Device:C C5
U 1 1 61808F91
P 3250 1350
F 0 "C5" H 3365 1396 50  0000 L CNN
F 1 "4.7u" H 3365 1305 50  0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 3288 1200 50  0001 C CNN
F 3 "~" H 3250 1350 50  0001 C CNN
	1    3250 1350
	1    0    0    -1  
$EndComp
Wire Wire Line
	2250 1200 2400 1200
Connection ~ 2250 1200
$Comp
L Device:C C4
U 1 1 61807F65
P 2250 1350
F 0 "C4" H 2365 1396 50  0000 L CNN
F 1 "4.7u" H 2365 1305 50  0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 2288 1200 50  0001 C CNN
F 3 "~" H 2250 1350 50  0001 C CNN
	1    2250 1350
	1    0    0    -1  
$EndComp
Wire Wire Line
	1950 1200 2250 1200
Wire Wire Line
	1800 1200 1950 1200
Connection ~ 1950 1200
$Comp
L Device:C C2
U 1 1 61806C93
P 1950 1350
F 0 "C2" H 2065 1396 50  0000 L CNN
F 1 "10u" H 2065 1305 50  0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 1988 1200 50  0001 C CNN
F 3 "~" H 1950 1350 50  0001 C CNN
	1    1950 1350
	1    0    0    -1  
$EndComp
$Comp
L Regulator_Linear:MCP1703A-5002_SOT23 U1
U 1 1 618046B1
P 2700 1200
F 0 "U1" H 2700 1442 50  0000 C CNN
F 1 "MCP1703A" H 2700 1351 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 2700 1400 50  0001 C CNN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/20005122B.pdf" H 2700 1150 50  0001 C CNN
	1    2700 1200
	1    0    0    -1  
$EndComp
$Comp
L power:Earth #PWR016
U 1 1 61DFF8F6
P 1950 2500
F 0 "#PWR016" H 1950 2250 50  0001 C CNN
F 1 "Earth" H 1950 2350 50  0001 C CNN
F 2 "" H 1950 2500 50  0001 C CNN
F 3 "~" H 1950 2500 50  0001 C CNN
	1    1950 2500
	1    0    0    -1  
$EndComp
$Comp
L power:Earth #PWR020
U 1 1 61DFF8FC
P 2250 2500
F 0 "#PWR020" H 2250 2250 50  0001 C CNN
F 1 "Earth" H 2250 2350 50  0001 C CNN
F 2 "" H 2250 2500 50  0001 C CNN
F 3 "~" H 2250 2500 50  0001 C CNN
	1    2250 2500
	1    0    0    -1  
$EndComp
$Comp
L power:Earth #PWR023
U 1 1 61DFF902
P 2700 2500
F 0 "#PWR023" H 2700 2250 50  0001 C CNN
F 1 "Earth" H 2700 2350 50  0001 C CNN
F 2 "" H 2700 2500 50  0001 C CNN
F 3 "~" H 2700 2500 50  0001 C CNN
	1    2700 2500
	1    0    0    -1  
$EndComp
$Comp
L power:Earth #PWR025
U 1 1 61DFF908
P 3250 2500
F 0 "#PWR025" H 3250 2250 50  0001 C CNN
F 1 "Earth" H 3250 2350 50  0001 C CNN
F 2 "" H 3250 2500 50  0001 C CNN
F 3 "~" H 3250 2500 50  0001 C CNN
	1    3250 2500
	1    0    0    -1  
$EndComp
Wire Wire Line
	3250 2200 3550 2200
Wire Wire Line
	3000 2200 3250 2200
Connection ~ 3250 2200
$Comp
L Device:C C21
U 1 1 61DFF911
P 3250 2350
F 0 "C21" H 3365 2396 50  0000 L CNN
F 1 "4.7u" H 3365 2305 50  0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 3288 2200 50  0001 C CNN
F 3 "~" H 3250 2350 50  0001 C CNN
	1    3250 2350
	1    0    0    -1  
$EndComp
$Comp
L Device:C C19
U 1 1 61DFF919
P 2250 2350
F 0 "C19" H 2365 2396 50  0000 L CNN
F 1 "4.7u" H 2365 2305 50  0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 2288 2200 50  0001 C CNN
F 3 "~" H 2250 2350 50  0001 C CNN
	1    2250 2350
	1    0    0    -1  
$EndComp
Wire Wire Line
	1950 2200 2250 2200
Wire Wire Line
	1800 2200 1950 2200
Connection ~ 1950 2200
$Comp
L Device:C C17
U 1 1 61DFF922
P 1950 2350
F 0 "C17" H 2065 2396 50  0000 L CNN
F 1 "10u" H 2065 2305 50  0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 1988 2200 50  0001 C CNN
F 3 "~" H 1950 2350 50  0001 C CNN
	1    1950 2350
	1    0    0    -1  
$EndComp
$Comp
L Regulator_Linear:MCP1703A-5002_SOT23 U3
U 1 1 61DFF928
P 2700 2200
F 0 "U3" H 2700 2442 50  0000 C CNN
F 1 "MCP1703A" H 2700 2351 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 2700 2400 50  0001 C CNN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/20005122B.pdf" H 2700 2150 50  0001 C CNN
	1    2700 2200
	1    0    0    -1  
$EndComp
$Comp
L power:Earth #PWR017
U 1 1 61E14799
P 2000 3700
F 0 "#PWR017" H 2000 3450 50  0001 C CNN
F 1 "Earth" H 2000 3550 50  0001 C CNN
F 2 "" H 2000 3700 50  0001 C CNN
F 3 "~" H 2000 3700 50  0001 C CNN
	1    2000 3700
	1    0    0    -1  
$EndComp
$Comp
L power:Earth #PWR021
U 1 1 61E1479F
P 2300 3700
F 0 "#PWR021" H 2300 3450 50  0001 C CNN
F 1 "Earth" H 2300 3550 50  0001 C CNN
F 2 "" H 2300 3700 50  0001 C CNN
F 3 "~" H 2300 3700 50  0001 C CNN
	1    2300 3700
	1    0    0    -1  
$EndComp
$Comp
L power:Earth #PWR024
U 1 1 61E147A5
P 2750 3700
F 0 "#PWR024" H 2750 3450 50  0001 C CNN
F 1 "Earth" H 2750 3550 50  0001 C CNN
F 2 "" H 2750 3700 50  0001 C CNN
F 3 "~" H 2750 3700 50  0001 C CNN
	1    2750 3700
	1    0    0    -1  
$EndComp
$Comp
L power:Earth #PWR026
U 1 1 61E147AB
P 3300 3700
F 0 "#PWR026" H 3300 3450 50  0001 C CNN
F 1 "Earth" H 3300 3550 50  0001 C CNN
F 2 "" H 3300 3700 50  0001 C CNN
F 3 "~" H 3300 3700 50  0001 C CNN
	1    3300 3700
	1    0    0    -1  
$EndComp
Wire Wire Line
	3300 3400 3600 3400
Wire Wire Line
	3050 3400 3300 3400
Connection ~ 3300 3400
$Comp
L Device:C C22
U 1 1 61E147B4
P 3300 3550
F 0 "C22" H 3415 3596 50  0000 L CNN
F 1 "4.7u" H 3415 3505 50  0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 3338 3400 50  0001 C CNN
F 3 "~" H 3300 3550 50  0001 C CNN
	1    3300 3550
	1    0    0    -1  
$EndComp
Wire Wire Line
	2300 3400 2450 3400
Connection ~ 2300 3400
$Comp
L Device:C C20
U 1 1 61E147BC
P 2300 3550
F 0 "C20" H 2415 3596 50  0000 L CNN
F 1 "4.7u" H 2415 3505 50  0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 2338 3400 50  0001 C CNN
F 3 "~" H 2300 3550 50  0001 C CNN
	1    2300 3550
	1    0    0    -1  
$EndComp
Wire Wire Line
	2000 3400 2300 3400
Wire Wire Line
	1850 3400 2000 3400
Connection ~ 2000 3400
$Comp
L Device:C C18
U 1 1 61E147C5
P 2000 3550
F 0 "C18" H 2115 3596 50  0000 L CNN
F 1 "10u" H 2115 3505 50  0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 2038 3400 50  0001 C CNN
F 3 "~" H 2000 3550 50  0001 C CNN
	1    2000 3550
	1    0    0    -1  
$EndComp
$Comp
L Regulator_Linear:MCP1703A-5002_SOT23 U4
U 1 1 61E147CB
P 2750 3400
F 0 "U4" H 2750 3642 50  0000 C CNN
F 1 "MCP1703A" H 2750 3551 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 2750 3600 50  0001 C CNN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/20005122B.pdf" H 2750 3350 50  0001 C CNN
	1    2750 3400
	1    0    0    -1  
$EndComp
Wire Notes Line
	850  3950 4400 3950
Wire Notes Line
	4400 3950 4400 550 
Wire Notes Line
	850  550  850  3950
Wire Notes Line
	850  550  4400 550 
Text GLabel 1800 7300 0    50   Input ~ 0
ECG_3v3
Wire Wire Line
	1800 7300 1850 7300
Wire Wire Line
	1850 7300 1850 7400
Text GLabel 1650 8900 0    50   Input ~ 0
ADC_3v3
Text GLabel 1450 10350 0    50   Input ~ 0
ADC_3v3
$Comp
L power:Earth #PWR030
U 1 1 61E80AA6
P 4150 10250
F 0 "#PWR030" H 4150 10000 50  0001 C CNN
F 1 "Earth" H 4150 10100 50  0001 C CNN
F 2 "" H 4150 10250 50  0001 C CNN
F 3 "~" H 4150 10250 50  0001 C CNN
	1    4150 10250
	1    0    0    -1  
$EndComp
Text GLabel 4150 9950 1    50   Input ~ 0
ADC_3v3
Text GLabel 3750 9950 2    50   Input ~ 0
CSB2
Wire Wire Line
	3650 9950 3750 9950
Text GLabel 3750 9850 2    50   Input ~ 0
MOSI
Text GLabel 3750 9750 2    50   Input ~ 0
MISO
Text GLabel 3750 9650 2    50   Input ~ 0
SCLK
Wire Wire Line
	3650 9650 3750 9650
Wire Wire Line
	3650 9750 3750 9750
Wire Wire Line
	3650 9850 3750 9850
$Comp
L power:Earth #PWR019
U 1 1 61F24073
P 2150 10350
F 0 "#PWR019" H 2150 10100 50  0001 C CNN
F 1 "Earth" H 2150 10200 50  0001 C CNN
F 2 "" H 2150 10350 50  0001 C CNN
F 3 "~" H 2150 10350 50  0001 C CNN
	1    2150 10350
	1    0    0    -1  
$EndComp
Text GLabel 2600 9850 0    50   Input ~ 0
~RESET
Text GLabel 2300 9950 0    50   Input ~ 0
~DSYNC
Text GLabel 2000 10050 0    50   Input ~ 0
~PDWN
Wire Wire Line
	2300 9950 2650 9950
Wire Wire Line
	2600 9850 2650 9850
Text GLabel 3750 9450 2    50   Input ~ 0
BUFEN
Text GLabel 3750 9550 2    50   Input ~ 0
DRDY
Wire Wire Line
	3750 9450 3650 9450
Wire Wire Line
	3650 9550 3750 9550
Text GLabel 3750 10050 2    50   Input ~ 0
POL
Wire Wire Line
	3750 10050 3650 10050
Wire Wire Line
	4500 10100 4500 10150
$Comp
L Device:R R9
U 1 1 61FAB1DF
P 4500 10300
F 0 "R9" H 4570 10346 50  0000 L CNN
F 1 "10k" H 4570 10255 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" V 4430 10300 50  0001 C CNN
F 3 "~" H 4500 10300 50  0001 C CNN
	1    4500 10300
	1    0    0    -1  
$EndComp
Wire Wire Line
	4500 10450 4500 10500
$Comp
L Device:R R10
U 1 1 61FCD134
P 4500 10650
F 0 "R10" H 4570 10696 50  0000 L CNN
F 1 "10k" H 4570 10605 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" V 4430 10650 50  0001 C CNN
F 3 "~" H 4500 10650 50  0001 C CNN
	1    4500 10650
	1    0    0    -1  
$EndComp
$Comp
L power:Earth #PWR033
U 1 1 61FD88A3
P 4500 10800
F 0 "#PWR033" H 4500 10550 50  0001 C CNN
F 1 "Earth" H 4500 10650 50  0001 C CNN
F 2 "" H 4500 10800 50  0001 C CNN
F 3 "~" H 4500 10800 50  0001 C CNN
	1    4500 10800
	1    0    0    -1  
$EndComp
Wire Wire Line
	3650 10250 4150 10250
Wire Wire Line
	4100 10350 4100 10450
Wire Wire Line
	4100 10450 4500 10450
Wire Wire Line
	3650 10350 4100 10350
Connection ~ 4500 10450
Text GLabel 3750 10450 2    50   Input ~ 0
AIN3
Text GLabel 3750 10550 2    50   Input ~ 0
AIN2
Text GLabel 3750 10650 2    50   Input ~ 0
AIN7
Text GLabel 3750 10750 2    50   Input ~ 0
AIN6
Wire Wire Line
	3750 10450 3650 10450
Wire Wire Line
	3750 10550 3650 10550
Wire Wire Line
	3750 10650 3650 10650
Wire Wire Line
	3750 10750 3650 10750
Wire Wire Line
	2050 10150 2650 10150
Wire Wire Line
	2100 10250 2100 10350
Wire Wire Line
	2100 10350 1650 10350
Wire Wire Line
	2100 10250 2650 10250
Connection ~ 1650 10350
Wire Wire Line
	2150 10350 2650 10350
Text GLabel 2500 10450 0    50   Input ~ 0
AIN0
Text GLabel 2500 10550 0    50   Input ~ 0
AIN1
Text GLabel 2500 10650 0    50   Input ~ 0
AIN4
Text GLabel 2500 10750 0    50   Input ~ 0
AIN5
Wire Wire Line
	2500 10450 2650 10450
Wire Wire Line
	2500 10550 2650 10550
Wire Wire Line
	2500 10650 2650 10650
Wire Wire Line
	2500 10750 2650 10750
Wire Wire Line
	2000 10050 2650 10050
Text GLabel 4500 10100 1    50   Input ~ 0
ADC_3v3
$Comp
L power:Earth #PWR034
U 1 1 6218E9C9
P 8500 9350
F 0 "#PWR034" H 8500 9100 50  0001 C CNN
F 1 "Earth" H 8500 9200 50  0001 C CNN
F 2 "" H 8500 9350 50  0001 C CNN
F 3 "~" H 8500 9350 50  0001 C CNN
	1    8500 9350
	0    1    1    0   
$EndComp
Text GLabel 8500 9250 0    50   Input ~ 0
AIN0
Text GLabel 8500 9550 0    50   Input ~ 0
AIN1
Text GLabel 9100 10050 2    50   Input ~ 0
AIN5
Text GLabel 8500 10150 0    50   Input ~ 0
AIN3
Text GLabel 8500 9850 0    50   Input ~ 0
AIN2
Text GLabel 9100 9450 2    50   Input ~ 0
AIN7
Text GLabel 9100 9750 2    50   Input ~ 0
AIN6
$Comp
L power:Earth #PWR035
U 1 1 6229D480
P 8500 9650
F 0 "#PWR035" H 8500 9400 50  0001 C CNN
F 1 "Earth" H 8500 9500 50  0001 C CNN
F 2 "" H 8500 9650 50  0001 C CNN
F 3 "~" H 8500 9650 50  0001 C CNN
	1    8500 9650
	0    1    1    0   
$EndComp
$Comp
L power:Earth #PWR036
U 1 1 622B7441
P 8500 9950
F 0 "#PWR036" H 8500 9700 50  0001 C CNN
F 1 "Earth" H 8500 9800 50  0001 C CNN
F 2 "" H 8500 9950 50  0001 C CNN
F 3 "~" H 8500 9950 50  0001 C CNN
	1    8500 9950
	0    1    1    0   
$EndComp
$Comp
L power:Earth #PWR037
U 1 1 622C4588
P 8500 10250
F 0 "#PWR037" H 8500 10000 50  0001 C CNN
F 1 "Earth" H 8500 10100 50  0001 C CNN
F 2 "" H 8500 10250 50  0001 C CNN
F 3 "~" H 8500 10250 50  0001 C CNN
	1    8500 10250
	0    1    1    0   
$EndComp
$Comp
L power:Earth #PWR038
U 1 1 6236EC9C
P 9100 9350
F 0 "#PWR038" H 9100 9100 50  0001 C CNN
F 1 "Earth" H 9100 9200 50  0001 C CNN
F 2 "" H 9100 9350 50  0001 C CNN
F 3 "~" H 9100 9350 50  0001 C CNN
	1    9100 9350
	0    -1   -1   0   
$EndComp
$Comp
L power:Earth #PWR039
U 1 1 6236EC95
P 9100 9650
F 0 "#PWR039" H 9100 9400 50  0001 C CNN
F 1 "Earth" H 9100 9500 50  0001 C CNN
F 2 "" H 9100 9650 50  0001 C CNN
F 3 "~" H 9100 9650 50  0001 C CNN
	1    9100 9650
	0    -1   -1   0   
$EndComp
$Comp
L power:Earth #PWR041
U 1 1 622DEDCB
P 9100 10250
F 0 "#PWR041" H 9100 10000 50  0001 C CNN
F 1 "Earth" H 9100 10100 50  0001 C CNN
F 2 "" H 9100 10250 50  0001 C CNN
F 3 "~" H 9100 10250 50  0001 C CNN
	1    9100 10250
	0    -1   -1   0   
$EndComp
Text GLabel 9100 10350 2    50   Input ~ 0
AIN4
Text GLabel 5750 10550 0    50   Input ~ 0
BUFEN
Text GLabel 5650 10800 0    50   Input ~ 0
DRDY
Text GLabel 5700 10300 0    50   Input ~ 0
POL
Text GLabel 5700 9800 0    50   Input ~ 0
~RESET
Text GLabel 5700 9550 0    50   Input ~ 0
~DSYNC
Text GLabel 5700 10050 0    50   Input ~ 0
~PDWN
Wire Wire Line
	5750 9800 5700 9800
Wire Wire Line
	5700 10050 5750 10050
Wire Wire Line
	5700 10300 5750 10300
Wire Wire Line
	5750 10000 5750 10050
Wire Wire Line
	5750 10250 5750 10300
Wire Wire Line
	5750 9750 5750 9800
Wire Wire Line
	5750 10500 5750 10550
Text GLabel 10700 1500 1    50   Input ~ 0
5V
Wire Wire Line
	10700 1500 10700 1600
Wire Wire Line
	10700 1600 10800 1600
Wire Wire Line
	10800 1600 10800 1700
Connection ~ 10700 1600
Wire Wire Line
	10700 1600 10700 1700
$Comp
L power:Earth #PWR042
U 1 1 62A332E1
P 10800 4350
F 0 "#PWR042" H 10800 4100 50  0001 C CNN
F 1 "Earth" H 10800 4200 50  0001 C CNN
F 2 "" H 10800 4350 50  0001 C CNN
F 3 "~" H 10800 4350 50  0001 C CNN
	1    10800 4350
	1    0    0    -1  
$EndComp
Wire Wire Line
	10500 4350 10500 4300
Wire Wire Line
	11200 4350 11100 4350
Wire Wire Line
	11200 4350 11200 4300
Wire Wire Line
	11100 4300 11100 4350
Connection ~ 11100 4350
Wire Wire Line
	11100 4350 11000 4350
Wire Wire Line
	11000 4300 11000 4350
Connection ~ 11000 4350
Wire Wire Line
	11000 4350 10900 4350
Wire Wire Line
	10900 4300 10900 4350
Connection ~ 10900 4350
Wire Wire Line
	10900 4350 10800 4350
Wire Wire Line
	10800 4300 10800 4350
Connection ~ 10800 4350
Wire Wire Line
	10800 4350 10700 4350
Wire Wire Line
	10700 4300 10700 4350
Connection ~ 10700 4350
Wire Wire Line
	10700 4350 10600 4350
Wire Wire Line
	10600 4300 10600 4350
Connection ~ 10600 4350
Wire Wire Line
	10600 4350 10500 4350
Text GLabel 11850 2400 2    50   Input ~ 0
I2C1_SDA
Text GLabel 11850 2500 2    50   Input ~ 0
I2C1_SCL
Wire Wire Line
	11850 2400 11700 2400
Wire Wire Line
	11850 2500 11700 2500
Text GLabel 10100 2100 0    50   Input ~ 0
UART_TX
Text GLabel 10100 2200 0    50   Input ~ 0
UART_RX
Text Notes 900  8750 0    55   ~ 0
Strain Gauge ADC \n
Wire Notes Line
	850  8650 850  10950
Wire Notes Line
	7200 8400 7200 4450
Wire Notes Line
	850  4450 7200 4450
Wire Notes Line
	850  8400 7200 8400
$Comp
L Device:R R13
U 1 1 63366A7A
P 5900 9300
F 0 "R13" H 5950 9350 50  0000 L CNN
F 1 "10k" H 5950 9250 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" V 5830 9300 50  0001 C CNN
F 3 "~" H 5900 9300 50  0001 C CNN
	1    5900 9300
	1    0    0    -1  
$EndComp
Text GLabel 5900 9150 1    50   Input ~ 0
ADC_3v3
$Comp
L Device:R R14
U 1 1 6340E9A3
P 6150 9300
F 0 "R14" H 6200 9350 50  0000 L CNN
F 1 "10k" H 6200 9250 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" V 6080 9300 50  0001 C CNN
F 3 "~" H 6150 9300 50  0001 C CNN
	1    6150 9300
	1    0    0    -1  
$EndComp
Text GLabel 6150 9150 1    50   Input ~ 0
ADC_3v3
$Comp
L Device:R R15
U 1 1 6343041A
P 6400 9300
F 0 "R15" H 6450 9350 50  0000 L CNN
F 1 "10k" H 6450 9250 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" V 6330 9300 50  0001 C CNN
F 3 "~" H 6400 9300 50  0001 C CNN
	1    6400 9300
	1    0    0    -1  
$EndComp
Text GLabel 6400 9150 1    50   Input ~ 0
ADC_3v3
$Comp
L Device:R R16
U 1 1 6345214F
P 6650 9300
F 0 "R16" H 6700 9350 50  0000 L CNN
F 1 "10k" H 6700 9250 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" V 6580 9300 50  0001 C CNN
F 3 "~" H 6650 9300 50  0001 C CNN
	1    6650 9300
	1    0    0    -1  
$EndComp
Text GLabel 6650 9150 1    50   Input ~ 0
ADC_3v3
Wire Wire Line
	6150 9750 6150 9650
Wire Wire Line
	5750 9750 6150 9750
Wire Wire Line
	6400 10000 6400 9750
Wire Wire Line
	5750 10000 6400 10000
Wire Wire Line
	5750 10250 6650 10250
Wire Wire Line
	5750 10500 6900 10500
Wire Wire Line
	5900 9550 5900 9450
$Comp
L Device:R R17
U 1 1 63473C20
P 6900 9300
F 0 "R17" H 6950 9350 50  0000 L CNN
F 1 "10k" H 6950 9250 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" V 6830 9300 50  0001 C CNN
F 3 "~" H 6900 9300 50  0001 C CNN
	1    6900 9300
	1    0    0    -1  
$EndComp
Wire Wire Line
	5650 10800 5750 10800
Wire Wire Line
	6650 9450 6650 9850
Wire Wire Line
	6900 9450 6900 9950
Wire Wire Line
	7000 9550 5900 9550
Connection ~ 5900 9550
Connection ~ 6150 9650
Wire Wire Line
	6150 9650 6150 9450
Wire Wire Line
	6150 9650 7000 9650
Connection ~ 6400 9750
Wire Wire Line
	6400 9750 6400 9450
Wire Wire Line
	6400 9750 7000 9750
Wire Wire Line
	7000 9850 6650 9850
Connection ~ 6650 9850
Wire Wire Line
	6650 9850 6650 10250
Wire Wire Line
	7000 9950 6900 9950
Connection ~ 6900 9950
Wire Wire Line
	6900 9950 6900 10500
Wire Wire Line
	7000 10050 7000 10750
Wire Wire Line
	7000 10750 5750 10750
Wire Wire Line
	5750 10750 5750 10800
Text GLabel 6900 9150 1    50   Input ~ 0
ADC_3v3
$Comp
L power:Earth #PWR045
U 1 1 63B4D185
P 4850 10800
F 0 "#PWR045" H 4850 10550 50  0001 C CNN
F 1 "Earth" H 4850 10650 50  0001 C CNN
F 2 "" H 4850 10800 50  0001 C CNN
F 3 "~" H 4850 10800 50  0001 C CNN
	1    4850 10800
	1    0    0    -1  
$EndComp
$Comp
L Device:C C23
U 1 1 63B4D18B
P 4850 10650
F 0 "C23" H 4900 10750 50  0000 L CNN
F 1 "100n" H 4900 10550 50  0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 4888 10500 50  0001 C CNN
F 3 "~" H 4850 10650 50  0001 C CNN
	1    4850 10650
	1    0    0    -1  
$EndComp
Wire Wire Line
	4500 10450 4850 10450
Wire Wire Line
	4850 10450 4850 10500
Wire Notes Line
	9550 8650 9550 10950
Wire Notes Line
	850  10950 9550 10950
Wire Notes Line
	850  8650 9550 8650
Text GLabel 10100 3500 0    50   Input ~ 0
22
Text GLabel 10100 3600 0    50   Input ~ 0
37
Text GLabel 10100 3700 0    50   Input ~ 0
13
Text GLabel 11700 3800 2    50   Input ~ 0
33
Text GLabel 11700 3700 2    50   Input ~ 0
32
Text GLabel 11700 2800 2    50   Input ~ 0
29
Text GLabel 11700 2700 2    50   Input ~ 0
7
Text GLabel 11700 2900 2    50   Input ~ 0
31
Text GLabel 11700 3100 2    50   Input ~ 0
26
Text GLabel 11700 3200 2    50   Input ~ 0
24
Text GLabel 11700 2100 2    50   Input ~ 0
27
Text GLabel 11700 2200 2    50   Input ~ 0
28
Text GLabel 11000 1500 1    50   Input ~ 0
3V3
Text GLabel 10100 2600 0    50   Input ~ 0
12
Text GLabel 10100 2500 0    50   Input ~ 0
11
Text GLabel 10100 2400 0    50   Input ~ 0
36
Text GLabel 13050 2250 0    50   Input ~ 0
MOSI
Text GLabel 13050 1750 0    50   Input ~ 0
SCLK
Text GLabel 13050 1250 0    50   Input ~ 0
CSB1
Text GLabel 13050 1500 0    50   Input ~ 0
CSB2
Text GLabel 13050 2000 0    50   Input ~ 0
MISO
Wire Wire Line
	13050 1500 13100 1500
Wire Wire Line
	13050 1250 13100 1250
Wire Wire Line
	13050 1750 13100 1750
Wire Wire Line
	13050 2000 13100 2000
Wire Wire Line
	13050 2250 13100 2250
Wire Wire Line
	13100 1750 13100 1700
Wire Wire Line
	13100 1500 13100 1450
Wire Wire Line
	13100 2000 13100 1950
Wire Wire Line
	13100 2250 13100 2200
Wire Wire Line
	13100 1250 13100 1200
Wire Wire Line
	13100 1450 13150 1450
Wire Wire Line
	13150 1450 13150 1600
Wire Wire Line
	13100 1950 13150 1950
Wire Wire Line
	13150 1800 13150 1950
Wire Wire Line
	13200 1900 13200 2200
Wire Wire Line
	13200 2200 13100 2200
Wire Wire Line
	13200 1500 13200 1200
Wire Wire Line
	13200 1200 13100 1200
Wire Wire Line
	12950 3400 13000 3400
Wire Wire Line
	13000 3400 13000 3350
Wire Wire Line
	13000 3350 13250 3350
Text GLabel 12950 3400 0    50   Input ~ 0
I2C1_SDA
Wire Wire Line
	12950 3800 13000 3800
Wire Wire Line
	12950 4300 13000 4300
Wire Wire Line
	12950 4550 13000 4550
Wire Wire Line
	13000 3800 13000 3750
Wire Wire Line
	13000 4300 13000 4250
Wire Wire Line
	13000 4550 13000 4500
Wire Wire Line
	13150 4000 13150 4050
Wire Wire Line
	13150 4050 13350 4050
Wire Wire Line
	13150 4250 13150 4150
Wire Wire Line
	13150 4150 13350 4150
Wire Wire Line
	13000 4250 13150 4250
Wire Wire Line
	13250 4500 13250 4250
Wire Wire Line
	13250 4250 13350 4250
Wire Wire Line
	13000 4500 13250 4500
Wire Wire Line
	13250 3750 13250 3950
Wire Wire Line
	13250 3950 13350 3950
Wire Wire Line
	13000 3750 13250 3750
$Comp
L power:Earth #PWR044
U 1 1 62D0960A
P 12900 4000
F 0 "#PWR044" H 12900 3750 50  0001 C CNN
F 1 "Earth" H 12900 3850 50  0001 C CNN
F 2 "" H 12900 4000 50  0001 C CNN
F 3 "~" H 12900 4000 50  0001 C CNN
	1    12900 4000
	0    1    1    0   
$EndComp
Text GLabel 12950 4300 0    50   Input ~ 0
UART_TX
Text GLabel 12950 4550 0    50   Input ~ 0
UART_RX
Text GLabel 12950 3150 0    50   Input ~ 0
I2C1_SCL
Wire Wire Line
	13050 2850 13150 2850
$Comp
L power:Earth #PWR043
U 1 1 62C94F62
P 13050 2850
F 0 "#PWR043" H 13050 2600 50  0001 C CNN
F 1 "Earth" H 13050 2700 50  0001 C CNN
F 2 "" H 13050 2850 50  0001 C CNN
F 3 "~" H 13050 2850 50  0001 C CNN
	1    13050 2850
	0    1    1    0   
$EndComp
Wire Wire Line
	13000 2600 13250 2600
Wire Wire Line
	13250 2800 13350 2800
Wire Wire Line
	13250 2600 13250 2800
Wire Wire Line
	13250 3100 13350 3100
Wire Wire Line
	13250 3350 13250 3100
Wire Wire Line
	13000 3100 13150 3100
Wire Wire Line
	13150 3000 13350 3000
Wire Wire Line
	13150 3100 13150 3000
Wire Wire Line
	13150 2900 13350 2900
Wire Wire Line
	13150 2850 13150 2900
Wire Wire Line
	13000 3150 13000 3100
Wire Wire Line
	13000 2650 13000 2600
Wire Wire Line
	12950 3150 13000 3150
Wire Wire Line
	12950 2650 13000 2650
Wire Wire Line
	12900 4000 13150 4000
Text GLabel 10100 3200 0    50   Input ~ 0
15
Text GLabel 15200 1400 2    50   Input ~ 0
12
Text GLabel 14600 1500 0    50   Input ~ 0
11
Text GLabel 15200 2000 2    50   Input ~ 0
36
Text GLabel 14600 2200 0    50   Input ~ 0
33
Text GLabel 15200 1900 2    50   Input ~ 0
32
Text GLabel 14600 1700 0    50   Input ~ 0
15
Text GLabel 15200 1500 2    50   Input ~ 0
22
Text GLabel 14600 2300 0    50   Input ~ 0
37
Text GLabel 14600 1600 0    50   Input ~ 0
13
Text GLabel 15200 1700 2    50   Input ~ 0
26
Text GLabel 15200 1600 2    50   Input ~ 0
24
Text GLabel 14600 1900 0    50   Input ~ 0
29
Text GLabel 14600 1400 0    50   Input ~ 0
7
Text GLabel 14600 2000 0    50   Input ~ 0
31
Text GLabel 14600 1800 0    50   Input ~ 0
27
Text GLabel 15200 1800 2    50   Input ~ 0
28
$Comp
L RPI~hat~library:2.54mm_header_1_x_4 H3
U 1 1 64446273
P 13450 4100
F 0 "H3" H 13678 4151 50  0000 L CNN
F 1 "UART" H 13678 4060 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 13678 4014 50  0001 L CNN
F 3 "" H 13450 4350 50  0001 C CNN
	1    13450 4100
	1    0    0    -1  
$EndComp
Wire Wire Line
	13300 1500 13200 1500
Wire Wire Line
	13300 1900 13200 1900
Wire Wire Line
	13150 1800 13300 1800
Wire Wire Line
	13150 1600 13300 1600
$Comp
L RPI~hat~library:2.54mm_header_1_x_4 H2
U 1 1 644661B2
P 13450 2950
F 0 "H2" H 13678 3001 50  0000 L CNN
F 1 "I2C" H 13678 2910 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 13678 2864 50  0001 L CNN
F 3 "" H 13450 3200 50  0001 C CNN
	1    13450 2950
	1    0    0    -1  
$EndComp
$Comp
L RPI~hat~library:2.54mm_header_1_x_5 H1
U 1 1 644E7052
P 13400 1650
F 0 "H1" H 13628 1651 50  0000 L CNN
F 1 "SPI" H 13628 1560 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x05_P2.54mm_Vertical" H 13450 2250 50  0001 C CNN
F 3 "" H 13450 2250 50  0001 C CNN
	1    13400 1650
	1    0    0    -1  
$EndComp
Wire Notes Line
	15650 900  15650 4650
Wire Notes Line
	15650 4650 9400 4650
Wire Notes Line
	9400 4650 9400 900 
Wire Notes Line
	9400 900  15650 900 
$Comp
L RPI~hat~library:ADS1293 U2
U 1 1 646D031F
P 2800 5650
F 0 "U2" H 2450 6200 50  0000 C CNN
F 1 "ADS1293" H 2550 3200 50  0000 C CNN
F 2 "RasperryPi ECG Hat:WQFN 28" H 2400 6200 50  0001 C CNN
F 3 "" H 2400 6200 50  0001 C CNN
	1    2800 5650
	1    0    0    -1  
$EndComp
$Comp
L RPI~hat~library:2.54mm_header_1_x_4 H5
U 1 1 6470F3F1
P 6650 7500
F 0 "H5" H 6650 7750 50  0000 L CNN
F 1 "ECG Control" H 6650 7250 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 6878 7414 50  0001 L CNN
F 3 "" H 6650 7750 50  0001 C CNN
	1    6650 7500
	1    0    0    -1  
$EndComp
$Comp
L RPI~hat~library:ADS1241 U5
U 1 1 6472F6F9
P 3150 9900
F 0 "U5" H 2800 10500 50  0000 C CNN
F 1 "ADS1241" H 2900 8900 50  0000 C CNN
F 2 "Package_SO:SSOP-28_5.3x10.2mm_P0.65mm" H 2800 10550 50  0001 C CNN
F 3 "" H 2800 10550 50  0001 C CNN
	1    3150 9900
	1    0    0    -1  
$EndComp
$Comp
L RPI~hat~library:2.54mm_header_1x6 H6
U 1 1 6474FC90
P 7150 9800
F 0 "H6" H 7100 10150 50  0000 L CNN
F 1 "ADC Control" H 7100 9450 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical" H 7100 10150 50  0001 C CNN
F 3 "" H 7100 10150 50  0001 C CNN
	1    7150 9800
	1    0    0    -1  
$EndComp
$Comp
L power:Earth #PWR040
U 1 1 6236EC8E
P 9100 9950
F 0 "#PWR040" H 9100 9700 50  0001 C CNN
F 1 "Earth" H 9100 9800 50  0001 C CNN
F 2 "" H 9100 9950 50  0001 C CNN
F 3 "~" H 9100 9950 50  0001 C CNN
	1    9100 9950
	0    -1   -1   0   
$EndComp
$Comp
L RPI~hat~library:2.54mm_header_2x12 H7
U 1 1 64770BDE
P 8800 9500
F 0 "H7" H 8650 9850 50  0000 C CNN
F 1 "ADC Input" H 8750 8550 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x12_P2.54mm_Vertical" H 8650 9850 50  0001 C CNN
F 3 "" H 8650 9850 50  0001 C CNN
	1    8800 9500
	1    0    0    -1  
$EndComp
$Comp
L RPI~hat~library:2.54mm_header_1x6 H8
U 1 1 64803B47
P 6400 5550
F 0 "H8" H 6350 5900 50  0000 L CNN
F 1 "ECG Input" H 6350 5200 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical" H 6350 5900 50  0001 C CNN
F 3 "" H 6350 5900 50  0001 C CNN
	1    6400 5550
	1    0    0    -1  
$EndComp
Text GLabel 6250 5800 0    50   Input ~ 0
IN6
Text GLabel 6250 5700 0    50   Input ~ 0
IN5
Text GLabel 6250 5300 0    50   Input ~ 0
IN1
Text GLabel 6250 5400 0    50   Input ~ 0
IN2
Text GLabel 6250 5500 0    50   Input ~ 0
IN3
Text GLabel 6250 5600 0    50   Input ~ 0
IN4
Wire Wire Line
	13300 1700 13100 1700
Text GLabel 10100 2800 0    50   Input ~ 0
35
Text GLabel 10100 2900 0    50   Input ~ 0
38
Text GLabel 10100 3000 0    50   Input ~ 0
40
Text GLabel 14600 2100 0    50   Input ~ 0
35
Text GLabel 15200 2100 2    50   Input ~ 0
38
Text GLabel 15200 2200 2    50   Input ~ 0
40
$Comp
L RPI~hat~library:2.54mm_header_2x12 H4
U 1 1 64944DD7
P 14900 1650
F 0 "H4" H 14750 2000 50  0000 C CNN
F 1 "Extra pins" H 14900 700 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x12_P2.54mm_Vertical" H 14750 2000 50  0001 C CNN
F 3 "" H 14750 2000 50  0001 C CNN
	1    14900 1650
	1    0    0    -1  
$EndComp
Text GLabel 15200 2500 2    50   Input ~ 0
3V3
$Comp
L power:Earth #PWR046
U 1 1 64A67DD2
P 14500 2500
F 0 "#PWR046" H 14500 2250 50  0001 C CNN
F 1 "Earth" H 14500 2350 50  0001 C CNN
F 2 "" H 14500 2500 50  0001 C CNN
F 3 "~" H 14500 2500 50  0001 C CNN
	1    14500 2500
	1    0    0    -1  
$EndComp
Wire Wire Line
	14600 2500 14500 2500
Wire Wire Line
	14500 2500 14500 2400
Wire Wire Line
	14500 2400 14600 2400
Connection ~ 14500 2500
Wire Wire Line
	2400 2200 2250 2200
Connection ~ 2250 2200
$Comp
L RPI~hat~library:LED D1
U 1 1 64C6920B
P 4100 850
F 0 "D1" V 4139 732 50  0000 R CNN
F 1 "LED" V 4048 732 50  0000 R CNN
F 2 "RasperryPi ECG Hat:LED" H 4100 850 50  0001 C CNN
F 3 "~" H 4100 850 50  0001 C CNN
	1    4100 850 
	0    -1   -1   0   
$EndComp
$Comp
L RPI~hat~library:LED D2
U 1 1 64C6A649
P 4100 2200
F 0 "D2" V 4139 2082 50  0000 R CNN
F 1 "LED" V 4048 2082 50  0000 R CNN
F 2 "RasperryPi ECG Hat:LED" H 4100 2200 50  0001 C CNN
F 3 "~" H 4100 2200 50  0001 C CNN
	1    4100 2200
	0    -1   -1   0   
$EndComp
$Comp
L RPI~hat~library:LED D3
U 1 1 64C6BDDA
P 4100 3350
F 0 "D3" V 4139 3232 50  0000 R CNN
F 1 "LED" V 4048 3232 50  0000 R CNN
F 2 "RasperryPi ECG Hat:LED" H 4100 3350 50  0001 C CNN
F 3 "~" H 4100 3350 50  0001 C CNN
	1    4100 3350
	0    -1   -1   0   
$EndComp
Wire Wire Line
	4100 3400 4100 3500
Connection ~ 4100 3500
Wire Wire Line
	4100 3500 4100 3550
Wire Wire Line
	4100 2400 4100 2350
Connection ~ 4100 2350
Wire Wire Line
	4100 1150 4100 1100
Wire Wire Line
	4100 1000 4100 1100
Connection ~ 4100 1100
Wire Wire Line
	4100 650  4100 700 
Text GLabel 1200 1200 0    50   Input ~ 0
5V
Text GLabel 1200 2200 0    50   Input ~ 0
5V
Text GLabel 1250 3400 0    50   Input ~ 0
5V
Text GLabel 12950 3800 0    50   Input ~ 0
5V
Text GLabel 12950 2650 0    50   Input ~ 0
5V
Text GLabel 15200 2400 2    50   Input ~ 0
5V
Text GLabel 15200 2300 2    50   Input ~ 0
5V
Text GLabel 1350 7100 1    50   Input ~ 0
ECG_3v3
Text GLabel 5050 7250 2    50   Input ~ 0
ECG_3v3
Text GLabel 9100 9250 2    50   Input ~ 0
Strain_3v3
Text GLabel 9100 9550 2    50   Input ~ 0
Strain_3v3
Text GLabel 9100 9850 2    50   Input ~ 0
Strain_3v3
Text GLabel 9100 10150 2    50   Input ~ 0
Strain_3v3
Text GLabel 8500 10350 0    50   Input ~ 0
Strain_3v3
Text GLabel 8500 10050 0    50   Input ~ 0
Strain_3v3
Text GLabel 8500 9750 0    50   Input ~ 0
Strain_3v3
Text GLabel 8500 9450 0    50   Input ~ 0
Strain_3v3
$Comp
L Device:C C24
U 1 1 65621CD6
P 4150 10100
F 0 "C24" H 4200 10200 50  0000 L CNN
F 1 "100n" H 4200 10000 50  0000 L CNN
F 2 "Capacitor_SMD:C_0402_1005Metric" H 4188 9950 50  0001 C CNN
F 3 "~" H 4150 10100 50  0001 C CNN
	1    4150 10100
	1    0    0    -1  
$EndComp
Connection ~ 4150 10250
Wire Wire Line
	4000 10150 4000 10000
Wire Wire Line
	4000 10000 4150 10000
Wire Wire Line
	3650 10150 4000 10150
Wire Wire Line
	4150 10000 4150 9950
Wire Wire Line
	5700 9550 5900 9550
Wire Wire Line
	11000 1500 11000 1700
NoConn ~ 11100 1700
$Comp
L power:Earth #PWR?
U 1 1 65D12DE3
P 2800 8150
F 0 "#PWR?" H 2800 7900 50  0001 C CNN
F 1 "Earth" H 2800 8000 50  0001 C CNN
F 2 "" H 2800 8150 50  0001 C CNN
F 3 "~" H 2800 8150 50  0001 C CNN
	1    2800 8150
	1    0    0    -1  
$EndComp
$EndSCHEMATC
