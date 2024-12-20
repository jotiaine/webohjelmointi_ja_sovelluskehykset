import os
import psycopg2
import models
from psycopg2.extras import RealDictCursor
from werkzeug.exceptions import NotFound


class ProductsPostgresRepository:
    def __init__(self, con):
        self.con = con

    def __del__(self):
        if self.con is not None and self.con.closed == 0:
            self.con.close()

    def get_all(self):
        with self.con.cursor() as cur:
            cur.execute("SELECT * FROM products")
            result = cur.fetchall()
            products = []
            for product in result:
                products.append(models.Product(product[0], product[1], product[2]))

            return products

    def get_by_id(self, _id):
        with self.con.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM products WHERE id=%s", (_id,))
            product = cur.fetchone()
            if product is None:
                raise NotFound("product not found")
            return models.Product(
                product["id"],
                product["name"],
                product["description"],
            )

    def _create(self, product):
        try:
            with self.con.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    "INSERT INTO products (name, description) VALUES (%s, %s) RETURNING id",
                    (product.name, product.description),
                )
                product.id = cur.fetchone()["id"]
                self.con.commit()
        except Exception as e:
            self.con.rollback()
            raise e

    def _update(self, product):
        try:
            with self.con.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    "UPDATE products SET name = %s, description = %s WHERE id = %s",
                    (product.name, product.description, product.id),
                )
                self.con.commit()
        except Exception as e:
            self.con.rollback()
            raise e

    def delete(self, product):
        try:
            with self.con.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("DELETE FROM products WHERE id = %s", (product.id,))
                self.con.commit()
        except Exception as e:
            self.con.rollback()
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
