from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskr.routes.personal_management import personal_management


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqldb://root:root@localhost:3306/personaldb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
SQLAlchemy(app)
app.register_blueprint(personal_management)
