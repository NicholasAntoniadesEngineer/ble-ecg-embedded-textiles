import { FC } from 'react'
import { useObservable } from 'rxjs-hooks'

import Actions from 'actions'
import ECGScreenComponent from './component'

const ECGScreenContainer:FC = () => {
  const { socket } = useObservable(Actions.AppService.getSubject)
  || Actions.AppService.getCurrentState()

  return (
    <ECGScreenComponent socket={ socket } />
  )
}

export default ECGScreenContainer