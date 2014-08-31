__author__ = 'ehsan'
from mongoengine import *
from connections import *
# connect(database, host=mongo_host, port=mongo_port, username=mongo_username, password=mongo_password)
connect(database, host='127.0.0.1', port=mongo_port, username=mongo_username, password=mongo_password)


class User(Document):
    username = StringField()
    password = StringField()
    type = StringField()
    name = StringField()
    family = StringField()