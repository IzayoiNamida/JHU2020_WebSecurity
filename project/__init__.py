# init.py
import secrets
import string
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
# generate a 16 character secret token
def genSecretToken(N=16): 
	res = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(N))
	return str(res)

def create_app():
	app = Flask(__name__)

	app.config['SECRET_KEY'] = 'web-sec-final-proj'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
	# we are only accepting .zip files
	app.config['UPLOAD_EXTENSIONS'] = ['.zip']
	# For demonstration purposes, we store the uploads in the working directory of the server
	# but you should not do it in the production server
	app.config['UPLOAD_PATH'] = 'uploads'

	db.init_app(app)

	login_manager = LoginManager()
	login_manager.login_view = 'auth.login'
	login_manager.init_app(app)

	from .models import User

	@login_manager.user_loader
	def load_user(user_id):
		# since the user_id is just the primary key of our user table, use it in the query for the user
		return User.query.get(int(user_id))

	# blueprint for auth routes in our app
	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint)

	# blueprint for non-auth parts of app
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	return app