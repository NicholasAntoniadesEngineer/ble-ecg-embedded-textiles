import { FC, useRef } from 'react'
import { Socket } from 'socket.io-client'
import { Grid } from '@mui/material'

import { IMUGraphsModel } from 'graphModels/IMUGraphModel'
import AddBookmark from 'view/components/AddBookmark'
import SocketGraph from 'view/components/SocketGraph'

interface IIMUScreenComponentProps {
  socket: Socket;
}

const IMUScreenComponent: FC<IIMUScreenComponentProps> = ({
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
        {IMUGraphsModel.map((graph) => (
          <Grid
            key={ graph.id }
            item
            xs={ 12 }
            lg={ 12 }
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

export default IMUScreenComponent