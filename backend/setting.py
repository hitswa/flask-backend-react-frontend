# importing libraries
from flask import Flask, request, Response, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# creating an instance of the flask app
app = Flask(__name__)
CORS(app, resources={r"/complaint/*": {"origins": "*"}})

# config your database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initializing our database
# db = SQLAlchemy(app)

