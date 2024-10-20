import { FC, useEffect, useRef, useState, useMemo } from 'react'
import RealTimeGraph from 'view/components/RealTimeGraph'
import { IGraphModel } from 'models/graphModel'
import { Chart } from 'react-chartjs-2'
import { Socket } from 'socket.io-client'

interface ISocketGraphComponentProps {
  graph: IGraphModel;
  socket: Socket
  eventName: string;
  getTs?: (tstamp: number) => void;
}

const SocketGraphComponent:FC<ISocketGraphComponentProps> = ({
  graph,
  socket,
  eventName,
  getTs,
}) => {
  const socketData = useRef<{ tstamp: number }>()
  const [showGraph, updateShowGraph] = useState(false)

  const handleRefresh = (chart: Chart, dataSet: { label: string, dataValue: string }) => {
    if (socketData.current) {
      const data = socketData.current[dataSet.dataValue]
      const chartSet = chart.data.datasets.filter((item) => item.label === dataSet.label)

      getTs && getTs(socketData.current.tstamp)

      chartSet[0].data.push({
        x: Date.now(),
        y: data,
      })

      chart.update('quiet')
    }
  }

  useEffect(() => {
    socket.on(eventName, (message) => {
      socketData.current = message

      if (!showGraph && socket.connected) {
        updateShowGraph(true)
      }
    })

    return () => {
      socket.off()
    }
  }, [socket, eventName])

  return (
    useMemo(() => (
      <RealTimeGraph
        showGraph={ showGraph }
        handleRefresh={ handleRefresh }
        min={ graph.min }
        max={ graph.max }
        duration={ graph.duration }
        refresh={ graph.refreshRate }
        showLegend
        showGrid
        dataSets={ graph.dataSets }
      />
    ), [showGraph])
  )
}

export default SocketGraphComponent