import { FC, useEffect } from 'react'
import { Box } from '@mui/material'
import ThemeVariables from 'common/variables'
import AppSideBar from '../../components/AppSidebar'
import AppHeader from '../../components/AppHeader'
import { IMenuItemsModel } from 'models/menuItemsModel'
import AppRouter from 'view/routers/AppRouter'
import { RouteModel } from 'models/RouteModel'

interface IAppScaffoldComponentProps {
  pageProps?: IMenuItemsModel;
  openBookmark: () => void;
  push: (route: RouteModel) => void;
}

const AppScaffoldComponent:FC<IAppScaffoldComponentProps> = ({
  pageProps,
  push,
  openBookmark,
}) => {
  useEffect(() => {
    push(RouteModel.home)
  }, [])

  return (
    <Box
      sx={ {
        display: 'flex',
        height: '100vh',
      } }
    >
      <Box
        sx={ {
          width: '12.5em',
          bgcolor: 'white',
          justifyContent: 'space-between',
        } }
      >
        <AppSideBar />
      </Box>
      <Box
        sx={ {
          paddingTop: ThemeVariables.spacing.lg,
          paddingBottom: ThemeVariables.spacing.xl,
          paddingLeft: ThemeVariables.spacing.xl,
          paddingRight: ThemeVariables.spacing.xl,
          width: '100%',
          height: '100vh',
          overflowY: 'scroll',
          '@media(min-width: 600px)': {
            paddingLeft: ThemeVariables.spacing.xxxl,
            paddingRight: ThemeVariables.spacing.xxxl,
            paddingBottom: ThemeVariables.spacing.xxxl,
          }
        } }
      >
        <AppHeader
          title={ pageProps?.text }
          showBookmarkButton={ pageProps?.showBookmark }
          openBookmark={ openBookmark }
        />
        <Box
          sx={ {
            mt: ThemeVariables.spacing.xxl
          } }
        >
          <AppRouter />
        </Box>
      </Box>
    </Box>
  )
}

export default AppScaffoldComponent