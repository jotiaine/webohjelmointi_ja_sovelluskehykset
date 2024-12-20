import mysql.connector
from werkzeug.exceptions import NotFound


class User:
    def __init__(self, _id, username, firstname, lastname):
        self.id = _id
        self.username = username
        self.firstname = firstname
        self.lastname = lastname

    def _create(self):
        try:
            with mysql.connector.connect(
                user="root", database="sovelluskehykset_bad1", password=""
            ) as con:
                with con.cursor(dictionary=True) as cur:
                    cur.execute(
                        "INSERT INTO users (username, firstname, lastname) VALUES (%s, %s, %s)",
                        (self.username, self.firstname, self.lastname),
                    )
                    con.commit()
                    self.id = cur.lastrowid
        except Exception as e:
            con.rollback()
            raise e

    @staticmethod
    def get_all():
        with mysql.connector.connect(
            user="root", database="sovelluskehykset_bad1", password=""
        ) as con:
            with con.cursor(dictionary=True) as cur:
                cur.execute("SELECT * FROM users")
                users = cur.fetchall()
                users_list = []
                for u in users:
                    user = User(u["id"], u["username"], u["firstname"], u["lastname"])
                    users_list.append(user)

                return users_list

    @staticmethod
    def get_by_id(_id):
        with mysql.connector.connect(
            user="root", database="sovelluskehykset_bad1", password=""
        ) as con:
            with con.cursor(dictionary=True) as cur:
                cur.execute("SELECT * FROM users WHERE id=%s", (_id,))
                user = cur.fetchone()
                if user is None:
                    raise NotFound("user not found")
                return User(
                    user["id"], user["username"], user["firstname"], user["lastname"]
                )

    def _update(self):
        try:
            with mysql.connector.connect(
                user="root", database="sovelluskehykset_bad1", password=""
            ) as con:
                with con.cursor(dictionary=True) as cur:
                    cur.execute(
                        "UPDATE users SET username = %s, firstname = %s, lastname = %s  WHERE id = %s",
                        (
                            self.username,
                            self.firstname,
                            self.lastname,
                            self.id,
                        ),
                    )
                    con.commit()
        except Exception as e:
            con.rollback()
            raise e

    def save(self):
        if self.id == 0:
            self._create()
        else:
            self._update()

    def delete(self):
        try:
            with mysql.connector.connect(
                user="root", database="sovelluskehykset_bad1", password=""
            ) as con:
                with con.cursor(dictionary=True) as cur:
                    cur.execute("DELETE FROM users WHERE id = %s", (self.id,))
                    con.commit()
        except Exception as e:
            con.rollback()
            raise e

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
        }

    @staticmethod
    def list_to_json(users_list):
        users_json_list = []
        for u in users_list:
            users_json_list.append(u.to_json())
        return users_json_list


class Product:
    def __init__(self, _id, name, description):
        self.id = _id
        self.name = name
        self.description = description

    def _create(self):
        try:
            with mysql.connector.connect(
                user="root", database="sovelluskehykset_bad1", password=""
            ) as con:
                with con.cursor(dictionary=True) as cur:
                    cur.execute(
                        "INSERT INTO products (name, description) VALUES (%s, %s)",
                        (self.name, self.description),
                    )
                    con.commit()
                    self.id = cur.lastrowid
        except Exception as e:
            con.rollback()
            raise e

    @staticmethod
    def get_all():
        with mysql.connector.connect(
            user="root", database="sovelluskehykset_bad1", password=""
        ) as con:
            with con.cursor(dictionary=True) as cur:
                cur.execute("SELECT * FROM products")
                products = cur.fetchall()
                products_list = []
                for p in products:
                    product = Product(p["id"], p["name"], p["description"])
                    products_list.append(product)

                return products_list

    @staticmethod
    def get_by_id(_id):
        with mysql.connector.connect(
            user="root", database="sovelluskehykset_bad1", password=""
        ) as con:
            with con.cursor(dictionary=True) as cur:
                cur.execute("SELECT * FROM products WHERE id = %s", (_id,))
                product = cur.fetchone()
                if product is None:
                    raise NotFound("product not found")
                return Product(product["id"], product["name"], product["description"])

    def _update(self):
        try:
            with mysql.connector.connect(
                user="root", database="sovelluskehykset_bad1", password=""
            ) as con:
                with con.cursor(dictionary=True) as cur:
                    cur.execute(
                        "UPDATE products SET name = %s, description = %s WHERE id = %s",
                        (self.name, self.description, self.id),
                    )
                    con.commit()
        except Exception as e:
            con.rollback()
            raise e

    def save(self):
        if self.id == 0:
            self._create()
        else:
            self._update()

    def delete(self):
        try:
            with mysql.connector.connect(
                user="root", database="sovelluskehykset_bad1", password=""
            ) as con:
                with con.cursor(dictionary=True) as cur:
                    cur.execute("DELETE FROM products WHERE id = %s", (self.id,))
                    con.commit()
        except Exception as e:
            con.rollback()
            raise e

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }

    @staticmethod
    def list_to_json(products_list):
        products_json_list = []
        for p in products_list:
            products_json_list.append(p.to_json())
        return products_json_list


class Vehicle:
    def __init__(self, _id, make, model):
        self.id = _id
        self.make = make
        self.model = model

    @staticmethod
    def get_all():
        with mysql.connector.connect(
            user="root", database="sovelluskehykset_bad1", password=""
        ) as con:
            with con.cursor(dictionary=True) as cur:
                cur.execute("SELECT * FROM vehicles")
                vehicles = cur.fetchall()
                vehichle_list = []
                for v in vehicles:
                    vehicle = Vehicle(v["id"], v["make"], v["model"])
                    vehichle_list.append(vehicle)
                return vehichle_list

    @staticmethod
    def get_vehicle():
        with mysql.connector.connect(
            user="root", database="sovelluskehykset_bad1", password=""
        ) as con:
            with con.cursor(dictionary=True) as cur:
                cur.execute("SELECT * FROM vehicles WHERE id=1")
                vehicle = cur.fetchall()
                print("##############vehicles", vehicle)

                return vehicle

    def to_json(self):
        return {"id": self.id, "make": self.make, "model": self.model}

    @staticmethod
    def list_to_json(vehicle_list):
        vehichles_json_list = []
        for v in vehicle_list:
            vehichles_json_list.append(v.to_json())

        return vehichles_json_list
