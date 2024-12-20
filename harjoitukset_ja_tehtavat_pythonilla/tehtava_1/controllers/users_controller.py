from flask import jsonify, request
from werkzeug.exceptions import NotFound

import models


# Controller -> model -> tietokanta -> model -> controller -> view
def get_all_users():
    users = models.User.get_all()
    return jsonify(models.User.list_to_json(users))


def get_user_by_id(user_id):
    try:
        user = models.User.get_by_id(user_id)
        return jsonify(user.to_json())
    except NotFound:
        return jsonify({"err": "user not found"}), 404
    except Exception as e:
        return jsonify({"err": str(e)}), 500


def create_user():
    try:
        data = request.get_json()
        new_user = models.User(0, data["username"], data["firstname"], data["lastname"])
        new_user.save()
        return jsonify(new_user.to_json())
    except Exception as e:
        return jsonify({"err": str(e)}), 500


def update_user_by_id(user_id):
    try:
        user = models.User.get_by_id(user_id)
        data = request.get_json()
        user.username = data["username"]
        user.firstname = data["firstname"]
        user.lastname = data["lastname"]
        user.save()
        return jsonify(user.to_json())
    except NotFound:
        return jsonify({"err": "user not found"}), 404


def delete_user_by_id(user_id):
    try:
        user = models.User.get_by_id(user_id)
        user.delete()
        return jsonify(), 200
    except NotFound:
        return jsonify({"err": "user not found"}), 404
    except Exception as e:
        return jsonify({"err": str(e)}), 500
