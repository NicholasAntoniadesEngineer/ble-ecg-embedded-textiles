import { FC } from 'react'
import { IMenuItemsModel } from 'models/menuItemsModel'
import { ListItemText, ListItemButton, Typography } from '@mui/material'
import ThemeVariables from 'common/variables'

interface IMenuItemComponentProps {
  item: IMenuItemsModel;
  onClick: () => void;
}

const MenuItemComponent:FC<IMenuItemComponentProps> = ({
  item,
  onClick
}) => {
  return (
    <ListItemButton
      selected={ item.selected }
      onClick={ onClick }
    >
      <ListItemText
        sx={ {
          paddingLeft: ThemeVariables.spacing.lg,
          '.MuiTypography-root': {
            display: 'flex',
            alignItems: 'center'
          }
        } }
      >
        {item.icon && (
          <item.icon />
        )}
        <Typography variant="body1">{item.text}</Typography>
      </ListItemText>
    </ListItemButton>
  )
}

export default MenuItemComponent