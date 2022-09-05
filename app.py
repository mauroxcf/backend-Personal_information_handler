from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskr.routes.personal_management import personal_management
from config import DATABASE_CONNECTION_URI


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
SQLAlchemy(app)
app.register_blueprint(personal_management)
