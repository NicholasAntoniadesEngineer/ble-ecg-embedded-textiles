import { FC, useState, SyntheticEvent, useRef } from 'react'
import { Socket } from 'socket.io-client'
import { Grid, Button, Box } from '@mui/material'

import { ECGGraphsModel } from 'graphModels/ECGGraphModel'

import Tabs from 'view/components/Tabs'
import AddBookmark from 'view/components/AddBookmark'
import SocketGraph from 'view/components/SocketGraph'

interface IECGScreenComponentProps {
  socket: Socket;
}

const ECGScreenComponent:FC<IECGScreenComponentProps> = ({
  socket,
}) => {
  const tstampRef = useRef<number>()
  const [activeTab, updateActiveTab] = useState<number | boolean>(0)
  const [showAll, toggleShowAll] = useState(false)
  const handleChange = (e: SyntheticEvent, newValue: number) => {
    updateActiveTab(newValue)
    toggleShowAll(false)
  }

  const tabs = ECGGraphsModel.map((item) => {
    return {
      id: item.id,
      label: item.label,
      type: item.label
    }
  })

  const handleShowAll = () => {
    toggleShowAll(!showAll)

    if (typeof activeTab !== 'number') {
      updateActiveTab(0)
    } else {
      updateActiveTab(false)
    }
  }

  const getTs = (tstamp: number) => {
    tstampRef.current =  tstamp
  }

  return (
    <>
      <AddBookmark ts={ tstampRef.current }/>
      <Box
        sx={ {
          display: 'flex',
          alignItems: 'flex-start',
        } }
      >
        <Tabs
          activeTab={ activeTab }
          tabs={ tabs }
          handleChange={ handleChange }
        />
        <Button
          size='small'
          variant={ showAll ? 'contained' : 'outlined' }
          color="primary"
          onClick={ handleShowAll }
          sx={ {
            marginTop: '0.5em',
            marginLeft: '1em'
          } }
        >
          {`${showAll ? 'Hide' : 'Show'} all Graphs`}
        </Button>
      </Box>
      {showAll ? (
        <Grid
          container
          spacing={ 3 }
        >
          {ECGGraphsModel.map((item) => (
            <Grid
              item
              sm={ 4 }
              key={ item.id }
            >
              <SocketGraph
                graph={ item }
                socket={ socket }
                eventName={ item.id }
                getTs={ getTs }
              />
            </Grid>
          ))}
        </Grid>
      ) : (
        <>
          {ECGGraphsModel.map((item, index) => {
            return activeTab === index && (
              <SocketGraph
                key={ item.id }
                graph={ item }
                socket={ socket }
                eventName={ item.id }
                getTs={ getTs }
              />
            )
          })}
        </>
      )}
    </>
  )
}

export default ECGScreenComponent