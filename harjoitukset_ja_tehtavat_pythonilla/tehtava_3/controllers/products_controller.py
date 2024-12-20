from flask import jsonify, request
from werkzeug.exceptions import NotFound

from decorators.db_connection import get_db_connection
import models
from repositories.repository_factory import products_repository_factory


# Controller -> repository -> model -> tietokanta -> model -> controller -> view
@get_db_connection
def get_all_products(con):
    try:
        repo = products_repository_factory(con)
        products = repo.get_all()
        return jsonify(repo.list_to_json(products))
    except Exception as e:
        return jsonify({"err": str(e)}), 500


@get_db_connection
def get_product_by_id(con, product_id):
    try:
        repo = products_repository_factory(con)
        product = repo.get_by_id(product_id)
        return jsonify(repo.to_json(product))
    except NotFound:
        return jsonify({"err": "product not found"}), 404
    except Exception as e:
        return jsonify({"err": str(e)}), 500


@get_db_connection
def create_product(con):
    try:
        data = request.get_json()
        new_product = models.Product(0, data["name"], data["description"])
        repo = products_repository_factory(con)
        repo.save(new_product)
        return jsonify(repo.to_json(new_product))
    except Exception as e:
        return jsonify({"err": str(e)}), 500


@get_db_connection
def update_product_by_id(con, product_id):
    try:
        repo = products_repository_factory(con)
        product = repo.get_by_id(product_id)
        data = request.get_json()
        product.name = data["name"]
        product.description = data["description"]
        repo.save(product)
        return jsonify(repo.to_json(product))
    except NotFound:
        return jsonify({"err": "product not found"}), 404


@get_db_connection
def delete_product_by_id(con, product_id):
    try:
        repo = products_repository_factory(con)
        product = repo.get_by_id(product_id)
        repo.delete(product)
        return jsonify(), 200
    except NotFound:
        return jsonify({"err": "product not found"}), 404
    except Exception as e:
        return jsonify({"err": str(e)}), 500
