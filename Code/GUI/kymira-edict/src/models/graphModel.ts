export interface IGraphModel {
  id: string;
  label: string;
  min?: number;
  max?: number;
  refreshRate: number;
  duration: number;
  dataSets: {
    label: string;
    color: string;
    dataValue: string;
  }[]
}