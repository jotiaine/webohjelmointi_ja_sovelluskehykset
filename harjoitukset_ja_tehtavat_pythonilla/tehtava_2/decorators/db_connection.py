import os
import mysql.connector
import psycopg2


def get_db_connection(route_handler):
    def wrapper(*args, **kwargs):
        if os.getenv("DB") == "mysql":
            con = mysql.connector.connect(
                user=os.getenv("DB_MYSQL_USER"),
                password=os.getenv("DB_MYSQL_PASSWORD"),
                database=os.getenv("DB_NAME"),
            )
        else:
            con = psycopg2.connect(
                user=os.getenv("DB_POSTGRES_USER"),
                password=os.getenv("DB_POSTGRES_PASSWORD"),
                database=os.getenv("DB_NAME"),
            )
        try:
            return route_handler(con, *args, **kwargs)
        finally:
            con.close()

    return wrapper
