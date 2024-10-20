import { FC } from 'react'
import ThemeVariables from 'common/variables'
import { RouteModel } from 'models/RouteModel'
import { IMenuItemsModel } from 'models/menuItemsModel'
import { Box, Typography } from '@mui/material'

import SideBarMenu from 'view/components/SideBarMenu'
import Logo from 'view/components/Logo'

interface IAppSideBarComponentProps {
  dataMenuItems: IMenuItemsModel[];
  toolMenuItems: IMenuItemsModel[];
  handleMenuItemClick: (path: RouteModel) => void;
}

const AppSideBarComponent: FC<IAppSideBarComponentProps> = ({
  dataMenuItems,
  toolMenuItems,
  handleMenuItemClick,
}) => {
  return (
    <Box
      sx={ {
        height: '100%',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'space-between',
      } }
    >
      <Box>
        <Box
          sx={ {
            padding: ThemeVariables.spacing.xl,
            textAlign: 'center',
            paddingBottom: '10em',
          } }
        >
          <Box onClick={ () => handleMenuItemClick(RouteModel.home) }>
            <Logo />
          </Box>
        </Box>
        <Box>
          <Typography
            variant="body2"
            sx={ {
              paddingLeft: ThemeVariables.spacing.lg,
              fontWeight: ThemeVariables.fontWeights.medium,
              color: 'black',
            } }
          >
            Data
          </Typography>
          <SideBarMenu
            menuItems={ dataMenuItems }
            onClick={ handleMenuItemClick }
          />
        </Box>
      </Box>
      <Box>
        <Typography
          variant="body2"
          sx={ {
            paddingLeft: ThemeVariables.spacing.lg,
            fontWeight: ThemeVariables.fontWeights.medium,
            color: 'black',
          } }
        >
          Tools
        </Typography>
        <SideBarMenu
          menuItems={ toolMenuItems }
          onClick={ handleMenuItemClick }
        />
      </Box>
    </Box>
  )
}

export default AppSideBarComponent