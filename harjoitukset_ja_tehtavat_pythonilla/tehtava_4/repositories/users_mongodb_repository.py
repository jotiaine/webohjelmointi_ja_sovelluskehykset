import models
from werkzeug.exceptions import NotFound
from bson.objectid import ObjectId


class UsersMongoDBRepository:
    def __init__(self, con):
        self.con = con
        self.mydb = con["sovelluskehykset_bad1"]
        self.mycol = self.mydb["users"]

    def __del__(self):
        if self.con is not None:
            self.con.close()

    def get_all(self):
        users = []
        for user in self.mycol.find():
            users.append(
                models.User(
                    str(user["_id"]),
                    user["username"],
                    user["firstname"],
                    user["lastname"],
                )
            )
        return users

    def get_by_id(self, _id):
        myquery = {"_id": ObjectId(_id)}
        user = self.mycol.find_one(myquery)
        if user is None:
            raise NotFound("user not found")
        return models.User(
            str(user["_id"]), user["username"], user["firstname"], user["lastname"]
        )

    def _create(self, user):
        try:
            mydict = {
                "username": user.username,
                "firstname": user.firstname,
                "lastname": user.lastname,
            }
            x = self.mycol.insert_one(mydict)
            user.id = str(x.inserted_id)
        except Exception as e:
            raise e

    def _update(self, user):
        try:
            myquery = {"_id": ObjectId(user.id)}
            newvalues = {
                "$set": {
                    "username": user.username,
                    "firstname": user.firstname,
                    "lastname": user.lastname,
                }
            }
            self.mycol.update_one(myquery, newvalues)
        except Exception as e:
            raise e

    def delete(self, user):
        try:
            myquery = {"_id": ObjectId(user.id)}
            self.mycol.delete_one(myquery)
        except Exception as e:
            raise e

    def save(self, user):
        if user.id == 0:
            self._create(user)
        else:
            self._update(user)

    def to_json(self, user):
        return {
            "id": user.id,
            "username": user.username,
            "firstname": user.firstname,
            "lastname": user.lastname,
        }

    def list_to_json(self, users_list):
        users_json_list = []
        for u in users_list:
            users_json_list.append(self.to_json(u))
        return users_json_list
