import { FC } from 'react'
import { Socket } from 'socket.io-client'
import { Grid } from '@mui/material'

import { SGGraphModels } from 'graphModels/SCGraphModels'
import SocketGraph from 'view/components/SocketGraph'

interface ISGScreenComponentProps {
  socket: Socket;
}

const SGScreenComponent: FC<ISGScreenComponentProps> = ({
  socket,
}) => {
  return (
    <Grid
      container
      spacing={ 3 }
    >
      {SGGraphModels.map((graph, i) => (
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

export default SGScreenComponent