import ThemeVariables from 'common/variables'

export const PPGGraphModel = [
  {
    id: 'ppg_split_1',
    label: 'PPG 1',
    min: -6,
    max: 6,
    refreshRate: 20,
    duration: 5000,
    dataSets: [
      {
        label: 'PPG 1',
        color: ThemeVariables.colours.success,
        dataValue: 'ppg',
      },
    ]
  },
  {
    id: 'ppg_split_2',
    label: 'PPG 2',
    min: -6,
    max: 6,
    refreshRate: 20,
    duration: 5000,
    dataSets: [
      {
        label: 'PPG 2',
        color: ThemeVariables.colours.secondary,
        dataValue: 'ppg',
      },
    ]
  },
  {
    id: 'ppg_split_3',
    label: 'PPG 3',
    min: -6,
    max: 6,
    refreshRate: 20,
    duration: 5000,
    dataSets: [
      {
        label: 'PPG 3',
        color: ThemeVariables.colours.darkBlue,
        dataValue: 'ppg',
      },
    ]
  },
]