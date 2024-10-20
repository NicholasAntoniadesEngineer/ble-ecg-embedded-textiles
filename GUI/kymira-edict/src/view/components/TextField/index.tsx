import { FC } from 'react'
import { TextField } from '@mui/material'
import ThemeVariables from 'common/variables'

interface ITextFieldComponentProps {
  value: string;
  error?: boolean;
  minWidth?: string;
  size?: 'small' | 'medium' | undefined,
  onBlur?: () => void;
  onChange: (value: string) => void;
}

const TextFieldComponent: FC<ITextFieldComponentProps> = ({
  value,
  error,
  minWidth = '20em',
  size,
  onBlur,
  onChange
}) => {
  return (
    <TextField
      error={ error }
      variant="outlined"
      size={ size }
      value={ value }
      type="email"
      onBlur={ onBlur }
      onChange={ (e) => onChange(e.target.value) }
      sx={ {
        minWidth: minWidth,
        '@media(min-width: 600px)': {
          minWidth: '100%'
        },
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
  )
}

export default TextFieldComponent