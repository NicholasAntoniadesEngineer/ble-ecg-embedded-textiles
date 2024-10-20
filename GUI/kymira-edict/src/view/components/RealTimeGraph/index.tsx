import { FC } from 'react'
import { Line, Chart } from 'react-chartjs-2'
import { ChartDataset } from 'chart.js'
import { Box, Typography, Grow } from '@mui/material'
import Loader from '../Loader'
import ThemeVariables from 'common/variables'
import StreamingPlugin from 'chartjs-plugin-streaming'
import 'chartjs-adapter-moment'
import 'react-loader-spinner/dist/loader/css/react-spinner-loader.css'

Chart.register(StreamingPlugin)

interface IRealTimeGraphComponentProps {
  showGraph?: boolean;
  graphName?: string;
  dataSets: {
    label: string;
    color: string;
    dataValue: string;
  }[];
  min?: number;
  max?: number;
  duration?: number;
  refresh?: number;
  showLegend?: boolean;
  showGrid?: boolean;
  handleRefresh: (chart: Chart, dataSet: { label: string, dataValue: string }) => void;
}

const RealTimeGraphComponent:FC<IRealTimeGraphComponentProps> = ({
  showGraph,
  graphName,
  dataSets,
  min,
  max,
  refresh = 1000,
  duration = 10000,
  showLegend = false,
  showGrid = false,
  handleRefresh,
}) => {
  const lines: ChartDataset<'line', []>[] = dataSets.map((set) => {
    return {
      label: set.label,
      labels: 'auto',
      borderColor: set.color,
      pointRadius: 0,
      fill: false,
      data: [],
      cubicInterpolationMode: 'monotone',
      tension: 0.8,
    }
  })

  return (
    <Box
      sx={ {
        padding: ThemeVariables.spacing.lg,
        backgroundColor: 'white',
        borderRadius: '10px',
        boxShadow: '0px 12px 24px #0000000F',
        minHeight: '500px',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        width: '100%',
      } }
    >
      <Box
        sx={ { width: '100%', minHeight: '400px' } }
      >
        <Typography
          variant="body1"
          sx={ {
            textAlign: 'center',
            fontWeight: ThemeVariables.fontWeights.medium,
            paddingBottom: ThemeVariables.spacing.md
          } }
        >
          {graphName}
        </Typography>
        {!showGraph && (
          <Box
            sx={ {
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              height: '100%',
              minHeight: '400px'
            } }
          >
            <Loader />
          </Box>
        )}
        <Grow
          in={ showGraph }
          unmountOnExit
          timeout={ { enter: 500, exit: 0 } }
        >
          <Box
            sx={ {
              minHeight: '400px',
            } }
          >
            <Line
              redraw
              data={ {
                datasets: lines,
              } }
              options={ {
                interaction: {
                  intersect: false
                },
                spanGaps: true,
                maintainAspectRatio: false,
                plugins: {
                  legend: {
                    display: showLegend,
                    position: 'bottom'
                  },
                },
                scales: {
                  y: {
                    grid: {
                      display: showGrid,
                    },
                    min: min,
                    max: max,
                  },
                  x: {
                    grid: {
                      display: false,
                    },
                    type: 'realtime',
                    realtime: {
                      ttl: undefined,
                      duration: duration,
                      delay: 2000,
                      refresh: refresh,
                      onRefresh: (chart) => {
                        dataSets.forEach((dataSet) => {
                          handleRefresh(chart, dataSet)
                        })
                      }
                    }
                  }
                }
              } }
            />
          </Box>
        </Grow>
      </Box>
    </Box>
  )
}

export default RealTimeGraphComponent