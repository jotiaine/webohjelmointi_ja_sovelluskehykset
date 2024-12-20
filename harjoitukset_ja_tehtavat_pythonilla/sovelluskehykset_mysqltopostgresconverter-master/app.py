from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

import models

# muuta db_url-muuttuja vastaamaan oman postgres-serverisi ja tietokantasi tietoja

db_url = "postgresql+psycopg2://postgres:683652@localhost/sovelluskehykset_bad1"

engine = create_engine(db_url)

if not database_exists(db_url):
    create_database(db_url)

models.metadata.create_all(engine)
