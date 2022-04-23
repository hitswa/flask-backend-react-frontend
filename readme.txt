pip install flask request response jsonify flask_sqlalchemy flask-cors

extension
alexcvzz.vscode-sqlite

create database
>>> python
>>> from complaint import db
>>> db.create_all()
>>> exit()

# start backend APIs
python api.py