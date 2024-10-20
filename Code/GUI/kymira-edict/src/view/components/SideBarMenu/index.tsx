import { FC } from 'react'
import ThemeVariables from 'common/variables'
import { IMenuItemsModel } from 'models/menuItemsModel'
import { RouteModel } from 'models/RouteModel'
import { List } from '@mui/material'
import MenuItem from '../MenuItem'

interface ISideBarMenuComponentProps {
  menuItems: IMenuItemsModel[];
  onClick: (path: RouteModel) => void;
}

const SideBarMenuComponent:FC<ISideBarMenuComponentProps> = ({
  menuItems,
  onClick,
}) => {
  return (
    <List
      sx={ {
        paddingRight: ThemeVariables.spacing.xl,
        '& .MuiListItemButton-root': {
          transition: '0.3s ease',
          borderTopRightRadius: '10px',
          borderBottomRightRadius: '10px',
          '&::before': {
            transition: '0.3s ease',
            display: 'block',
            content: '""',
            left: '-2em',
            top: 0,
            bottom: 0,
            position: 'absolute',
            backgroundColor: 'primary.main',
            width: '3px',
            borderRadius: '5px',
          },
        },
        '& .MuiTypography-root': {
          color: 'darkBlue.main',
          fontWeight: ThemeVariables.fontWeights.medium,
        },
        '&& .Mui-selected, && .Mui-selected:hover': {
          transition: '0.3s ease',
          '&::before': {
            left: 0,
          },
          '&, & .MuiTypography-root': {
            color: 'primary.main',
            fontWeight: ThemeVariables.fontWeights.bold,
          },
        },
      } }
    >
      {menuItems.map((item) => (
        <MenuItem
          key={ item.text }
          item={ item }
          onClick={ () => onClick(item.path) }
        />
      ))}
    </List>
  )
}

export default SideBarMenuComponent