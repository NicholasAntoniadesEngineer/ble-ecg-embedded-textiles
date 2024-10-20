import { OverridableComponent } from '@mui/material/OverridableComponent'
import { SvgIconTypeMap } from '@mui/material'
import { RouteModel } from './RouteModel'

export interface IMenuItemsModel {
  selected: boolean,
  text: string,
  location: string;
  path: RouteModel;
  showBookmark: boolean;
  icon?: OverridableComponent<SvgIconTypeMap<{}, 'svg'>>,
}