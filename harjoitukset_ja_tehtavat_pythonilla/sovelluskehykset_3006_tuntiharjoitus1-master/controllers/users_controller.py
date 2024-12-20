from flask import jsonify

import models


# Controller -> model -> tietokanta -> model -> controller -> view
def get_all_users():
    users = models.User.get_all()
    return jsonify(models.User.list_to_json(users))


def get_user():
    user = models.User.get_user()
    return jsonify(user)


def create_users():
    models.User.create()
    users = models.User.get_all()
    return jsonify(models.User.list_to_json(users))


def update_users():
    models.User.update_users()
    users = models.User.get_all()
    return jsonify(models.User.list_to_json(users))


def delete_users():
    models.User.delete_users()
    users = models.User.get_all()
    return jsonify(models.User.list_to_json(users))
