import { FC } from 'react'
import { useObservable } from 'rxjs-hooks'

import Actions from 'actions'
import MultiIMUScreenComponent from './component'

const MulitIMUScreenContainer:FC = () => {
  const { socket, multiIMUSelectedData, multiIMUActiveButton } = useObservable(Actions.AppService.getSubject)
  || Actions.AppService.getCurrentState()

  return (
    <MultiIMUScreenComponent
      socket={ socket }
      selectedData={ multiIMUSelectedData }
      activeButton={ multiIMUActiveButton }
      handleSetData={ Actions.AppService.setMultiIMUData }
    />
  )
}

export default MulitIMUScreenContainer