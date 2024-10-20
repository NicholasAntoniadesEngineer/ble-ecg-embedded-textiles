import AppBloc from './blocs/AppBloc'
import HistoryService from './commonServices/HistoryBloc'
import NotificationService from './commonServices/NotificationBloc'
import { IActions } from './interface'

class Actions implements IActions {
  AppService = AppBloc
  HistoryService = HistoryService
  NotificationService = NotificationService
}

export default new Actions()
