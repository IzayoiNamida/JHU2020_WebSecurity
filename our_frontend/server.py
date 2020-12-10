from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'web-sec-project-2020'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    # blueprint for auth routes in our app
    from blueprints.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from blueprints.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app