from . import db
from flask_login import UserMixin


class users(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String (150), unique=True)
    first_name = db.Column(db.String (500))
    last_name = db.Column(db.String (500))
    password = db.Column(db.String)
    
class tasks(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    descripition = db.Column(db.String(500))
    status = db.Column(db.String (50))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
