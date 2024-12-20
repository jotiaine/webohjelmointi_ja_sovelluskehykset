import mysql.connector


def get_db_conn(route_handler_func):
    def wrapper(*args, **kwargs):
        with mysql.connector.connect(
            user="root", password="", host="localhost", database="sovelluskehykset_bad1"
        ) as con:
            return route_handler_func(con, *args, **kwargs)

    return wrapper
