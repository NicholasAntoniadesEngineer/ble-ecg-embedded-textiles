import { FC, useState } from 'react'
import moment, { Moment } from 'moment'
import { Box, Typography, Stack } from '@mui/material'

import { CsvDownloadTypes } from 'models/csvDownloadTypes'

import LoadingButton from '@mui/lab/LoadingButton'
import TextField from 'view/components/TextField'
import DatePicker from 'view/components/DatePicker'

import ThemeVariables from 'common/variables'

interface ICSVScreenComponentProps {
  csvLoading: boolean;
  handleCSVDownload: (type: CsvDownloadTypes, email: string, start?: number, end?: number) => void
}

const CSVScreenComponent: FC<ICSVScreenComponentProps> = ({
  csvLoading,
  handleCSVDownload
}) => {
  const [startDate, setStartDate] = useState<Moment | null>(moment())
  const [endDate, setEndDate] = useState<Moment | null>(moment())
  const [email, setEmail] = useState('')
  const [emailError, updateEmailError] = useState(false)

  const validateEmail = (emailToValidate: string) => {
    const reg = /^[^\s@]+@[^\s@]+\.[^\s@]+$/

    return reg.test(emailToValidate)
  }

  const handleInputChange = (value: string) => {
    emailError && updateEmailError(false)
    setEmail(value)
  }


  const handleEmailClick = (type: CsvDownloadTypes) => {
    if (!validateEmail(email) || email === '') {
      updateEmailError(true)

      return
    }

    updateEmailError(false)
    handleCSVDownload(type, email, startDate?.unix(), endDate?.unix())
  }

  return (
    <>
      <Box
        sx={ {
          marginTop: '2.5em',
        } }
      >
        <Typography
          variant="h5"
          sx={ {
            marginBottom: ThemeVariables.spacing.sm
          } }
        >
          Start Date
        </Typography>
        <DatePicker
          value={ startDate }
          onChange={ setStartDate }
        />
        <Typography
          variant="h5"
          sx={ {
            marginBottom: ThemeVariables.spacing.sm,
            marginTop: ThemeVariables.spacing.xxl
          } }
        >
          End Date
        </Typography>
        <DatePicker
          value={ endDate }
          onChange={ setEndDate }
        />
        <Typography
          variant="h5"
          sx={ {
            marginBottom: ThemeVariables.spacing.sm,
            marginTop: ThemeVariables.spacing.xxl
          } }
        >
          Email address
        </Typography>
        <TextField
          value={ email }
          error={ emailError }
          onChange={ handleInputChange }
        />
        <Stack
          direction="row"
          spacing={ 2 }
          alignItems="center"
          sx={ {
            marginTop: ThemeVariables.spacing.xxl
          } }
        >
          <LoadingButton
            variant="contained"
            color="secondary"
            size="large"
            loading={ csvLoading }
            onClick={ () => handleEmailClick(CsvDownloadTypes.imperial) }
          >
            Send CSV
          </LoadingButton>
          {/* <LoadingButton
            variant="contained"
            color="secondary"
            size="large"
            loading={ csvLoading }
            onClick={ () => handleEmailClick(CsvDownloadTypes.newcastle) }
          >
            Send Newcastle CSV
          </LoadingButton> */}
        </Stack>
      </Box>
    </>
  )
}

export default CSVScreenComponent