from flask import jsonify

import models


def get_all_products():
    products = models.Product.get_all()
    return jsonify(models.Product.list_to_json(products))


def get_product():
    product = models.Product.get_product()
    return jsonify(product)


def create_products():
    models.Product.create()
    products = models.Product.get_all()
    return jsonify(models.Product.list_to_json(products))


def update_products():
    models.Product.update_products()
    products = models.Product.get_all()
    return jsonify(models.Product.list_to_json(products))


def delete_products():
    models.Product.delete_products()
    products = models.Product.get_all()
    return jsonify(models.Product.list_to_json(products))
