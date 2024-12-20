import os

from .users_mysql_repository import UsersMysqlRepository
from .users_postgres_repository import UsersPostgresRepository
from .users_jsonplaceholder_repository import UsersJsonPlaceholderRepository
from .users_mongodb_repository import UsersMongoDBRepository

from .products_mysql_repository import ProductsMysqlRepository
from .products_postgres_repository import ProductsPostgresRepository
from .products_mongodb_repository import ProductsMongoDBRepository

# Muistiinpanoja:
# Miksi factory patternia pitäisi käyttää, kun ilmankin pärjää?
# Kaikissa eri suunnittelumallien käyttöesimerkeissä on kyse pohjimmiltaan parista asiasta
# Separation of Concerns
# Koodin keskitetty hallinta
# nyt, kun UserRepositoryn instansseja ei luoda missä sattuu,
# vaan keskitetysti reposityro_factory:n avulla,
# muutokset UserRepositoryyn tarvitsee tehdä vain yhteen paikkaan
# myös silloin, jos pitää tehdä uusi repositorio uutta datalähdettä varten,
# lisäys tarvitsee tehdä vain yhteen paikkaan.
# Koodin testattavuus paranee sitä enemmän, mitä modulaarisemmin se on rakennettu
# yksikkötestejä ajettaessa repository voidaan helposti korvata stubilla / fakella.


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
    elif os.getenv("DB") == "mongodb":
        return UsersMongoDBRepository(con)
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
    elif os.getenv("DB") == "mongodb":
        return ProductsMongoDBRepository(con)
    else:
        return ProductsMysqlRepository(con)


def vehicles_repository_factory():
    pass
