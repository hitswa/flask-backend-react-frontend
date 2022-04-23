from flask_sqlalchemy import SQLAlchemy
from setting import *
import time

# Initializing our database
db = SQLAlchemy(app)

# the class Ticket will inherit the db.Model of SQLAlchemy
class Complaints(db.Model):
    __tablename__ = 'complaints' # creating a table with this name
    id = db.Column(db.Integer, primary_key=True) # declaring primary key
    ticket = db.Column(db.Integer,  nullable=False)
    user = db.Column(db.String(20),  nullable=False)
    ministry = db.Column(db.String(20),  nullable=False)
    department = db.Column(db.String(20),  nullable=False)
    state = db.Column(db.String(20),  nullable=False)
    city = db.Column(db.String(20),  nullable=False)
    complaint = db.Column(db.String(1000),  nullable=False)
    
    # this method we are defining will convert our output to json
    def json(self):
        # return json
        return {'id': self.id, 'ticket': self.ticket, 'user': self.user, 'ministry': self.ministry, 'department': self.department, 'state': self.state, 'city': self.city}

	# function to add ticket to database
    def create(_user, _ministry, _department, _state, _city, _complaint):
        # creating an instance of our Complaint constructor
        new_complaint = Complaints(
            ticket=int(time.time()), 
            user=_user, 
            ministry=_ministry, 
            department=_department, 
            state=_state, 
            city=_city , 
            complaint=_complaint 
        )
        db.session.add(new_complaint)  # add new complaint to database session
        db.session.commit()  # commit changes to session

	# function to get all complaints in our database
    def get_all():
        # return array of object
        return [Complaints.json(complaint) for complaint in Complaints.query.all()]

	# function to get complaint by ticket number from our database
    def get(_ticket):
        # retuen object
        return Complaints.json(Complaints.query.filter_by(ticket=_ticket).first())

	# function to update complaint by id from our database
    def update(_ticket, _user=None, _ministry=None, _department=None, _state=None, _city=None, _complaint=None):
		# if ticket is empty return response
        if _ticket == None:
        	return {}

        complaint_to_update = Complaints.query.filter_by(ticket=_ticket).first()

		# add update complaint to database session
        if _user != None:
        	complaint_to_update.user 		= _user
        if _ministry != None:
        	complaint_to_update.ministry 	= _ministry
        if _department != None:
        	complaint_to_update.department 	= _department
        if _state != None:
        	complaint_to_update.state 		= _state
        if _city != None:
        	complaint_to_update.city 		= _city
        if _complaint != None:
        	complaint_to_update.complaint   = _complaint

        db.session.commit() # commit changes to session

	# function to get complaint by ticket number from our database
    def delete(_ticket):
    	# filter complaint by ticket number and delete
        Complaints.query.filter_by(ticket=_ticket).delete()
        db.session.commit() # commit changes to session