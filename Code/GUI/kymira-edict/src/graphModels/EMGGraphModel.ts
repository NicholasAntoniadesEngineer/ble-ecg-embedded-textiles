import ThemeVariables from 'common/variables'

export const EMGGraphModel = [
  {
    id: 'emg_split_1',
    label: 'EMG 1',
    refreshRate: 100,
    duration: 5000,
    dataSets: [
      {
        label: 'EMG 1',
        color: ThemeVariables.colours.success,
        dataValue: 'emg',
      },
    ]
  },
  {
    id: 'emg_split_2',
    label: 'EMG 2',
    refreshRate: 100,
    duration: 5000,
    min: -0.0020,
    max: 0.0020,
    dataSets: [
      {
        label: 'EMG 2',
        color: ThemeVariables.colours.secondary,
        dataValue: 'emg',
      },
    ]
  },
  {
    id: 'emg_split_3',
    label: 'EMG 3',
    refreshRate: 100,
    duration: 5000,
    min: -0.0020,
    max: 0.0020,
    dataSets: [
      {
        label: 'EMG 3',
        color: ThemeVariables.colours.darkBlue,
        dataValue: 'emg',
      },
    ]
  },
]