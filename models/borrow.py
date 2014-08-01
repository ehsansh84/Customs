__author__ = 'ehsan'
from mongoengine import *
from connections import *
connect(database, host=mongo_host, port=mongo_port, username=mongo_username, password=mongo_password)


class Borrow(Document):
    personnel_id = IntField()
    file_id = IntField()
    date = DateTimeField()
    flow = ListField()
    returned = BooleanField()
    # returned = DictField()
