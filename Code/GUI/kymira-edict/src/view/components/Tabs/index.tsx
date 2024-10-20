import { FC, SyntheticEvent } from 'react'
import { Tabs, Tab } from '@mui/material'
import ThemeVariables from 'common/variables'

interface ITabsComponentProps {
  activeTab: number | boolean;
  tabs: {
    id: string;
    label: string;
    type: string;
  }[];
  handleChange: (e: SyntheticEvent, newValue: number) => void;
}

const TabsComponent: FC<ITabsComponentProps> = ({
  activeTab,
  tabs,
  handleChange,
}) => {
  return (
    <Tabs
      variant="scrollable"
      scrollButtons="auto"
      value={ activeTab }
      onChange={ (e, value) => handleChange(e, value) }
      sx={ {
        paddingBottom: ThemeVariables.spacing.xl
      } }
    >
      {tabs.map((item) => (
        <Tab
          key={ item.id }
          label={ item.label }
          id={ item.type }
        />
      ))}
    </Tabs>
  )
}

export default TabsComponent