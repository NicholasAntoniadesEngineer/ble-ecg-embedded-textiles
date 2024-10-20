import { FC } from 'react'
import {
  Route, Switch, Redirect,
} from 'react-router-dom'
import { RouteModel } from 'models/RouteModel'
import HomeScreen from 'view/screens/HomeScreen'
import ECGScreen from 'view/screens/ECGScreen'
// import EMGScreen from 'view/screens/EMGScreen'
import IMUScreen from 'view/screens/IMUScreen'
import CSVScreen from 'view/screens/CSVScreen'
// import MultiIMUScreen from 'view/screens/12IMUScreen'
// import SGScreen from 'view/screens/SGScreen'
import PPGScreen from 'view/screens/PPGScreen'

const AppRouterComponent: FC = () => {
  return (
    <Switch>
      <Route
        path={ RouteModel.home }
        component={ HomeScreen }
      />
      <Route
        path={ RouteModel.ecg }
        component={ ECGScreen }
      />
      {/* <Route
        path={ RouteModel.emg }
        component={ EMGScreen }
      /> */}
      <Route
        path={ RouteModel.imu }
        component={ IMUScreen }
      />
      {/* <Route
        path={ RouteModel.multiImu }
        component={ MultiIMUScreen }
      /> */}
      <Route
        path={ RouteModel.ppg }
        component={ PPGScreen }
      />
      {/* <Route
        path={ RouteModel.sg }
        component={ SGScreen }
      /> */}
      <Route
        path={ RouteModel.csv }
        component={ CSVScreen }
      />
      <Redirect to={ RouteModel.home }/>
    </Switch>
  )
}

export default AppRouterComponent