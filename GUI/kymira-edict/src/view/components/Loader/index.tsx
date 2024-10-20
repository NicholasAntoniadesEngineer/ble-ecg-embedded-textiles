import { FC } from 'react'
import Loader from 'react-loader-spinner'
import ThemeVariables from 'common/variables'

const LoaderComponent:FC = () => {
  return (
    <Loader
      type="ThreeDots"
      color={ ThemeVariables.colours.darkBlue }
      height={ 60 }
      width={ 60 }
    />
  )
}

export default LoaderComponent
