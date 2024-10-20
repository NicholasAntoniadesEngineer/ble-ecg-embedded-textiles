import { FC } from 'react'
import { useObservable } from 'rxjs-hooks'

import Actions from 'actions'
import AddBookmarkComponent from './component'

interface IAddbookMarkContainerProps {
  ts: number | undefined
}

const AddbookMarkContainer:FC<IAddbookMarkContainerProps> = ({
  ts,
}) => {
  const { showBookmarkBar } = useObservable(Actions.AppService.getSubject)
    || Actions.AppService.getCurrentState()

  return (
    <AddBookmarkComponent
      showBookmarkBar={ showBookmarkBar }
      ts={ ts }
      addBookmark={ Actions.AppService.handleAddBookmark }
    />
  )
}

export default AddbookMarkContainer