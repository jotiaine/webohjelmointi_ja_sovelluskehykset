import os
import mysql.connector
import psycopg2


def get_db_connection(route_handler):
    def wrapper(*args, **kwargs):
        if os.getenv("DB") == "mysql":
            db_connector = mysql.connector
        else:
            db_connector = psycopg2
        with db_connector.connect(user="root", database="sovelluskehykset_bad1") as con:
            return route_handler(con, *args, **kwargs)

    return wrapper
