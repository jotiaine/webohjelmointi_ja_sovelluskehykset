import models
from werkzeug.exceptions import NotFound


# Data access layer
class UsersMysqlRepository:
    def __init__(self, con):
        self.con = con

    def __del__(self):
        if self.con is not None and self.con.is_connected():
            self.con.close()

    def get_all(self):
        with self.con.cursor() as cur:
            cur.execute("SELECT * FROM users")
            result = cur.fetchall()
            users = []
            for user in result:
                users.append(models.User(user[0], user[1], user[2], user[3]))

            return users

    def get_by_id(self, _id):
        with self.con.cursor(dictionary=True) as cur:
            cur.execute("SELECT * FROM users WHERE id=%s", (_id,))
            user = cur.fetchone()
            if user is None:
                raise NotFound("user not found")
            return models.User(
                user["id"], user["username"], user["firstname"], user["lastname"]
            )

    def _create(self, user):
        try:
            with self.con.cursor(dictionary=True) as cur:
                cur.execute(
                    "INSERT INTO users (username, firstname, lastname) VALUES (%s, %s, %s)",
                    (user.username, user.firstname, user.lastname),
                )
                self.con.commit()
                user.id = cur.lastrowid
        except Exception as e:
            self.con.rollback()
            raise e

    def _update(self, user):
        try:
            with self.con.cursor(dictionary=True) as cur:
                cur.execute(
                    "UPDATE users SET username = %s, firstname = %s, lastname = %s  WHERE id = %s",
                    (
                        user.username,
                        user.firstname,
                        user.lastname,
                        user.id,
                    ),
                )
                self.con.commit()
        except Exception as e:
            self.con.rollback()
            raise e

    def delete(self, user):
        try:
            with self.con.cursor(dictionary=True) as cur:
                cur.execute("DELETE FROM users WHERE id = %s", (user.id,))
                self.con.commit()
        except Exception as e:
            self.con.rollback()
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
