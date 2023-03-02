from peewee import *
from os import path
from peewee import Model

connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "Sean.db"))


class People(Model):
    name = CharField()
    phone_number = CharField()
    email = CharField()
    county = CharField()
    gender = CharField()
    religion = CharField()
    password = CharField()

    class Meta:
        database = db


People.create_table(fail_silently=True)
