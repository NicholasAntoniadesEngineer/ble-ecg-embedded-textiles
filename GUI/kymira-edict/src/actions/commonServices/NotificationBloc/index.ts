import { createElement } from 'react'
import { toast } from 'react-toastify'
import { INotificationService } from 'actions/interface'
import BasicNotification from 'view/components/BasicNotification'

class NotificationService implements INotificationService {
  showSuccessMessage = (message: string, autoClose = 5000) => {
    return toast(
      createElement(
        BasicNotification,
        {
          message,
          type: 'success',
        }
      ),
      {
        hideProgressBar: true,
        position: 'bottom-right',
        autoClose,
      }
    )
  }

  showWarnMessage = (message: string, autoClose = 5000) => {
    return toast(
      createElement(
        BasicNotification,
        {
          message,
          type: 'warning',
        }
      ),
      {
        hideProgressBar: true,
        position: 'bottom-right',
        autoClose,
      }
    )
  }

  showErrorMessage = (message: string, autoClose = 5000) => {
    return toast(
      createElement(
        BasicNotification,
        {
          message,
          type: 'error',
        }
      ),
      {
        hideProgressBar: true,
        position: 'bottom-right',
        autoClose,
      }
    )
  }
}

export default new NotificationService()
