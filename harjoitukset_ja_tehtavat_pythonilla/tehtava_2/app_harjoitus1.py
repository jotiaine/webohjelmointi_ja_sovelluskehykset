from flask import Flask
from dotenv import load_dotenv

from controllers.users_controller import (
    get_all_users,
    get_user_by_id,
    create_user,
    update_user_by_id,
    delete_user_by_id,
)
from controllers.products_controller import (
    get_all_products,
    get_product_by_id,
    create_product,
    update_product_by_id,
    delete_product_by_id,
)

from controllers.vehicles_controller import (
    get_all_vehicles_api,
    get_vehicle,
)

app = Flask(__name__)

# users
app.add_url_rule("/api/users", view_func=create_user, methods=["POST"])
app.add_url_rule("/api/users", view_func=get_all_users, methods=["GET"])
app.add_url_rule("/api/users/<user_id>", view_func=get_user_by_id, methods=["GET"])
app.add_url_rule("/api/users/<user_id>", view_func=update_user_by_id, methods=["PUT"])
app.add_url_rule(
    "/api/users/<user_id>", view_func=delete_user_by_id, methods=["DELETE"]
)

# products
app.add_url_rule("/api/products", view_func=create_product, methods=["POST"])
app.add_url_rule("/api/products", view_func=get_all_products, methods=["GET"])
app.add_url_rule(
    "/api/products/<product_id>", view_func=get_product_by_id, methods=["GET"]
)
app.add_url_rule(
    "/api/products/<product_id>", view_func=update_product_by_id, methods=["PUT"]
)
app.add_url_rule(
    "/api/products/<product_id>", view_func=delete_product_by_id, methods=["DELETE"]
)


# vehicles
app.add_url_rule("/api/vehicles", view_func=get_all_vehicles_api)
app.add_url_rule("/api/vehicles/1", view_func=get_vehicle)


if __name__ == "__main__":
    load_dotenv()
    app.run()
