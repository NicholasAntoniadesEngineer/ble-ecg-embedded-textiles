import { FC } from 'react'
import AppScaffold from './screens/AppScaffold'
import Notification from './components/Notification'

const AppViewComponent:FC = () => {
  return (
    <>
      <AppScaffold />
      <Notification />
    </>
  )
}

export default AppViewComponent
