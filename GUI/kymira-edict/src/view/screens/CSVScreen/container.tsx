import { FC } from 'react'
import { useObservable } from 'rxjs-hooks'

import Actions from 'actions'
import CSVScreenComponent from './component'

const CSVScreenContainer:FC = () => {
  const { csvLoading } = useObservable(Actions.AppService.getSubject)
    || Actions.AppService.getCurrentState()

  return (
    <CSVScreenComponent
      csvLoading={ csvLoading }
      handleCSVDownload={ Actions.AppService.handleCSVDownload }
    />
  )
}

export default CSVScreenContainer