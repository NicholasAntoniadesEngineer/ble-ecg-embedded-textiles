import { FC } from 'react'
import { Socket } from 'socket.io-client'
import { Grid } from '@mui/material'

import { EMGGraphModel } from 'graphModels/EMGGraphModel'
import SocketGraph from 'view/components/SocketGraph'

interface IEMGScreenComponentProps {
  socket: Socket;
}

const EMGScreenComponent: FC<IEMGScreenComponentProps> = ({
  socket,
}) => {
  return (
    <Grid
      container
      spacing={ 3 }
    >
      {EMGGraphModel.map((graph, i) => (
        <Grid
          key={ graph.id }
          item
          xs={ 12 }
          lg={ i === 2 ? 12 : 6  }
        >
          <SocketGraph
            graph={ graph }
            socket={ socket }
            eventName={ graph.id }
          />
        </Grid>
      ))}
    </Grid>
  )
}

export default EMGScreenComponent