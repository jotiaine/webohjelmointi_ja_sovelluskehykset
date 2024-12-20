from flask import Flask, jsonify, request

from controllers.users_controller import (
    get_all_users,
    get_user,
    create_users,
    update_users,
    delete_users,
)
from controllers.products_controller import (
    get_all_products,
    get_product,
    create_products,
    update_products,
    delete_products,
)

from controllers.vehicles_controller import (
    get_all_vehicles_api,
    get_vehicle,
)

app = Flask(__name__)

# users
app.add_url_rule("/api/create_users", view_func=create_users)
app.add_url_rule("/api/users", view_func=get_all_users)
app.add_url_rule("/api/users/1", view_func=get_user)
app.add_url_rule("/api/update_users", view_func=update_users)
app.add_url_rule("/api/delete_users", view_func=delete_users)

# products
app.add_url_rule("/api/create_products", view_func=create_products)
app.add_url_rule("/api/products", view_func=get_all_products)
app.add_url_rule("/api/products/1", view_func=get_product)
app.add_url_rule("/api/update_products", view_func=update_products)
app.add_url_rule("/api/delete_products", view_func=delete_products)

# vehicles
app.add_url_rule("/api/vehicles", view_func=get_all_vehicles_api)
app.add_url_rule("/api/vehicles/1", view_func=get_vehicle)


if __name__ == "__main__":
    app.run()
