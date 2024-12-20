import os
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
    get_all_vehicles_html_page,
)

app = Flask(__name__)

# users
app.add_url_rule(
    "/api/users", view_func=create_user, methods=["POST"], endpoint="create_user"
)
app.add_url_rule(
    "/api/users", view_func=get_all_users, methods=["GET"], endpoint="get_all_users"
)
app.add_url_rule(
    "/api/users/<user_id>",
    view_func=get_user_by_id,
    methods=["GET"],
    endpoint="get_user_by_id",
)
app.add_url_rule(
    "/api/users/<user_id>",
    view_func=update_user_by_id,
    methods=["PUT"],
    endpoint="update_user_by_id",
)
app.add_url_rule(
    "/api/users/<user_id>",
    view_func=delete_user_by_id,
    methods=["DELETE"],
    endpoint="delete_user_by_id",
)

# products
app.add_url_rule(
    "/api/products",
    view_func=create_product,
    methods=["POST"],
    endpoint="create_product",
)
app.add_url_rule(
    "/api/products",
    view_func=get_all_products,
    methods=["GET"],
    endpoint="get_all_products",
)
app.add_url_rule(
    "/api/products/<product_id>",
    view_func=get_product_by_id,
    methods=["GET"],
    endpoint="get_product_by_id",
)
app.add_url_rule(
    "/api/products/<product_id>",
    view_func=update_product_by_id,
    methods=["PUT"],
    endpoint="update_product_by_id",
)
app.add_url_rule(
    "/api/products/<product_id>",
    view_func=delete_product_by_id,
    methods=["DELETE"],
    endpoint="delete_product_by_id",
)


# vehicles
app.add_url_rule("/api/vehicles", view_func=get_all_vehicles_api, methods=["GET"])
app.add_url_rule("/vehicles", view_func=get_all_vehicles_html_page, methods=["GET"])


if __name__ == "__main__":
    load_dotenv(
        override=True
    )  # load_dotenv() ei ladannut .env, joten override=True vaadittiin, tämän selvitin chatGPT:ltä kun db ei vaihtunut, vaikka vaihdoin .envissä.
    app.run()
