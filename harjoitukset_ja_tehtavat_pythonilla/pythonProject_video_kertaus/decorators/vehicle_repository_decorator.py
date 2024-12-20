from repositories.vehicles_csv_repository import VehiclesCsvRepository


def get_vehicle_csv_repo(route_handler_func):
    def wrapper(*args, **kwargs):
        with open("vehicles.csv") as csvfile:
            repo = VehiclesCsvRepository(csvfile)
            return route_handler_func(repo, *args, **kwargs)

    return wrapper
