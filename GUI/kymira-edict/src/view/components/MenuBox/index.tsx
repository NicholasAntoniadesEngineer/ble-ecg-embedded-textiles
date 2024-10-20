import { FC } from 'react'
import { Typography, Box, ButtonBase, Grow } from '@mui/material'
import ArrowForwardIcon from '@mui/icons-material/ArrowForward'
import ThemeVariables from 'common/variables'

interface IMenuBoxComponentProps {
  title: string;
  onClick: () => void;
}

const MenuBoxComponent:FC<IMenuBoxComponentProps> = ({
  title,
  onClick
}) => {
  return (
    <Grow
      in
      timeout={ 500 }
    >
      <ButtonBase
        sx={ {
          width: '100%',
        } }
      >
        <Box
          onClick={ onClick }
          sx={ {
            transition: '0.3s ease',
            width: '100%',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            borderRadius: '4px',
            backgroundColor: 'white',
            paddingLeft: ThemeVariables.spacing.md,
            paddingRight: ThemeVariables.spacing.md,
            paddingTop: ThemeVariables.spacing.xl,
            paddingBottom: ThemeVariables.spacing.xl,
            boxShadow: '0px 12px 24px #0000000F',
            '&:hover': {
              boxShadow: '0px 12px 24px #0000002b',
              cursor: 'pointer',
              '& .arrowIcon': {
                right: '-0.15em'
              }
            }
          } }
        >
          <Typography
            variant="h4"
            sx={ {
              fontWeight: ThemeVariables.fontWeights.bold
            } }
          >{title}</Typography>
          <Box
            sx={ {
              display: 'flex',
              color: 'primary.main',
              position: 'relative'
            } }
          >
            <Typography
              sx={ {
                fontWeight: ThemeVariables.fontWeights.bold,
                marginRight: '1.15em'
              } }
              variant="body2"
            >
            View
            </Typography>
            <ArrowForwardIcon
              className="arrowIcon"
              sx={ {
                fontSize: ThemeVariables.fontSizes.xs,
                transition: '0.3s ease',
                position: 'absolute',
                top: '0.15em',
                right: 0,
              } }
            />
          </Box>
        </Box>
      </ButtonBase>
    </Grow>
  )
}

export default MenuBoxComponent