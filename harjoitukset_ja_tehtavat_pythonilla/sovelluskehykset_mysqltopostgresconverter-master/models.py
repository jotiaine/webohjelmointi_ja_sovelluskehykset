from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import Mapped, declarative_base, mapped_column
from sqlalchemy.orm.base import Mapped

Base = declarative_base()
metadata = Base.metadata


class Products(Base):
    __tablename__ = 'products'

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(255), nullable=False)
    description = mapped_column(Text)


class Users(Base):
    __tablename__ = 'users'

    id = mapped_column(Integer, primary_key=True)
    username = mapped_column(String(255), nullable=False)
    firstname = mapped_column(String(255), nullable=False)
    lastname = mapped_column(String(255), nullable=False)


class Vehicles(Base):
    __tablename__ = 'vehicles'

    id = mapped_column(Integer, primary_key=True)
    make = mapped_column(String(255), nullable=False)
    model = mapped_column(String(255), nullable=False)
