# main.py

import datetime
import os
from flask import Blueprint, render_template, request, redirect, abort, url_for, current_app, flash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from .models import Grade
from . import db, genSecretToken

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
	# get all the scores associated with the cuurent logged student
	grades = Grade.query.filter_by(sid=current_user.id).all()
	#grades = [(grade.sid, grade.aid, grade.score, grade.date) for grade in grades]
	return render_template('gradebook.html', grades=grades)

@main.route('/submit', methods=['POST'])
@login_required
def submit():
	token = genSecretToken()
	print(token)
	print(request)
	uploaded_file = request.files['file']
	# we use secure_filename from the werkzeug.utils library to sanitize the filename
	# of the uploaded files
	filename_full = secure_filename(uploaded_file.filename)
	if filename_full != '':
		file_name, file_extension = os.path.splitext(filename_full)
		if file_extension not in current_app.config['UPLOAD_EXTENSIONS']:
			return "unsupported file format"
		new_dir_path = os.path.join(current_app.config['UPLOAD_PATH'], token)
		print(new_dir_path)
		if not os.path.exists(new_dir_path):
			os.makedirs(new_dir_path)
		uploaded_file.save(os.path.join(current_app.config['UPLOAD_PATH'], token, file_name+file_extension))
	else:
		return redirect(url_for('main.assignment_1'))

	flash('We have received your submission.')
	return redirect(url_for('main.assignment_1'))