import { IMenuItemsModel } from 'models/menuItemsModel'
import { IGraphModel } from 'models/graphModel'
import { IMULimbsModel } from 'models/IMULimbsModel'
import { Socket } from 'socket.io-client'

export interface IAppState {
  socket: Socket;
  multiIMUSelectedData: IGraphModel[];
  menuItems: IMenuItemsModel[];
  multiIMUActiveButton: IMULimbsModel;
  csvLoading: boolean;
  bookmarkLoading: boolean;
  showBookmarkBar: boolean;
}
