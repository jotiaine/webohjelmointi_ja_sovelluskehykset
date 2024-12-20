import models
import psycopg2


class UsersPostgresRepository:
    def __init__(self):
        self.con = psycopg2.connect(
            user="postgres", password="683652", database="sovelluskehykset_bad1"
        )

    def __del__(self):
        if self.con is not None and not self.con.closed():
            self.con.close()

    def get_all(self):
        with self.con.cursor() as cur:
            cur.execute("SELECT * FROM users")
            result = cur.fetchall()
            users = []
            for user in result:
                users.append(models.User(user[0], user[1], user[2], user[3]))

            return users
