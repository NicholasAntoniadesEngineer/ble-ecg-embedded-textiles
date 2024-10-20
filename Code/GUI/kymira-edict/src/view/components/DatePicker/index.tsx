import { FC } from 'react'
import MobileDateTimePicker from '@mui/lab/MobileDateTimePicker'
import AdapterDateFns from '@mui/lab/AdapterMoment'
import LocalizationProvider from '@mui/lab/LocalizationProvider'
import { TextField } from '@mui/material'
import ThemeVariables from 'common/variables'
import { Moment } from 'moment'

interface IDatePickerComponentProps {
  value: Moment | null;
  onChange: (date: Moment | null) => void;
}

const DatePickerComponent:FC<IDatePickerComponentProps> = ({
  value,
  onChange
}) => {
  return (
    <LocalizationProvider dateAdapter={ AdapterDateFns }>
      <MobileDateTimePicker
        allowSameDateSelection
        showDaysOutsideCurrentMonth
        value={ value }
        onChange={ (newValue) => {
          onChange(newValue)
        } }
        renderInput={ (params) => (
          <TextField
            { ...params }
            sx={ {
              minWidth: '20em',
              '& .MuiOutlinedInput-notchedOutline': {
                borderColor: 'white',
              },
              '& .MuiOutlinedInput-input': {
                transition: '0.3s ease',
                fontWeight: ThemeVariables.fontWeights.medium,
                boxShadow: '0px 12px 24px #0000000F',
                '&:hover': {
                  cursor: 'pointer',
                  boxShadow: '0px 12px 24px #0000002b',
                  borderColor: 'white',
                }
              },
              '&:hover': {
                '& .MuiOutlinedInput-notchedOutline': {
                  borderColor: 'white !important',
                },
              },
              '& .Mui-focused': {
                '& .MuiOutlinedInput-notchedOutline': {
                  borderColor: 'white !important',
                  boxShadow: '0px 12px 24px #0000002b',
                },
              }
            } }
          />
        ) }
      />
    </LocalizationProvider>
  )
}

export default DatePickerComponent