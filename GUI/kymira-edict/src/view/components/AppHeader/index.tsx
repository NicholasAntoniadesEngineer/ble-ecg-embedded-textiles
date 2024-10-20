import { FC } from 'react'
import { Box, Button } from '@mui/material'
import PageTitle from '../PageTitle'

interface IAppHeaderComponentProps {
  title?: string;
  showBookmarkButton?: boolean;
  openBookmark: () => void;
}

const AppHeaderComponent:FC<IAppHeaderComponentProps> = ({
  title,
  showBookmarkButton,
  openBookmark,
}) => {
  return (
    <Box>
      <Box
        sx={ {
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
        } }
      >
        <PageTitle title={ title }/>
        {showBookmarkButton && (
          <Button
            size='small'
            variant='outlined'
            color="primary"
            onClick={ openBookmark }
          >
            Toggle Bookmark bar
          </Button>
        )}
      </Box>
    </Box>
  )
}

export default AppHeaderComponent