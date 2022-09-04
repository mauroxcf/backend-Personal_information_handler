from flask import Blueprint, request, jsonify
from flaskr.utils.db import db
from flaskr.utils.helper import create_dict
from flaskr.models import PersonalData
import json

personal_management = Blueprint('personal Management', __name__)

@personal_management.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@personal_management.route("/all", methods=['GET'])
def get_all_person():
    try:
        mydict = create_dict()
        persons = PersonalData.query.all()

        """ for row in persons:
            mydict.add(row[0],({"document_type":row[1],"document_id":row[2],"phone":row[3],"last_name":row[4]})) """

        #json_dump = json.dumps(persons)
        #json_dump = json.dumps(mydict, indent=2, sort_keys=True)
        #print(json_dump)
        return jsonify({"status": "success",
                            "message": "Successfully return all persons"}), 200
    except Exception as error:
        return jsonify({"status": "error",
                        "message": "bad request",
                        "data": "fixing"}), 400


@personal_management.route("/new", methods=['POST'])
def add_person():
    if request.method == 'POST':
        try:
            # receive data
            response: dict = request.get_json()
            document_type = response.get("document_type")
            document_id: int = response.get("document_id")
            first_name: str = response.get("first_name")
            lastname: str = response.get("last_name")
            print(response)
            # create a new Person object
            new_person = PersonalData(document_type, document_id, first_name, last_name)
            #json_dump = json.dumps(new_person)

            # save the object into the database
            db.session.add(new_person)
            db.session.commit()

            return jsonify({"status": "success",
                            "message": "Successfully created person",
                            "data": "fixing"}), 200

        except Exception as error:
            return jsonify({"status": "error",
                            "message": "bad request"}), 400
