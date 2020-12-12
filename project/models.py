from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) #student_id
    email = db.Column(db.String(100), unique=True) #student_email
    password = db.Column(db.String(100)) #student_password
    name = db.Column(db.String(1000)) #student_name

class Grade(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) #submission_id
    sid = db.Column(db.Integer) # student_id
    aid = db.Column(db.Integer) # assignment_id
    score = db.Column(db.Integer) # submission_score
    date = db.Column(db.Date)