from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	email = db.Column(db.String(120), unique=True)

	def __init__(self, username, email):
    		self.username = username
    		self.email = email

	def __repr__(self):
    		return 'User:'+str(self.username)+', Email:'+str(self.email)

@app.route('/users')
def users():
	string = User.query.all()
	return render_template('users.html', userlist = string)

if __name__ == '__main__':

    app.run()
