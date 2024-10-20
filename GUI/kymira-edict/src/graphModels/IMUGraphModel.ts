import ThemeVariables from 'common/variables'

export const IMUGraphsModel = [
  {
    id: 'imu_split_1',
    label: 'IMU 1',
    min: -6,
    max: 6,
    refreshRate: 20,
    duration: 2000,
    dataSets: [
      {
        label: 'X',
        color: ThemeVariables.colours.success,
        dataValue: 'ax',
      },
      {
        label: 'Y',
        color: ThemeVariables.colours.primary,
        dataValue: 'ay',
      },
      {
        label: 'Z',
        color: ThemeVariables.colours.warn,
        dataValue: 'az',
      }
    ]
  },
]