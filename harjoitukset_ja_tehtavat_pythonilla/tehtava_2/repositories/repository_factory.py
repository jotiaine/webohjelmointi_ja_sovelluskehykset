import os

from .users_mysql_repository import UsersMysqlRepository
from .users_postgres_repository import UsersPostgresRepository
from .products_mysql_repository import ProductsMysqlRepository
from .products_postgres_repository import ProductsPostgresRepository


# Factory pattern, tehdään keskitetysti repoista instanssit
def users_repository_factory(con):
    if os.getenv("DB") == "mysql":
        return UsersMysqlRepository(con)
    else:
        return UsersPostgresRepository(con)


def products_repository_factory(con):
    if os.getenv("DB") == "mysql":
        return ProductsMysqlRepository(con)
    else:
        return ProductsPostgresRepository(con)


def vehicles_repository_factory():
    pass
