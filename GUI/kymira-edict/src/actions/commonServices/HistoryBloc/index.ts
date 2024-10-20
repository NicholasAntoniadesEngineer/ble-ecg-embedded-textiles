import {
  createBrowserHistory, BrowserHistoryBuildOptions, History,
} from 'history'

import { RouteModel } from 'models/RouteModel'
import { IHistoryService } from 'actions/interface'

const buildHistoryOptions: BrowserHistoryBuildOptions = {
  basename: process.env.baseName,
}

class HistoryBloc implements IHistoryService {
  history: History<History> = createBrowserHistory(buildHistoryOptions)

  getHistory = () => {
    return this.history
  }

  push = (route: RouteModel | string) => {
    this.history.push(route)
  }

  back = () => {
    this.history.goBack()
  }
}

export default new HistoryBloc()
