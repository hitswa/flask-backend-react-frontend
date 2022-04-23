import { useEffect, useState } from "react"
import axios from "axios";
import Chart from "./components/Chart/Chart"
import Table from "./components/Table/Table"

const App = () => {

    const [complaints, setComplaints] = useState(null);
    const [chartData, setChartData] = useState(null);

    useEffect(()=>{
        const fetchTableData = () => {
            axios
                .get('http://localhost:3001/complaint')
                .then(
                    (res)=>{
                        console.log({res})
                        if(res.data.success === true) {
                            setComplaints(res.data.data)
                        }
                    },
                    (err)=>{
                        console.log({err})
                    }
                )
                .catch(
                    (exc)=>{
                        console.log({exc})
                    }
                )
        }
        const fetchChartData = () => {
            axios
                .get('http://localhost:3001/complaint/trend')
                .then(
                    (res)=>{
                        console.log({res})
                        if(res.data.success === true) {
                            setChartData(res.data.data)
                        }
                    },
                    (err)=>{
                        console.log({err})
                    }
                )
                .catch(
                    (exc)=>{
                        console.log({exc})
                    }
                )
        }
        fetchTableData()
        fetchChartData()
    },[])

    return (
        <>
            <div className="container">
                <h1>Welcome to react app (Frontend)</h1>
                <Chart chartData={chartData} />
                <Table complaints={complaints} />
            </div>
        </>
    )
}

export default App;