from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import joinedload
import os

db_name = '/tmp/test.db'
if os.path.exists(db_name): os.remove(db_name)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(180), unique=True, nullable=False)

class UserCommData(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref = db.backref('usercommdata', lazy=True))
    phone = db.Column(db.String(40))
    email = db.Column(db.String(200))


db.create_all()

admin = User(username = 'admin')
guest = User(username = 'guest')

phone1 = UserCommData(phone = 'adminphone1', email = 'adminemail1', user = admin)
phone2 = UserCommData(phone = 'adminphone2', email = 'adminemail2', user = admin)
phone3 = UserCommData(phone = 'guestphone1', email = 'guestemail1', user = guest)


db.session.add(admin)
db.session.add(guest)
db.session.commit()

query = User.query.options(joinedload('usercommdata'))
for user in query:
    print(user.username)
    for item in user.usercommdata:
        print('\t' + item.phone, item.email)
