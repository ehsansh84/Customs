__author__ = 'ehsan'
from mongoengine import *
from connections import *
connect(database, host=mongo_host, port=mongo_port, username=mongo_username, password=mongo_password)


class File(Document):
    kootaj = StringField()
    desc = StringField()
