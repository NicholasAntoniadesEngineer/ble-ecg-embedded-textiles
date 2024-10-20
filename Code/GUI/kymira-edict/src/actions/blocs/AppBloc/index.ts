
import { IAppBloc } from 'actions/interface'
import { ProtoBloc } from '../proto-block'
import { RouteModel } from 'models/RouteModel'
import { IMULimbsModel } from 'models/IMULimbsModel'
import { IAppState } from './state-model'
import { MultiIMUGraphData } from 'graphModels/12IMUGraphModel'

import { CsvDownloadTypes } from 'models/csvDownloadTypes'

import DownloadIcon from '@mui/icons-material/Download'
import HistoryBloc from 'actions/commonServices/HistoryBloc'
import NotificationBloc from 'actions/commonServices/NotificationBloc'
import { io } from 'socket.io-client'
import axios from 'axios'

const defaultAppState: IAppState = {
  socket: io('https://devtest-backend.azurewebsites.net', { transports: ['websocket', 'polling'] }),
  csvLoading: false,
  showBookmarkBar: false,
  bookmarkLoading: false,
  multiIMUSelectedData: MultiIMUGraphData.leftLegGraphs,
  multiIMUActiveButton: IMULimbsModel.leftLeg,
  menuItems: [
    {
      selected: true,
      text: 'Home',
      location: 'data',
      path: RouteModel.home,
      showBookmark: false,
    },
    {
      selected: false,
      text: 'ECG',
      location: 'data',
      path: RouteModel.ecg,
      showBookmark: true,
    },
    // {
    //   selected: false,
    //   text: 'EMG',
    //   location: 'data',
    //   path: RouteModel.emg,
    //   showBookmark: false,
    // },
    {
      selected: false,
      text: 'IMU',
      location: 'data',
      path: RouteModel.imu,
      showBookmark: true,
    },
    // {
    //   selected: false,
    //   text: '12 IMU',
    //   location: 'data',
    //   path: RouteModel.multiImu,
    //   showBookmark: false,
    // },
    {
      selected: false,
      text: 'PPG',
      location: 'data',
      path: RouteModel.ppg,
      showBookmark: true,
    },
    // {
    //   selected: false,
    //   text: 'SG',
    //   location: 'data',
    //   path: RouteModel.sg,
    //   showBookmark: false,
    // },
    {
      selected: false,
      text: 'CSV',
      location: 'tools',
      icon: DownloadIcon,
      path: RouteModel.csv,
      showBookmark: false,
    },
  ]
}

interface IResponseFailureModel {
  msg: string;
}

class AppScreenBloc extends ProtoBloc<IAppState> implements IAppBloc {
  constructor() {
    super(defaultAppState)
  }

  setActiveMenuItem = (item: RouteModel) => {
    const newState = { ...this.state }

    // Set active state for menu item and set other items to false
    newState.menuItems.forEach((menuItem) => {
      menuItem.path === item ? menuItem.selected = true : menuItem.selected = false
    })

    this.pushState(newState)
  }

  handleMenuItemClick = (path: RouteModel) => {
    this.setActiveMenuItem(path)
    HistoryBloc.push(path)
  }

  toggleBookmarkBar = () => {
    this.pushState({
      ...this.state,
      showBookmarkBar: !this.state.showBookmarkBar
    })
  }

  closeBookmarkBar = () => {
    this.pushState({
      ...this.state,
      showBookmarkBar: false,
    })
  }

  handleAddBookmark = async (note: string, tstamp: number) => {
    const body = {
      note: note,
      tstamp: tstamp,
    }

    this.pushState({
      ...this.state,
      bookmarkLoading: true,
    })

    try {
      const response = await axios.post('https://kymetric-hub-imperial.azurewebsites.net/api/bookmarks/save', body)

      if (response) {
        NotificationBloc.showSuccessMessage('Bookmark added')
      }

    } catch (e) {
      NotificationBloc.showErrorMessage('oops something went wrong')
    }

    this.pushState({
      ...this.state,
      csvLoading: false,
    })

  }

  handleCSVDownload = async (type: CsvDownloadTypes, email: string, start?: number, end?: number) => {
    const body = {
      startDate: start,
      endDate: end,
      email: email
    }

    this.pushState({
      ...this.state,
      csvLoading: true,
    })

    try {
      const response = await axios.post(`https://dev-${type}.azurewebsites.net/api/csv/download`, body)

      if (response) {
        NotificationBloc.showSuccessMessage('Success!')
      }

    } catch (e) {
      e.response.data.forEach((item: IResponseFailureModel) => {
        NotificationBloc.showErrorMessage(`${type}: ${item.msg}`)
      })
    }

    this.pushState({
      ...this.state,
      csvLoading: false,
    })
  }

  setMultiIMUData = (limb: IMULimbsModel) => {
    const newState = { ...this.state }
    const { rightArmGraphs, leftArmGraphs, rightLegGraphs, leftLegGraphs, torsoGraphs } = MultiIMUGraphData

    switch (limb) {
      case IMULimbsModel.leftArm:
        newState.multiIMUSelectedData = leftArmGraphs
        break
      case IMULimbsModel.leftLeg:
        newState.multiIMUSelectedData = leftLegGraphs
        break
      case IMULimbsModel.rightLeg:
        newState.multiIMUSelectedData = rightLegGraphs
        break
      case IMULimbsModel.rightArm:
        newState.multiIMUSelectedData = rightArmGraphs
        break
      case IMULimbsModel.torso:
        newState.multiIMUSelectedData = torsoGraphs
        break
    }

    newState.multiIMUActiveButton = limb

    this.pushState(newState)
  }
}

export default new AppScreenBloc()
