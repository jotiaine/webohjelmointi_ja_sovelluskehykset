import models
from werkzeug.exceptions import NotFound
from bson.objectid import ObjectId


class ProductsMongoDBRepository:
    def __init__(self, con):
        self.con = con
        self.mydb = con["sovelluskehykset_bad1"]
        self.mycol = self.mydb["products"]

    def __del__(self):
        if self.con is not None:
            self.con.close()

    def get_all(self):
        products = []
        for product in self.mycol.find():
            products.append(
                models.Product(
                    str(product["_id"]), product["name"], product["description"]
                )
            )
        return products

    def get_by_id(self, _id):
        myquery = {"_id": ObjectId(_id)}
        product = self.mycol.find_one(myquery)
        if product is None:
            raise NotFound("product not found")
        return models.Product(
            str(product["_id"]),
            product["name"],
            product["description"],
        )

    def _create(self, product):
        try:
            mydict = {
                "name": product.name,
                "description": product.description,
            }
            x = self.mycol.insert_one(mydict)
            product.id = str(x.inserted_id)
        except Exception as e:
            raise e

    def _update(self, product):
        try:
            myquery = {"_id": ObjectId(product.id)}
            newvalues = {
                "$set": {
                    "name": product.name,
                    "description": product.description,
                }
            }
            self.mycol.update_one(myquery, newvalues)
        except Exception as e:
            raise e

    def delete(self, product):
        try:
            myquery = {"_id": ObjectId(product.id)}
            self.mycol.delete_one(myquery)
        except Exception as e:
            raise e

    def save(self, product):
        if product.id == 0:
            self._create(product)
        else:
            self._update(product)

    def to_json(self, product):
        return {
            "id": product.id,
            "name": product.name,
            "description": product.description,
        }

    def list_to_json(self, products_list):
        products_json_list = []
        for u in products_list:
            products_json_list.append(self.to_json(u))
        return products_json_list
