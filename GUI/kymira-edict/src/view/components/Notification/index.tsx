import { FC } from 'react'
import { ToastContainer } from 'react-toastify'

const NotificationComponent: FC = () => {
  return (
    <ToastContainer
      role="alert"
      position="top-right"
      autoClose={ 5000 }
      hideProgressBar={ true }
      closeButton={ false }
      newestOnTop
      closeOnClick
      rtl={ false }
      draggable
      pauseOnHover
      pauseOnFocusLoss={ false }
    />
  )
}

export default NotificationComponent
