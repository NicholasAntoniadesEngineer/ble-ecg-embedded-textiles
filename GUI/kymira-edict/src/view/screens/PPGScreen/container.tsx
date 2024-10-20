import { FC } from 'react'
import { useObservable } from 'rxjs-hooks'

import Actions from 'actions'
import PPGScreenComponent from './component'

const PPGScreenContainer:FC = () => {
  const { socket } = useObservable(Actions.AppService.getSubject)
  || Actions.AppService.getCurrentState()

  return (
    <PPGScreenComponent
      socket={ socket }
    />
  )
}

export default PPGScreenContainer