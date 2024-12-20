from flask import Flask
from controllers.vehicles_controller import get_all_vehicles

app = Flask(__name__)

app.add_url_rule("/api/vehicles", endpoint="vehicles_index", view_func=get_all_vehicles)

if __name__ == "__main__":
    app.run(debug=False)
