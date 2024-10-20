import { FC } from 'react'
import { Typography } from '@mui/material'
import ThemeVariables from 'common/variables'

interface IPageTitleComponentProps {
  title?: string;
}

const PageTitleComponent:FC<IPageTitleComponentProps> = ({
  title
}) => {
  return (
    <Typography
      variant="h2"
      sx={ {
        position: 'relative',
        display: 'inline-block',
        fontWeight: ThemeVariables.fontWeights.bold,
        '&::after': {
          content: '""',
          position: 'absolute',
          left: 0,
          bottom: -3,
          height: '3px',
          backgroundColor: 'primary.main',
          width: '2em'
        },
      } }
    >
      {title}
    </Typography>
  )
}

export default PageTitleComponent