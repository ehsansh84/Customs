__author__ = 'ehsan'
# from pymongo import MongoClient
import redis

# host = '127.0.0.1'
# mongo_connection = MongoClient('mongodb://username:password@' + host + ':27017/republishan2')
# mongo_connection = MongoClient('mongodb://' + host + ':27017/tempdb')
# database = mongo_connection.Customs

mongo_host = mongo_port = database = mongo_username = mongo_password = ''
redis_host = redis_port = redis_username = redis_password = ''

# mongo_server = 'my_local'
# mongo_server = 'customs_local'
# mongo_server = 'customs_remote'
mongo_server = 'customs_remote_lan'
redis_server = 'customs_remote_lan'

database = 'Customs'

if mongo_server == 'local':
    mongo_host = '127.0.0.1'
    mongo_port = 27017
    mongo_username = ''
    mongo_password = ''
elif mongo_server == 'customs_local':
    mongo_host = '127.0.0.1'
    mongo_port = 27017
    mongo_username = ''
    mongo_password = ''
elif mongo_server == 'customs_remote':
    mongo_host = '82.115.26.202'
    mongo_port = 27017
    mongo_username = ''
    mongo_password = ''
elif mongo_server == 'customs_remote_lan':
    mongo_host = '192.1.8.13'
    mongo_port = 27017
    mongo_username = ''
    mongo_password = ''

if redis_server == 'local':
    #TODO: not set
    redis_host = '127.0.0.1'
    redis_port = 6379
    redis_username = ''
    redis_password = ''
elif redis_server == 'customs_local':
    redis_host = '127.0.0.1'
    redis_port = 6379
    redis_username = ''
    redis_password = ''
elif redis_server == 'customs_remote':
    #TODO: not set
    redis_host = '82.115.26.202'
    redis_port = 6379
    redis_username = ''
    redis_password = ''
# elif redis_server == 'customs_remote_lan':
#     redis_host = '192.1.8.13'
#     redis_port = 6379
#     redis_username = ''
#     redis_password = ''


redis_instance = redis.StrictRedis(host=redis_host, port=redis_port, db=0, password=redis_password)
