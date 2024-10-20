import { FC } from 'react'
import { useObservable } from 'rxjs-hooks'

import Actions from 'actions'
import IMUScreenComponent from './component'

const IMUScreenContainer:FC = () => {
  const { socket } = useObservable(Actions.AppService.getSubject)
  || Actions.AppService.getCurrentState()

  return (
    <IMUScreenComponent socket={ socket } />
  )
}

export default IMUScreenContainer