import ThemeVariables from 'common/variables'

export const MultiIMUGraphData = {
  rightArmGraphs: [
    {
      id: 'imu_split_1',
      label: 'Right Arm 1',
      min: -6,
      max: 6,
      refreshRate: 20,
      duration: 2000,
      dataSets: [
        {
          label: 'Right Shoulder - x',
          color: ThemeVariables.colours.success,
          dataValue: 'ax',
        },
        {
          label: 'Right Shoulder - y',
          color: ThemeVariables.colours.primary,
          dataValue: 'ay',
        },
        {
          label: 'Right Shoulder - z',
          color: ThemeVariables.colours.warn,
          dataValue: 'az',
        }
      ]
    },
    {
      id: 'imu_split_2',
      label: 'Right Arm 2',
      min: -6,
      max: 6,
      refreshRate: 20,
      duration: 2000,
      dataSets: [
        {
          label: 'Right Upper Arm - x',
          color: ThemeVariables.colours.success,
          dataValue: 'ax',
        },
        {
          label: 'Right Upper Arm - y',
          color: ThemeVariables.colours.primary,
          dataValue: 'ay',
        },
        {
          label: 'Right Upper Arm - z',
          color: ThemeVariables.colours.warn,
          dataValue: 'az',
        }
      ]
    },
    {
      id: 'imu_split_3',
      label: 'Right Arm 3',
      min: -6,
      max: 6,
      refreshRate: 20,
      duration: 2000,
      dataSets: [
        {
          label: 'Right Lower Arm - x',
          color: ThemeVariables.colours.success,
          dataValue: 'ax',
        },
        {
          label: 'Right Lower Arm - y',
          color: ThemeVariables.colours.primary,
          dataValue: 'ay',
        },
        {
          label: 'Right Lower Arm - z',
          color: ThemeVariables.colours.warn,
          dataValue: 'az',
        }
      ]
    },
  ],
  leftArmGraphs: [
    {
      id: 'imu_split_5',
      label: 'Left Arm 1',
      min: -6,
      max: 6,
      refreshRate: 200,
      duration: 2000,
      dataSets: [
        {
          label: 'Left Shoulder - x',
          color: ThemeVariables.colours.success,
          dataValue: 'ax',
        },
        {
          label: 'Left Shoulder - y',
          color: ThemeVariables.colours.primary,
          dataValue: 'ay',
        },
        {
          label: 'Left Shoulder - z',
          color: ThemeVariables.colours.warn,
          dataValue: 'az',
        }
      ]
    },
    {
      id: 'imu_split_6',
      label: 'Left Arm 2',
      min: -6,
      max: 6,
      refreshRate: 20,
      duration: 2000,
      dataSets: [
        {
          label: 'Left Upper Arm - x',
          color: ThemeVariables.colours.success,
          dataValue: 'ax',
        },
        {
          label: 'Left Upper Arm - y',
          color: ThemeVariables.colours.primary,
          dataValue: 'ay',
        },
        {
          label: 'Left Upper Arm - z',
          color: ThemeVariables.colours.warn,
          dataValue: 'az',
        }
      ]
    },
    {
      id: 'imu_split_7',
      label: 'Left Arm 3',
      min: -6,
      max: 6,
      refreshRate: 20,
      duration: 2000,
      dataSets: [
        {
          label: 'Left Lower Arm - x',
          color: ThemeVariables.colours.success,
          dataValue: 'ax',
        },
        {
          label: 'Left Lower Arm - y',
          color: ThemeVariables.colours.primary,
          dataValue: 'ay',
        },
        {
          label: 'Left Lower Arm - z',
          color: ThemeVariables.colours.warn,
          dataValue: 'az',
        }
      ]
    },
  ],
  rightLegGraphs: [
    {
      id: 'imu_split_8',
      label: 'Right Leg 1',
      min: -6,
      max: 6,
      refreshRate: 20,
      duration: 2000,
      dataSets: [
        {
          label: 'Lower Back - x',
          color: ThemeVariables.colours.success,
          dataValue: 'ax',
        },
        {
          label: 'Lower Back - y',
          color: ThemeVariables.colours.primary,
          dataValue: 'ay',
        },
        {
          label: 'Lower Back - z',
          color: ThemeVariables.colours.warn,
          dataValue: 'az',
        }
      ]
    },
    {
      id: 'imu_split_9',
      label: 'Right Leg 2',
      min: -6,
      max: 6,
      refreshRate: 20,
      duration: 2000,
      dataSets: [
        {
          label: 'Right Upper Leg - x',
          color: ThemeVariables.colours.success,
          dataValue: 'ax',
        },
        {
          label: 'Right Upper Leg - y',
          color: ThemeVariables.colours.primary,
          dataValue: 'ay',
        },
        {
          label: 'Right Upper Leg - z',
          color: ThemeVariables.colours.warn,
          dataValue: 'az',
        }
      ]
    },
    {
      id: 'imu_split_10',
      label: 'Right Leg 3',
      min: -6,
      max: 6,
      refreshRate: 20,
      duration: 2000,
      dataSets: [
        {
          label: 'Right Lower Leg - x',
          color: ThemeVariables.colours.success,
          dataValue: 'ax',
        },
        {
          label: 'Right Lower Leg - y',
          color: ThemeVariables.colours.primary,
          dataValue: 'ay',
        },
        {
          label: 'Right Lower Leg - z',
          color: ThemeVariables.colours.warn,
          dataValue: 'az',
        }
      ]
    },
  ],
  leftLegGraphs: [
    {
      id: 'imu_split_12',
      label: 'Left Leg 1',
      min: -6,
      max: 6,
      refreshRate: 20,
      duration: 2000,
      dataSets: [
        {
          label: 'Lower Back - x',
          color: ThemeVariables.colours.success,
          dataValue: 'ax',
        },
        {
          label: 'Lower Back - y',
          color: ThemeVariables.colours.primary,
          dataValue: 'ay',
        },
        {
          label: 'Lower Back - z',
          color: ThemeVariables.colours.warn,
          dataValue: 'az',
        }
      ]
    },
    {
      id: 'imu_split_13',
      label: 'Left Leg 2',
      min: -6,
      max: 6,
      refreshRate: 20,
      duration: 2000,
      dataSets: [
        {
          label: 'Left Upper Leg - x',
          color: ThemeVariables.colours.success,
          dataValue: 'ax',
        },
        {
          label: 'Left Upper Leg - y',
          color: ThemeVariables.colours.primary,
          dataValue: 'ay',
        },
        {
          label: 'Left Upper Leg - z',
          color: ThemeVariables.colours.warn,
          dataValue: 'az',
        }
      ]
    },
    {
      id: 'imu_split_14',
      label: 'Left Leg 3',
      min: -6,
      max: 6,
      refreshRate: 20,
      duration: 2000,
      dataSets: [
        {
          label: 'Left Lower Leg - x',
          color: ThemeVariables.colours.success,
          dataValue: 'ax',
        },
        {
          label: ' Left Lower Leg - y',
          color: ThemeVariables.colours.primary,
          dataValue: 'ay',
        },
        {
          label: 'Left Lower Leg - z',
          color: ThemeVariables.colours.warn,
          dataValue: 'az',
        }
      ]
    },
  ],
  torsoGraphs: [
    {
      id: 'imu_split_4',
      label: 'Torso 1',
      min: -6,
      max: 6,
      refreshRate: 20,
      duration: 2000,
      dataSets: [
        {
          label: 'Torso 1 X',
          color: ThemeVariables.colours.success,
          dataValue: 'ax',
        },
        {
          label: 'Torso 1 Y',
          color: ThemeVariables.colours.primary,
          dataValue: 'ay',
        },
        {
          label: 'Torso 1 Z',
          color: ThemeVariables.colours.warn,
          dataValue: 'az',
        }
      ]
    },
    {
      id: 'imu_split_11',
      label: 'Torso 2',
      min: -6,
      max: 6,
      refreshRate: 20,
      duration: 2000,
      dataSets: [
        {
          label: 'Torso 2 X',
          color: ThemeVariables.colours.success,
          dataValue: 'ax',
        },
        {
          label: 'Torso 2 Y',
          color: ThemeVariables.colours.primary,
          dataValue: 'ay',
        },
        {
          label: 'Torso 2 Z',
          color: ThemeVariables.colours.warn,
          dataValue: 'az',
        }
      ]
    },
  ]
}
