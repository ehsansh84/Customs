__author__ = 'ehsan'
from mongoengine import *
from connections import *
connect(database, host=mongo_host, port=mongo_port, username=mongo_username, password=mongo_password)


class Editrequest(Document):
    user_id = StringField()
    s_date = StringField()
    m_date = DateTimeField()
    violation_id = StringField()
    reason = StringField()
