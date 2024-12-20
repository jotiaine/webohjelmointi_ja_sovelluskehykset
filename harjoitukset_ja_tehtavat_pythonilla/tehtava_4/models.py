import mysql.connector
from werkzeug.exceptions import NotFound


class User:
    def __init__(self, _id, username, firstname, lastname):
        self.id = _id
        self.username = username
        self.firstname = firstname
        self.lastname = lastname


class Product:
    def __init__(self, _id, name, description):
        self.id = _id
        self.name = name
        self.description = description


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
