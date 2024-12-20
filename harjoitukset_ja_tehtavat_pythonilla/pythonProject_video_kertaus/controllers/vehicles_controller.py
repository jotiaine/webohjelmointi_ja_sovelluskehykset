from flask import jsonify
from repositories.vehicles_mysql_repository import VehiclesMysqlRepository
from decorators.db_connection import get_db_conn
from decorators.vehicle_repository_decorator import get_vehicle_csv_repo


# @get_db_conn
# def get_all_vehicles(con):
#     try:
#         repo = VehiclesMysqlRepository(con)
#         vehicles = repo.get_all()
#         return jsonify(repo.list_to_json(vehicles))
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


@get_vehicle_csv_repo
def get_all_vehicles(repo):
    try:
        vehicles = repo.get_all()
        return jsonify(repo.list_to_json(vehicles))
    except Exception as e:
        return jsonify({"error": str(e)}), 500
