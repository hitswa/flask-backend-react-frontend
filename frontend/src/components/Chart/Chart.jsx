import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';

ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend
);

export const options = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Chart.js Bar Chart',
      },
    },
};

const labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];

const dummyData = [
  {
    label: 'Dataset 1',
    data: [20, 15, 18, 17, 19, 15, 17, 16, 19, 14, 12, 13],
    backgroundColor: 'rgba(255, 99, 132, 0.5)',
  },
  {
    label: 'Dataset 2',
    data: [20, 15, 18, 17, 19, 15, 17, 16, 19, 14, 12, 13],
    backgroundColor: 'rgba(53, 162, 235, 0.5)',
  },
]

const Chart = (props) => {
    return (
        <>
            <h2>Chart</h2>
            <Bar options={options} data={{
                labels,
                datasets: props.chartData !== null ? props.chartData : dummyData
            }} />
        </>
    )
}

export default Chart;