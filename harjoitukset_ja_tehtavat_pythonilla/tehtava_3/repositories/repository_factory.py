import os

from .users_mysql_repository import UsersMysqlRepository
from .users_postgres_repository import UsersPostgresRepository
from .users_jsonplaceholder_repository import UsersJsonPlaceholderRepository

from .products_mysql_repository import ProductsMysqlRepository
from .products_postgres_repository import ProductsPostgresRepository


# Factory pattern, tehdään keskitetysti repoista instanssit
def users_repository_factory(con):
    if os.getenv("DB") == "mysql":
        return UsersMysqlRepository(con)
    elif os.getenv("DB") == "postgres":
        return UsersPostgresRepository(con)
    elif os.getenv("DB") == "json":
        return (
            UsersJsonPlaceholderRepository()
        )  # Tämä toimii samalla users ja productille
    else:
        return UsersMysqlRepository(con)


def products_repository_factory(con):
    if os.getenv("DB") == "mysql":
        return ProductsMysqlRepository(con)
    elif os.getenv("DB") == "postgres":
        return ProductsPostgresRepository(con)
    elif os.getenv("DB") == "json":
        return (
            UsersJsonPlaceholderRepository()
        )  # Tämä toimii samalla users ja productille
    else:
        return UsersMysqlRepository(con)


def vehicles_repository_factory():
    pass
