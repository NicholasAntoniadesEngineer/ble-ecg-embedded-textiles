#ifndef BMI160REG_H
#define	BMI160REG_H

/********** Define for magnetometer *************/
#define BMI160_MAG_PMU_STATUS_BIT   0     //Added for BMM150 Support
#define BMI160_MAG_PMU_STATUS_LEN   2     //Added for BMM150 Support

#define BMI160_STATUS_DRDY_MAG      5     //Added for BMM150 Support
#define BMI160_STATUS_MAG_MAN_OP    2     //Added for BMM150 Support
#define BMI160_MAG_RATE_SEL_BIT     0     //Added for BMM150 Support
#define BMI160_MAG_RATE_SEL_LEN     4     //Added for BMM150 Support
#define BMI160_FIFO_MAG_EN_BIT      5     //Added for BMM150 Support

#define BMI160_MAG_IF_0             0x4B  //Added for BMM150 Support
#define BMI160_MAG_IF_1             0x4C  //Added for BMM150 Support
#define BMI160_MAG_IF_2             0x4D  //Added for BMM150 Support
#define BMI160_MAG_IF_3             0x4E  //Added for BMM150 Support
#define BMI160_MAG_IF_4             0x4F  //Added for BMM150 Support

#define BMM150_EN_SLEEP_MODE        0x01  //Added for BMM150 Support
#define BMM150_XY_REPETITIONS       0x04  //Added for BMM150 Support
#define BMM150_Z_REPETITIONS        0x0E  //Added for BMM150 Support

#define BMM150_DATA_REG             0x42  //Added for BMM150 Support
#define BMM150_POWER_REG            0x4B  //Added for BMM150 Support
#define BMM150_OPMODE_REG           0x4C  //Added for BMM150 Support
#define BMM150_XY_REP_REG           0x51  //Added for BMM150 Support
#define BMM150_Z_REP_REG            0x52  //Added for BMM150 Support

//Based I2C addr is 0x20 caused it is 0x10 plus one 0 at the end.
#define BMM150_BASED_I2C_ADDR       0x20  //Added for BMM150 Support
#define BMI160_MAG_MAN_EN           0x83  //Added for BMM150 Support
#define BMI160_MAG_MAN_DIS          0x03  //Added for BMM150 Support
#define BMI160_MAG_CONF_25Hz        0x06  //Added for BMM150 Support

#define BMM150_POWER_REG_DEFAULT    0x01  //Added for BMM150 Support
#define BMM150_OPMODE_REG_DEFAULT   0x02  //Added for BMM150 Support
#define BMM150_OPMODE_REG_P         0x06  //Added for BMM150 Support
#define BMM150_R_DATA_ADDR          0x42  //Added for BMM150 Support

#define BMI160_FOC_CONF_DEFAULT     0x40  //Added for BMM150 Support

#define BMI160_IF_CONF              0x6B  //Added for BMM150 Support

#define BMI160_2ND_INT_MAG          0x20  //Added for BMM150 Support

#define BMI160_EN_PULL_UP_REG_1     0x37  //Added for BMM150 Support
#define BMI160_EN_PULL_UP_REG_2     0x9A  //Added for BMM150 Support
#define BMI160_EN_PULL_UP_REG_3     0xC0  //Added for BMM150 Support
#define BMI160_EN_PULL_UP_REG_4     0x90  //Added for BMM150 Support
#define BMI160_EN_PULL_UP_REG_5     0x80  //Added for BMM150 Support

#define BMI160_7F                   0x7F  //Added for BMM150 Support

#define BMI160_CMD_MAG_MODE_NORMAL  0x19  //Added for BMM150 Support

#define BMI160_RA_MAG_X_L           0x04  //Added for BMM150 Support
#define BMI160_RA_MAG_X_H           0x05  //Added for BMM150 Support
#define BMI160_RA_MAG_Y_L           0x06  //Added for BMM150 Support
#define BMI160_RA_MAG_Y_H           0x07  //Added for BMM150 Support
#define BMI160_RA_MAG_Z_L           0x08  //Added for BMM150 Support
#define BMI160_RA_MAG_Z_H           0x09  //Added for BMM150 Support

#define BMI160_RA_MAG_CONF          0X44  //Added for BMM150 Support

/**************************/

#define BMI160_CHIP_ID 0xd1

#define BMI160_SPI_READ_BIT         7

#define BMI160_RA_CHIP_ID           0x00

#define BMI160_ACC_PMU_STATUS_BIT   4
#define BMI160_ACC_PMU_STATUS_LEN   2
#define BMI160_GYR_PMU_STATUS_BIT   2
#define BMI160_GYR_PMU_STATUS_LEN   2

#define BMI160_RA_PMU_STATUS        0x03

#define BMI160_RA_GYRO_X_L          0x0C
#define BMI160_RA_GYRO_X_H          0x0D
#define BMI160_RA_GYRO_Y_L          0x0E
#define BMI160_RA_GYRO_Y_H          0x0F
#define BMI160_RA_GYRO_Z_L          0x10
#define BMI160_RA_GYRO_Z_H          0x11
#define BMI160_RA_ACCEL_X_L         0x12
#define BMI160_RA_ACCEL_X_H         0x13
#define BMI160_RA_ACCEL_Y_L         0x14
#define BMI160_RA_ACCEL_Y_H         0x15
#define BMI160_RA_ACCEL_Z_L         0x16
#define BMI160_RA_ACCEL_Z_H         0x17

#define BMI160_STATUS_FOC_RDY       3
#define BMI160_STATUS_NVM_RDY       4
#define BMI160_STATUS_DRDY_GYR      6
#define BMI160_STATUS_DRDY_ACC      7

#define BMI160_RA_STATUS            0x1B

#define BMI160_STEP_INT_BIT         0
#define BMI160_ANYMOTION_INT_BIT    2
#define BMI160_D_TAP_INT_BIT        4
#define BMI160_S_TAP_INT_BIT        5
#define BMI160_NOMOTION_INT_BIT     7
#define BMI160_FFULL_INT_BIT        5
#define BMI160_DRDY_INT_BIT         4
#define BMI160_LOW_G_INT_BIT        3
#define BMI160_HIGH_G_INT_BIT       2

#define BMI160_TAP_SIGN_BIT         7
#define BMI160_TAP_1ST_Z_BIT        6
#define BMI160_TAP_1ST_Y_BIT        5
#define BMI160_TAP_1ST_X_BIT        4

#define BMI160_ANYMOTION_SIGN_BIT   3
#define BMI160_ANYMOTION_1ST_Z_BIT  2
#define BMI160_ANYMOTION_1ST_Y_BIT  1
#define BMI160_ANYMOTION_1ST_X_BIT  0

#define BMI160_HIGH_G_SIGN_BIT      3
#define BMI160_HIGH_G_1ST_Z_BIT     2
#define BMI160_HIGH_G_1ST_Y_BIT     1
#define BMI160_HIGH_G_1ST_X_BIT     0

#define BMI160_RA_INT_STATUS_0      0x1C
#define BMI160_RA_INT_STATUS_1      0x1D
#define BMI160_RA_INT_STATUS_2      0x1E
#define BMI160_RA_INT_STATUS_3      0x1F

#define BMI160_RA_TEMP_L            0x20
#define BMI160_RA_TEMP_H            0x21

#define BMI160_RA_FIFO_LENGTH_0     0x22
#define BMI160_RA_FIFO_LENGTH_1     0x23

#define BMI160_FIFO_DATA_INVALID    0x80
#define BMI160_RA_FIFO_DATA         0x24

#define BMI160_ACCEL_RATE_SEL_BIT    0
#define BMI160_ACCEL_RATE_SEL_LEN    4

#define BMI160_RA_ACCEL_CONF        0X40
#define BMI160_RA_ACCEL_RANGE       0X41

#define BMI160_GYRO_RATE_SEL_BIT    0
#define BMI160_GYRO_RATE_SEL_LEN    4

#define BMI160_RA_GYRO_CONF         0X42
#define BMI160_RA_GYRO_RANGE        0X43

#define BMI160_FIFO_HEADER_EN_BIT   4
#define BMI160_FIFO_ACC_EN_BIT      6
#define BMI160_FIFO_GYR_EN_BIT      7

#define BMI160_RA_FIFO_CONFIG_0     0x46
#define BMI160_RA_FIFO_CONFIG_1     0x47

#define BMI160_ANYMOTION_EN_BIT     0
#define BMI160_ANYMOTION_EN_LEN     3
#define BMI160_D_TAP_EN_BIT         4
#define BMI160_S_TAP_EN_BIT         5
#define BMI160_NOMOTION_EN_BIT      0
#define BMI160_NOMOTION_EN_LEN      3
#define BMI160_LOW_G_EN_BIT         3
#define BMI160_LOW_G_EN_LEN         1
#define BMI160_HIGH_G_EN_BIT        0
#define BMI160_HIGH_G_EN_LEN        3

#define BMI160_STEP_EN_BIT          3
#define BMI160_DRDY_EN_BIT          4
#define BMI160_FFULL_EN_BIT         5

#define BMI160_RA_INT_EN_0          0x50
#define BMI160_RA_INT_EN_1          0x51
#define BMI160_RA_INT_EN_2          0x52

#define BMI160_INT1_EDGE_CTRL       0
#define BMI160_INT1_LVL             1
#define BMI160_INT1_OD              2
#define BMI160_INT1_OUTPUT_EN       3

#define BMI160_RA_INT_OUT_CTRL      0x53

#define BMI160_LATCH_MODE_BIT       0
#define BMI160_LATCH_MODE_LEN       4

#define BMI160_RA_INT_LATCH         0x54
#define BMI160_RA_INT_MAP_0         0x55
#define BMI160_RA_INT_MAP_1         0x56
#define BMI160_RA_INT_MAP_2         0x57

#define BMI160_ANYMOTION_DUR_BIT    0
#define BMI160_ANYMOTION_DUR_LEN    2
#define BMI160_NOMOTION_DUR_BIT     2
#define BMI160_NOMOTION_DUR_LEN     6

#define BMI160_NOMOTION_SEL_BIT     0
#define BMI160_NOMOTION_SEL_LEN     1

#define BMI160_RA_INT_LOWHIGH_0     0x5A
#define BMI160_RA_INT_LOWHIGH_1     0x5B
#define BMI160_RA_INT_LOWHIGH_2     0x5C
#define BMI160_RA_INT_LOWHIGH_3     0x5D
#define BMI160_RA_INT_LOWHIGH_4     0x5E

#define BMI160_RA_INT_MOTION_0      0x5F
#define BMI160_RA_INT_MOTION_1      0x60
#define BMI160_RA_INT_MOTION_2      0x61
#define BMI160_RA_INT_MOTION_3      0x62

#define BMI160_TAP_DUR_BIT          0
#define BMI160_TAP_DUR_LEN          3
#define BMI160_TAP_SHOCK_BIT        6
#define BMI160_TAP_QUIET_BIT        7
#define BMI160_TAP_THRESH_BIT       0
#define BMI160_TAP_THRESH_LEN       5

#define BMI160_RA_INT_TAP_0         0x63
#define BMI160_RA_INT_TAP_1         0x64

#define BMI160_FOC_ACC_Z_BIT        0
#define BMI160_FOC_ACC_Z_LEN        2
#define BMI160_FOC_ACC_Y_BIT        2
#define BMI160_FOC_ACC_Y_LEN        2
#define BMI160_FOC_ACC_X_BIT        4
#define BMI160_FOC_ACC_X_LEN        2
#define BMI160_FOC_GYR_EN           6

#define BMI160_RA_FOC_CONF          0x69

#define BMI160_GYR_OFFSET_X_MSB_BIT 0
#define BMI160_GYR_OFFSET_X_MSB_LEN 2
#define BMI160_GYR_OFFSET_Y_MSB_BIT 2
#define BMI160_GYR_OFFSET_Y_MSB_LEN 2
#define BMI160_GYR_OFFSET_Z_MSB_BIT 4
#define BMI160_GYR_OFFSET_Z_MSB_LEN 2
#define BMI160_ACC_OFFSET_EN        6
#define BMI160_GYR_OFFSET_EN        7

#define BMI160_RA_OFFSET_0          0x71
#define BMI160_RA_OFFSET_1          0x72
#define BMI160_RA_OFFSET_2          0x73
#define BMI160_RA_OFFSET_3          0x74
#define BMI160_RA_OFFSET_4          0x75
#define BMI160_RA_OFFSET_5          0x76
#define BMI160_RA_OFFSET_6          0x77

#define BMI160_RA_STEP_CNT_L        0x78
#define BMI160_RA_STEP_CNT_H        0x79

#define BMI160_STEP_BUF_MIN_BIT     0
#define BMI160_STEP_BUF_MIN_LEN     3
#define BMI160_STEP_CNT_EN_BIT      3

#define BMI160_STEP_TIME_MIN_BIT    0
#define BMI160_STEP_TIME_MIN_LEN    3
#define BMI160_STEP_THRESH_MIN_BIT  3
#define BMI160_STEP_THRESH_MIN_LEN  2
#define BMI160_STEP_ALPHA_BIT       5
#define BMI160_STEP_ALPHA_LEN       3

#define BMI160_RA_STEP_CONF_0       0x7A
#define BMI160_RA_STEP_CONF_1       0x7B

#define BMI160_RA_STEP_CONF_0_NOR   0x15
#define BMI160_RA_STEP_CONF_0_SEN   0x2D
#define BMI160_RA_STEP_CONF_0_ROB   0x1D
#define BMI160_RA_STEP_CONF_1_NOR   0x03
#define BMI160_RA_STEP_CONF_1_SEN   0x00
#define BMI160_RA_STEP_CONF_1_ROB   0x07


#define BMI160_GYRO_RANGE_SEL_BIT   0
#define BMI160_GYRO_RANGE_SEL_LEN   3

#define BMI160_GYRO_RATE_SEL_BIT    0
#define BMI160_GYRO_RATE_SEL_LEN    4

#define BMI160_GYRO_DLPF_SEL_BIT    4
#define BMI160_GYRO_DLPF_SEL_LEN    2

#define BMI160_ACCEL_DLPF_SEL_BIT   4
#define BMI160_ACCEL_DLPF_SEL_LEN   3

#define BMI160_ACCEL_RANGE_SEL_BIT  0
#define BMI160_ACCEL_RANGE_SEL_LEN  4

#define BMI160_CMD_START_FOC        0x03
#define BMI160_CMD_ACC_MODE_NORMAL  0x11
#define BMI160_CMD_GYR_MODE_NORMAL  0x15
#define BMI160_CMD_FIFO_FLUSH       0xB0
#define BMI160_CMD_INT_RESET        0xB1
#define BMI160_CMD_STEP_CNT_CLR     0xB2
#define BMI160_CMD_SOFT_RESET       0xB6

#define BMI160_RA_CMD               0x7E
#endif

