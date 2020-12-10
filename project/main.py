# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    return render_template('index.html')

@main.route('/gradebook')
@login_required
def gradebook():
    return render_template('gradebook.html', name=current_user.name)