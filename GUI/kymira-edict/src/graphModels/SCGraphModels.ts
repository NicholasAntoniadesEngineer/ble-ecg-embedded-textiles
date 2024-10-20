import ThemeVariables from 'common/variables'

export const SGGraphModels = [
  {
    id: 'sg_split_1',
    label: 'SG 1',
    min: -6,
    max: 6,
    refreshRate: 20,
    duration: 5000,
    dataSets: [
      {
        label: 'SG 1',
        color: ThemeVariables.colours.success,
        dataValue: 'sg',
      },
    ]
  },
  {
    id: 'sg_split_2',
    label: 'SG 2',
    min: -6,
    max: 6,
    refreshRate: 20,
    duration: 5000,
    dataSets: [
      {
        label: 'SG 2',
        color: ThemeVariables.colours.secondary,
        dataValue: 'sg',
      },
    ]
  },
  {
    id: 'sg_split_3',
    label: 'SG 3',
    min: -6,
    max: 6,
    refreshRate: 20,
    duration: 5000,
    dataSets: [
      {
        label: 'SG 3',
        color: ThemeVariables.colours.darkBlue,
        dataValue: 'sg',
      },
    ]
  },
]