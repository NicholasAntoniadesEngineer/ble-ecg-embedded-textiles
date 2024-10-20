import { FC } from 'react'
import { useObservable } from 'rxjs-hooks'

import Actions from 'actions'
import AppScaffoldComponent from './component'

const AppScaffoldContainer:FC = () => {
  const { menuItems } = useObservable(Actions.AppService.getSubject)
  || Actions.AppService.getCurrentState()

  const pageProps = menuItems.find((item) => item.selected)

  return (
    <AppScaffoldComponent
      pageProps={ pageProps }
      openBookmark={ Actions.AppService.toggleBookmarkBar }
      push={ Actions.HistoryService.push }
    />
  )
}

export default AppScaffoldContainer