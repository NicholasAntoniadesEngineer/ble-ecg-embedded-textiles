import { FC } from 'react'
import { useObservable } from 'rxjs-hooks'

import Actions from 'actions'
import EMGScreenComponent from './component'

const EMGScreenContainer:FC = () => {
  const { socket } = useObservable(Actions.AppService.getSubject)
  || Actions.AppService.getCurrentState()

  return (
    <EMGScreenComponent
      socket={ socket }
    />
  )
}

export default EMGScreenContainer