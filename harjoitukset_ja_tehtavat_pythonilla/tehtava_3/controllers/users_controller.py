from flask import jsonify, request
from werkzeug.exceptions import NotFound

from decorators.db_connection import get_db_connection
import models
from repositories.repository_factory import users_repository_factory


# Controller -> model -> tietokanta -> model -> controller -> view
@get_db_connection
def get_all_users(con):
    try:
        repo = users_repository_factory(con)
        users = repo.get_all()
        return jsonify(repo.list_to_json(users))
    except Exception as e:
        return jsonify({"err": str(e)}), 500


@get_db_connection
def get_user_by_id(con, user_id):
    try:
        repo = users_repository_factory(con)
        user = repo.get_by_id(user_id)
        return jsonify(repo.to_json(user))
    except NotFound:
        return jsonify({"err": "user not found"}), 404
    except Exception as e:
        return jsonify({"err": str(e)}), 500


@get_db_connection
def create_user(con):
    try:
        data = request.get_json()
        new_user = models.User(0, data["username"], data["firstname"], data["lastname"])
        repo = users_repository_factory(con)
        repo.save(new_user)
        return jsonify(repo.to_json(new_user))
    except Exception as e:
        return jsonify({"err": str(e)}), 500


@get_db_connection
def update_user_by_id(con, user_id):
    try:
        repo = users_repository_factory(con)
        user = repo.get_by_id(user_id)
        data = request.get_json()
        user.username = data["username"]
        user.firstname = data["firstname"]
        user.lastname = data["lastname"]
        repo.save(user)
        return jsonify(repo.to_json(user))
    except NotFound:
        return jsonify({"err": "user not found"}), 404


@get_db_connection
def delete_user_by_id(con, user_id):
    try:
        repo = users_repository_factory(con)
        user = repo.get_by_id(user_id)
        repo.delete(user)
        return jsonify(), 200
    except NotFound:
        return jsonify({"err": "user not found"}), 404
    except Exception as e:
        return jsonify({"err": str(e)}), 500
