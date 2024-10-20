import { FC } from 'react'
import { useObservable } from 'rxjs-hooks'

import Actions from 'actions'
import SCScreenComponent from './component'

const SCScreenContainer:FC = () => {
  const { socket } = useObservable(Actions.AppService.getSubject)
  || Actions.AppService.getCurrentState()

  return (
    <SCScreenComponent
      socket={ socket }
    />
  )
}

export default SCScreenContainer