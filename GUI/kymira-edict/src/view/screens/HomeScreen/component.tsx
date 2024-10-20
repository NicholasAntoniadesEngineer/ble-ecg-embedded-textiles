import { FC } from 'react'
import { Typography, Box, Grid } from '@mui/material'
import { Socket } from 'socket.io-client'
import { RouteModel } from 'models/RouteModel'
import { IMenuItemsModel } from 'models/menuItemsModel'
import ThemeVariables from 'common/variables'
import PageTitle from 'view/components/PageTitle'
import MenuBox from 'view/components/MenuBox'

interface IHomeScreenComponentProps {
  socket: Socket;
  dataMenuItems: IMenuItemsModel[];
  toolMenuItems: IMenuItemsModel[];
  handleMenuItemClick: (path: RouteModel) => void;
}

const HomeScreenComponent: FC<IHomeScreenComponentProps> = ({
  socket,
  dataMenuItems,
  toolMenuItems,
  handleMenuItemClick,
}) => {
  const { userAgent } = navigator
  const { platform } = navigator
  const online = navigator.onLine.valueOf().toString()
  const { connected, id } = socket

  const handleClick = (path: RouteModel) => {
    // Settimeout to allow animation on button
    setTimeout(() => {
      handleMenuItemClick(path)
    }, 200)
  }

  return (
    <>
      <Box
        sx={ {
          maxWidth: '35em'
        } }
      >
        <Typography variant="body1">{`Socket Connected: ${connected}`}</Typography>
        <Typography
          variant="body1"
          sx={ {
            marginBottom: ThemeVariables.spacing.xl
          } }
        >{`Socket ID: ${id}`}</Typography>
        <Typography
          variant="body1"
          sx={ {
            marginBottom: ThemeVariables.spacing.xl
          } }
        >{`User Agent: ${userAgent}`}</Typography>
        <Typography variant="body1">{`Platform: ${platform}`}</Typography>
        <Typography variant="body1">{`Online: ${online}`}</Typography>
      </Box>

      <Box
        sx={ {
          marginTop: '4em',
        } }
      >
        <PageTitle title="Data" />
        <Grid
          container
          spacing={ 3 }
          sx={ {
            marginTop: ThemeVariables.spacing.xxs,
          } }
        >
          {dataMenuItems.map((item) => (
            <Grid
              key={ item.text }
              item
              xs={ 6 }
              sm={ 6 }
              md={ 4 }
              lg={ 2 }
            >
              <MenuBox
                title={ item.text }
                onClick={ () => handleClick(item.path) }
              />
            </Grid>
          ))}
        </Grid>
      </Box>
      <Box
        sx={ {
          marginTop: '4em',
        } }
      >
        <PageTitle title="Tools" />
        <Grid
          container
          spacing={ 3 }
          sx={ {
            marginTop: ThemeVariables.spacing.xxs,
          } }
        >
          {toolMenuItems.map((item) => (
            <Grid
              key={ item.text }
              item
              xs={ 6 }
              sm={ 6 }
              md={ 4 }
              lg={ 2 }
            >
              <MenuBox
                title={ item.text }
                onClick={ () => handleClick(item.path) }
              />
            </Grid>
          ))}
        </Grid>
      </Box>
    </>
  )
}

export default HomeScreenComponent