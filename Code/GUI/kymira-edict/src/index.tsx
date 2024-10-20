import { StrictMode } from 'react'
import ReactDOM from 'react-dom'
import App from 'view'
import reportWebVitals from './reportWebVitals'
import { Router } from 'react-router-dom'
import actions from 'actions'
import theme from './common/theme'
import { ThemeProvider } from '@mui/material/styles'
import { CssBaseline } from '@mui/material'
import { injectStyle } from 'react-toastify/dist/inject-style'

ReactDOM.render(
  <StrictMode>
    <Router history={ actions.HistoryService.getHistory() }>
      <ThemeProvider theme={ theme }>
        <CssBaseline />
        <App />
      </ThemeProvider>
    </Router>
  </StrictMode>,
  document.getElementById('root')
)

injectStyle()

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals()
