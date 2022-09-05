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


@personal_management.route("/delete", methods=['GET'])
def delete_person():
    """
    It receives a JSON object with a id, then it queries the database for a person with that
    id, and if it finds one, it deletes it
    :return: A JSON object with the status and message.
    """
    try:
        # receive data and get element by document_id
        response: dict = request.get_json()
        person_id = response["id"]

        # delete Person object
        person = PersonalData.query.filter_by(id=person_id).first()

        # save new changes
        db.session.delete(person)
        db.session.commit()

        return jsonify({"status": "success",
                            "message": "Successfully deleted person"}), 200
    except Exception as error:
        return jsonify({"status": "error",
                        "message": "bad request"}), 400


@personal_management.route("/update/<id>", methods=['GET', 'POST'])
def update_person(id):
    """
    It receives a request, checks if it's a POST request, if it is, it receives the data, updates the
    object and saves it into the database, if it's not, it returns the object without changes
    :param id: The id of the person to be updated
    :return: The response is a JSON object with the following structure:
    """
    person = PersonalData.query.get(id)
    if request.method == 'POST':
        try:
            # receive data
            response: dict = request.get_json()
            person.document_type = response.get("document_type")
            person.document_id: int = response.get("document_id")
            person.first_name: str = response.get("first_name")
            person.last_name: str = response.get("last_name")

            # save the object into the database
            db.session.commit()

            return jsonify({"status": "success",
                            "message": "Successfully updated person"}), 200

        except Exception as error:
            return jsonify({"status": "error",
                            "message": "bad request"}), 400
    else:
        person_no_changes = person.to_dict()
        return jsonify({"status": "success",
                            "message": "Successfully get person",
                            "data": person_no_changes}), 200
