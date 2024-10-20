import { FC, useState } from 'react'
import { Collapse, Button, Grid } from '@mui/material'
import ThemeVariables from 'common/variables'
import TextField from '../TextField'

interface IAddBookmarkComponentProps {
  showBookmarkBar: boolean;
  ts: number | undefined;
  addBookmark: (note: string, tstamp: number) => void
}

const AddBookmarkComponent: FC<IAddBookmarkComponentProps> = ({
  showBookmarkBar,
  ts,
  addBookmark
}) => {
  const [note, setNote] = useState('')
  const [error, setError] = useState(false)

  const handleBookmark = () => {
    if (note === '') {
      setError(true)

      return
    }

    ts && addBookmark(note, ts)
  }

  return (
    <Collapse in={ showBookmarkBar }>
      <Grid
        container
        justifyContent="flex-end"
        sx={ {
          pb: ThemeVariables.spacing.lg,
          pt: ThemeVariables.spacing.xxs
        } }
      >
        <Grid
          item
          xs={ 12 }
          md={ 9 }
          lg={ 6 }
        >
          <TextField
            value={ note }
            onChange={ (e) => setNote(e) }
            error={ error }
            onBlur={ () => setError(false) }
            size="small"
          />
        </Grid>
        <Grid
          item
          xs={ 12 }
          md={ 3 }
          lg={ 2 }
        >
          <Button
            onClick={ handleBookmark }
            sx={ {
              minWidth: '100%',
              borderTopLeftRadius: 0,
              borderBottomLeftRadius: 0,
            } }
          >Add Bookmark
          </Button>
        </Grid>
      </Grid>
    </Collapse>
  )
}

export default AddBookmarkComponent
