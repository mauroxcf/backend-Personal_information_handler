from app import app
from flaskr.utils.db import db

def create_app():
    with app.app_context():
        db.create_all()

    if __name__ == '__main__':
        app.run(debug=True, host="0.0.0.0")
