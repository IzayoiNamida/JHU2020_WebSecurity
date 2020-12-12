# main.py

import datetime
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Grade
from . import db

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def dashboard():
    return render_template('dashboard.html')

@main.route('/assignments')
@login_required
def assignments():
    return render_template('assignments.html')

@main.route('/assignment/1')
@login_required
def assignment_1():
    return render_template('assignment1.html')

@main.route('/gradebook')
@login_required
def gradebook():
    grades = Grade.query.filter_by(sid=current_user.id).all()
    #grades = [(grade.sid, grade.aid, grade.score, grade.date) for grade in grades]
    return render_template('gradebook.html', grades=grades)