import os
import mysql.connector
import psycopg2
import pymongo


def get_db_connection(route_handler):
    def wrapper(*args, **kwargs):
        if os.getenv("DB") == "mysql":
            con = mysql.connector.connect(
                user=os.getenv("DB_MYSQL_USER"),
                password=os.getenv("DB_MYSQL_PASSWORD"),
                database=os.getenv("DB_NAME"),
            )
        elif os.getenv("DB") == "postgres":
            con = psycopg2.connect(
                user=os.getenv("DB_POSTGRES_USER"),
                password=os.getenv("DB_POSTGRES_PASSWORD"),
                database=os.getenv("DB_NAME"),
            )
        elif os.getenv("DB") == "json":
            con = None
        elif os.getenv("DB") == "mongodb":
            host = os.getenv("DB_MONGO_HOST")
            port = os.getenv("DB_MONGO_PORT")
            con = pymongo.MongoClient(f"mongodb://{host}:{port}/")
        try:
            return route_handler(con, *args, **kwargs)
        finally:
            if con is not None:
                con.close()

    return wrapper
