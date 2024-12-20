import models


class VehiclesMysqlRepository:
    def __init__(self, _db):
        self.db = _db

    def get_all(self):
        with self.db.cursor() as cur:
            cur.execute("SELECT id, make, model FROM vehicles")
            result = cur.fetchall()
            vehicles = []
            for row in result:
                vehicles.append(models.Vehicle(row[0], row[1], row[2]))
            return vehicles

    def to_json(self, vehicle):
        return {"id": vehicle.id, "make": vehicle.make, "model": vehicle.model}

    def list_to_json(self, vehicles):
        vehicles_json_list = []
        for vehicle in vehicles:
            vehicles_json_list.append(self.to_json(vehicle))
        return vehicles_json_list
