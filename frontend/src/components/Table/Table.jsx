import React from 'react';

const Table = (props) => {
    return (
        <>
            <h4>Table</h4>
            <table className='table'>
                <thead>
                    <tr>
                        <th>#</th>
                        <th>ticket</th>
                        <th>user</th>
                        <th>ministry</th>
                        <th>department</th>
                        <th>state</th>
                        <th>city</th>
                    </tr>
                </thead>
                <tbody>
                    {props.complaints && props.complaints.map((complaint, index)=>{
                        return (
                            <tr key={index}>
                                <td>{complaint.id}</td>
                                <td>{complaint.ticket}</td>
                                <td>{complaint.user}</td>
                                <td>{complaint.ministry}</td>
                                <td>{complaint.department}</td>
                                <td>{complaint.state}</td>
                                <td>{complaint.city}</td>
                            </tr>
                        )
                    })}
                </tbody>
            </table>
        </>
    )
}

export default Table;