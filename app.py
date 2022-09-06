from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskr.routes.personal_management import personal_management
from config import DATABASE_CONNECTION_URI
from flask_migrate import Migrate
from flaskr.utils.db import db
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
SQLAlchemy(app)
migrate = Migrate(app, db)
app.register_blueprint(personal_management)
