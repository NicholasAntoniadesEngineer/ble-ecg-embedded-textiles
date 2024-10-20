import { FC, ReactElement } from 'react'
import { Box, Typography } from '@mui/material'
import ThemeVariables from 'common/variables'
import ErrorOutlineIcon from '@mui/icons-material/ErrorOutline'
import DoneOutlineIcon from '@mui/icons-material/DoneOutline'

interface IBasicNotificationMessageComponent {
  message: string | Element;
  type: string;
}

const BasicNotificationMessageComponent: FC<IBasicNotificationMessageComponent> = ({
  message,
  type,
}) => {
  let bgColour: string = ThemeVariables.colours.primary
  let icon: ReactElement = <DoneOutlineIcon />

  switch (type) {
    case 'success':
      bgColour = ThemeVariables.colours.success
      break

    case 'warning':
      bgColour = ThemeVariables.colours.warn
      icon = <ErrorOutlineIcon />
      break

    case 'error':
      bgColour = ThemeVariables.colours.primary
      icon = <ErrorOutlineIcon />
      break
  }

  return (
    <Box
      sx={ {
        backgroundColor: bgColour,
        position: 'absolute',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        display: 'flex',
        alignItems: 'center',
        paddingLeft: ThemeVariables.spacing.xl,
        color: 'white'
      } }
    >
      {icon}
      <Typography
        variant="body1"
        sx={ {
          paddingLeft: ThemeVariables.spacing.sm,
          fontWeight: ThemeVariables.fontWeights.bold,
        } }
      >{message}</Typography>
    </Box>
  )
}

export default BasicNotificationMessageComponent
