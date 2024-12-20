import csv
import models


class VehiclesCsvRepository:
    def __init__(self, _src):
        self.src = _src

    def get_all(self):
        reader = csv.DictReader(self.src, delimiter=";")
        vehicles = []
        for vehicle in reader:
            vehicles.append(
                models.Vehicle(vehicle["id"], vehicle["make"], vehicle["model"])
            )
        return vehicles

    def to_json(self, vehicle):
        return {"id": vehicle.id, "make": vehicle.make, "model": vehicle.model}

    def list_to_json(self, vehicles):
        return [self.to_json(vehicle) for vehicle in vehicles]
