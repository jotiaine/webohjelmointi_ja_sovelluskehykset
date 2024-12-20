from flask import jsonify, request
from werkzeug.exceptions import NotFound

import models


# Controller -> model -> tietokanta -> model -> controller -> view
def get_all_products():
    products = models.Product.get_all()
    return jsonify(models.Product.list_to_json(products))


def get_product_by_id(product_id):
    try:
        product = models.Product.get_by_id(product_id)
        return jsonify(product.to_json())
    except NotFound:
        return jsonify({"err": "product not found"}), 404
    except Exception as e:
        return jsonify({"err": str(e)}), 500


def create_product():
    try:
        data = request.get_json()
        new_product = models.Product(0, data["name"], data["description"])
        new_product.save()
        return jsonify(new_product.to_json())
    except Exception as e:
        return jsonify({"err": str(e)}), 500


def update_product_by_id(product_id):
    try:
        product = models.Product.get_by_id(product_id)
        data = request.get_json()
        product.name = data["name"]
        product.description = data["description"]
        product.save()
        return jsonify(product.to_json())
    except NotFound:
        return jsonify({"err": "product not found"}), 404


def delete_product_by_id(product_id):
    try:
        product = models.Product.get_by_id(product_id)
        product.delete()
        return jsonify(), 200
    except NotFound:
        return jsonify({"err": "product not found"}), 404
    except Exception as e:
        return jsonify({"err": str(e)}), 500
