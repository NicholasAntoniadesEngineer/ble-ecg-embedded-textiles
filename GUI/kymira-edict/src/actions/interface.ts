import { RouteModel } from 'models/RouteModel'
import { CsvDownloadTypes } from 'models/csvDownloadTypes'
import { IMULimbsModel } from 'models/IMULimbsModel'
import { History } from 'history'

export interface IActions {
  AppService: IAppBloc;
  HistoryService: IHistoryService;
  NotificationService: INotificationService;
}

export interface IAppBloc {
  setActiveMenuItem: (item: RouteModel | string) => void;
  handleMenuItemClick: (path: RouteModel) => void;
  handleCSVDownload: (type: CsvDownloadTypes, email: string, start?: number, end?: number) => void;
  toggleBookmarkBar: () => void;
  closeBookmarkBar: () => void;
  handleAddBookmark: (note: string, tstamp: number) => void;
  setMultiIMUData: (limb: IMULimbsModel) => void;
}

export interface INotificationService {
  showSuccessMessage: (message: string, autoClose?: number) => void;
  showWarnMessage: (message: string) => void;
  showErrorMessage: (message: string, autoClose?: number) => void;
}

export interface IHistoryService {
  getHistory: () => History<History>;
  push: (route: RouteModel) => void;
  back: () => void;
}