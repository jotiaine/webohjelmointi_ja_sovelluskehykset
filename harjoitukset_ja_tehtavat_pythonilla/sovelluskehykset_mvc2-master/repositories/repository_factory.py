import os
from .users_mysql_repository import UsersMysqlRepository
from .users_postgres_repository import UsersPostgresRepository


# Factory pattern, tehdään keskitetysti repoista instanssit
def users_repository_factory(con):

    return UsersMysqlRepository(con)


def vehicles_repository_factory():
    pass
