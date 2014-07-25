__author__ = 'ehsan'
from pymongo import MongoClient

host = '127.0.0.1'
# mongo_connection = MongoClient('mongodb://username:password@' + host + ':27017/republishan2')
mongo_connection = MongoClient('mongodb://' + host + ':27017/tempdb')
database = mongo_connection.Customs

mongo_host = mongo_port = database = mongo_username = mongo_password = ''

mongo_server = 'my_local'
# mongo_server = 'customs_local'
# mongo_server = 'customs_remote'

database = 'Customs'

if mongo_server == 'local':
    mongo_host = '127.0.0.1'
    mongo_port = '27017'
    mongo_username = ''
    mongo_password = ''
elif mongo_server == 'customs_local':
    mongo_host = '127.0.0.1'
    mongo_port = '27017'
    mongo_username = ''
    mongo_password = ''
elif mongo_server == 'customs_remote':
    mongo_host = '-'
    mongo_port = '27017'
    mongo_username = ''
    mongo_password = ''