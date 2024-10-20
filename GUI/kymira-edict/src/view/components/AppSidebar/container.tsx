import { FC } from 'react'
import { useObservable } from 'rxjs-hooks'

import Actions from 'actions'
import AppSideBarComponent from './component'

const AppSideBarContainer:FC = () => {
  const { menuItems } = useObservable(Actions.AppService.getSubject)
    || Actions.AppService.getCurrentState()

  const dataMenuItems = menuItems.filter((item) => item.location === 'data')
  const toolMenuItems = menuItems.filter((item) => item.location === 'tools')

  return (
    <AppSideBarComponent
      dataMenuItems={ dataMenuItems }
      toolMenuItems={ toolMenuItems }
      handleMenuItemClick={ Actions.AppService.handleMenuItemClick }
    />
  )
}

export default AppSideBarContainer