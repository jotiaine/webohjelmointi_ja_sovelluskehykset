from flask import jsonify, render_template

import models
from repositories.vehicles_repository import VehicleRepositoryMysql


def get_all_vehicles_api():
    repo = VehicleRepositoryMysql()
    vehicles = repo.get_all()
    return jsonify(models.Vehicle.list_to_json(vehicles))


def get_all_vehicles_html_page():
    repo = VehicleRepositoryMysql()
    vehicles = repo.get_all()
    return render_template("vehicles/index.html", vehicles_param=vehicles)


def get_vehicle():
    vehicle = models.Vehicle.get_vehicle()
    return jsonify(vehicle)
