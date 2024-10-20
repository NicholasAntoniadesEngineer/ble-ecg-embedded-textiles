import { FC, useRef } from 'react'
import { Socket } from 'socket.io-client'
import { Grid } from '@mui/material'

import { PPGGraphModel } from 'graphModels/PPGGraphModel'
import AddBookmark from 'view/components/AddBookmark'
import SocketGraph from 'view/components/SocketGraph'

interface IPPGScreenComponentProps {
  socket: Socket;
}

const PPGScreenComponent: FC<IPPGScreenComponentProps> = ({
  socket,
}) => {
  const tstampRef = useRef<number>()
  const getTs = (tstamp: number) => {
    tstampRef.current = tstamp
  }

  return (
    <>
      <AddBookmark ts={ tstampRef.current } />
      <Grid
        container
        spacing={ 3 }
      >
        {PPGGraphModel.map((graph, i) => (
          <Grid
            key={ graph.id }
            item
            xs={ 12 }
            lg={ i === 2 ? 12 : 6 }
          >
            <SocketGraph
              graph={ graph }
              socket={ socket }
              eventName={ graph.id }
              getTs={ getTs }
            />
          </Grid>
        ))}
      </Grid>
    </>
  )
}

export default PPGScreenComponent