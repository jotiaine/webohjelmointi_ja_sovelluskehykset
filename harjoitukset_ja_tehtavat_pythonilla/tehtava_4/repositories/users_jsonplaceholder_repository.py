import requests
import models
from werkzeug.exceptions import NotFound


class UsersJsonPlaceholderRepository:
    def __init__(self):
        self.url = "https://jsonplaceholder.typicode.com/users"

    def __del__(self):
        pass

    def get_all(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            result = response.json()
            users = []
            for user in result:
                users.append(
                    models.User(
                        user["id"],
                        user["name"],  # username
                        user["username"],  # firstname
                        user["email"],  # lastname
                    )
                )
            return users

    def get_by_id(self, _id):
        response = requests.get(f"{self.url}/{_id}")
        if response.status_code == 200:
            user = response.json()
            return models.User(
                user["id"],
                user["name"],  # username
                user["username"],  # firstname
                user["email"],  # lastname
            )

    def to_json(self, user):
        firstname = user.username.split(" ")[0]
        lastname = user.username.split(" ")[1]
        return {
            "id": user.id,
            "username": user.username,  # name
            "firstname": firstname,  # username
            "lastname": lastname,  # email
        }

    def list_to_json(self, users_list):
        users_json_list = []
        for u in users_list:
            users_json_list.append(self.to_json(u))
        return users_json_list
