import { FC } from 'react'
import { Socket } from 'socket.io-client'
import { Grid, Button, Box } from '@mui/material'

import { IGraphModel } from 'models/graphModel'
import { IMULimbsModel } from 'models/IMULimbsModel'

import SocketGraph from 'view/components/SocketGraph'
import ThemeVariables from 'common/variables'

interface IMultiIMUScreenComponentProps {
  socket: Socket;
  selectedData: IGraphModel[];
  activeButton: IMULimbsModel;
  handleSetData: (limb: IMULimbsModel) => void;
}

const MultiIMUScreenComponent: FC<IMultiIMUScreenComponentProps> = ({
  socket,
  selectedData,
  activeButton,
  handleSetData,
}) => {
  const buttons = [
    {
      text: 'Left Leg',
      type: IMULimbsModel.leftLeg,
      onClick: () => handleSetData(IMULimbsModel.leftLeg)
    },
    {
      text: 'Right Leg',
      type: IMULimbsModel.rightLeg,
      onClick: () => handleSetData(IMULimbsModel.rightLeg)
    },
    {
      text: 'Left Arm',
      type: IMULimbsModel.leftArm,
      onClick: () => handleSetData(IMULimbsModel.leftArm)
    },
    {
      text: 'Right Arm',
      type: IMULimbsModel.rightArm,
      onClick: () => handleSetData(IMULimbsModel.rightArm)
    },
    {
      text: 'Torso',
      type: IMULimbsModel.torso,
      onClick: () => handleSetData(IMULimbsModel.torso)
    }
  ]

  return (
    <>
      <Box
        sx={ {
          marginBottom: ThemeVariables.spacing.xl
        } }
      >
        {buttons.map((button) => (
          <Button
            key={ button.text }
            variant={ activeButton === button.type ? 'contained' : 'outlined' }
            color="primary"
            size="small"
            onClick={ button.onClick }
            sx={ {
              marginRight: ThemeVariables.spacing.md,
            } }
          >
            {button.text}
          </Button>
        ))}
      </Box>
      <Grid
        container
        spacing={ 3 }
      >
        {selectedData.map((item, i) => {
          return (
            <Grid
              key={ item.id }
              item
              xs={ 12 }
              lg={ i === 2 ? 12 : 6 }
            >
              <SocketGraph
                graph={ item }
                socket={ socket }
                eventName={ item.id }
              />
            </Grid>
          )
        })}
      </Grid>
    </>
  )
}

export default MultiIMUScreenComponent