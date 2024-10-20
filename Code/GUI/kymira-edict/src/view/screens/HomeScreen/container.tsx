import { FC } from 'react'
import { useObservable } from 'rxjs-hooks'

import Actions from 'actions'
import HomeScreenComponent from './component'
import { RouteModel } from 'models/RouteModel'

const AppSideBarContainer:FC = () => {
  const { socket, menuItems } = useObservable(Actions.AppService.getSubject)
  || Actions.AppService.getCurrentState()

  const dataMenuItems = menuItems.filter((item) => item.location === 'data' && item.path !== RouteModel.home)
  const toolMenuItems = menuItems.filter((item) => item.location === 'tools')

  return (
    <HomeScreenComponent
      socket={ socket }
      dataMenuItems={ dataMenuItems }
      toolMenuItems={ toolMenuItems }
      handleMenuItemClick={ Actions.AppService.handleMenuItemClick }
    />
  )
}

export default AppSideBarContainer