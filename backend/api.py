from complaint import *
import json

# route to get all complaints
@app.route('/complaint', methods=['GET'])
def get_complaints():
    return {
        "success": True,
        "message": "Success",
        "data": Complaints.get_all()
    }

# route to get complaint by ticket number
@app.route('/complaint/<int:ticket>', methods=['GET'])
def get_complaint_by_ticket_number(ticket):
    return {
        "success": True,
        "message": "Success",
        "data": Complaints.get(ticket)
    }

# route to add new complaint
@app.route('/complaint', methods=['POST'])
def add_complaint():
    request_data = request.get_json()  # getting data from request
    Complaints.create(
        request_data["user"], 
        request_data["ministry"], 
        request_data["department"], 
        request_data["state"], 
        request_data["city"], 
        request_data["complaint"]
    )
    return {
        "success": True,
        "message": "Complaint created successfully",
        "data": None
    }

# route to update complaint with PUT method
@app.route('/complaint/<int:ticket>', methods=['PUT'])
def update_complaint(ticket):
    request_data = request.get_json()
    Complaints.update(
        ticket,
        request_data["user"], 
        request_data["ministry"], 
        request_data["department"], 
        request_data["state"], 
        request_data["city"], 
        request_data["complaint"]
    )
    return {
        "success": True,
        "message": "Complaint updated successfully",
        "data": None
    }

# route to delete complaint using the DELETE method
@app.route('/complaint/<int:ticket>', methods=['DELETE'])
def remove_complaint(ticket):
    Complaints.delete(ticket)
    return {
        "success": True,
        "message": "Complaint deleted successfully",
        "data": None
    }

# route to delete complaint using the DELETE method
@app.route('/complaint/trend', methods=['GET'])
def get_chart_trend():
    return jsonify([
        {
            "label": 'Dataset 1',
            "data": [20,15,5,8,9,5,8,5,17,20,16,15],
            "backgroundColor": 'rgba(255, 99, 132, 0.5)'
        },
        {
            "label": 'Dataset 2',
            "data": [20,15,5,8,9,5,8,5,17,20,16,15],
            "backgroundColor": 'rgba(53, 162, 235, 0.5)'
        }
    ])

if __name__ == "__main__":
    app.run(port=3001, debug=True)