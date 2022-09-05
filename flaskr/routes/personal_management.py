from flask import Blueprint, request, jsonify
from flaskr.utils.db import db
from flaskr.models import PersonalData, DocumentType
import json

personal_management = Blueprint('personal Management', __name__)

@personal_management.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@personal_management.route("/all", methods=['GET'])
def get_all_person():
    """
    It creates a dictionary, queries the database for all persons, and then returns a json response
    :return: A tuple of a jsonified dictionary and a status code.
    """
    persons = PersonalData.query.all()
    person_list = []
    for person in persons:
        person_list.append(person.to_dict())

    return jsonify({"status": "success",
                        "message": "Successfully return all persons",
                        "data": person_list}), 200


@personal_management.route("/new", methods=['POST'])
def add_person():
    """
    It receives a JSON object, creates a new Person object, and saves it into the database
    :return: a json object with the status and message.
    """
    if request.method == 'POST':
        try:
            # receive data
            response: dict = request.get_json()
            document_type = response.get("document_type")
            document_id: int = response.get("document_id")
            first_name: str = response.get("first_name")
            last_name: str = response.get("last_name")
            print(response)
            # create a new Person object
            new_person = PersonalData(document_type, document_id, first_name, last_name)
            # save the object into the database
            db.session.add(new_person)
            db.session.commit()

            return jsonify({"status": "success",
                            "message": "Successfully created person"}), 200

        except Exception as error:
            return jsonify({"status": "error",
                            "message": "bad request"}), 400
