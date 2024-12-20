import mysql.connector
import random


class User:
    def __init__(self, _id, username, firstname, lastname):
        self.id = _id
        self.username = username
        self.firstname = firstname
        self.lastname = lastname

    @staticmethod
    def create():
        with mysql.connector.connect(
            user="root", database="sovelluskehykset_bad1", password=""
        ) as con:
            with con.cursor(dictionary=True) as cur:
                cur.execute(
                    "INSERT INTO users (username, firstname, lastname) VALUES ('joni.tiainen', 'joni', 'tiainen')"
                )
                con.commit()

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
    def get_user():
        with mysql.connector.connect(
            user="root", database="sovelluskehykset_bad1", password=""
        ) as con:
            with con.cursor(dictionary=True) as cur:
                cur.execute("SELECT * FROM users WHERE id=1")
                user = cur.fetchall()
                print("##############users", user)

                return user

    @staticmethod
    def update_users():
        list_of_possible_lastname = ["virtanen", "peipponen", "tonttunen"]
        random_lastname = random.choice(list_of_possible_lastname)
        with mysql.connector.connect(
            user="root", database="sovelluskehykset_bad1", password=""
        ) as con:
            with con.cursor(dictionary=True) as cur:
                cur.execute(
                    f"UPDATE users SET lastname = '{random_lastname}' WHERE id = 1"
                )
                con.commit()

    @staticmethod
    def delete_users():
        with mysql.connector.connect(
            user="root", database="sovelluskehykset_bad1", password=""
        ) as con:
            with con.cursor(dictionary=True) as cur:
                cur.execute("DELETE FROM users WHERE lastname = 'tiainen'")
                con.commit()

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

    @staticmethod
    def create():
        with mysql.connector.connect(
            user="root", database="sovelluskehykset_bad1", password=""
        ) as con:
            with con.cursor(dictionary=True) as cur:
                cur.execute(
                    "INSERT INTO products (name, description) VALUES ('BMW', 'Auto kun auto')"
                )
                con.commit()

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
    def get_product():
        with mysql.connector.connect(
            user="root", database="sovelluskehykset_bad1", password=""
        ) as con:
            with con.cursor(dictionary=True) as cur:
                cur.execute("SELECT * FROM products WHERE id=1")
                product = cur.fetchall()
                print("##############products", product)

                return product

    @staticmethod
    def update_products():
        list_of_possible_products = ["mersu", "volvo", "bmw"]
        random_product = random.choice(list_of_possible_products)
        with mysql.connector.connect(
            user="root", database="sovelluskehykset_bad1", password=""
        ) as con:
            with con.cursor(dictionary=True) as cur:
                cur.execute(
                    f"UPDATE products SET name = '{random_product}' WHERE id = 1"
                )
                con.commit()

    @staticmethod
    def delete_products():
        with mysql.connector.connect(
            user="root", database="sovelluskehykset_bad1", password=""
        ) as con:
            with con.cursor(dictionary=True) as cur:
                cur.execute("DELETE FROM products WHERE name = 'bmw'")
                con.commit()

    def to_json(self):
        return {"id": self.id, "name": self.name, "description": self.description}

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
