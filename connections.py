__author__ = 'ehsan'
# from pymongo import MongoClient
import redis
from tools.debug import Debug
from pymongo import MongoClient
# host = '127.0.0.1'
# mongo_connection = MongoClient('mongodb://username:password@' + host + ':27017/republishan2')
# mongo_connection = MongoClient('mongodb://' + host + ':27017/tempdb')
# database = mongo_connection.Customs

mongo_host = mongo_port = database = mongo_username = mongo_password = ''
redis_host = redis_port = redis_username = redis_password = ''

mongo_server = 'local'
# mongo_server = 'customs_local'
# mongo_server = 'customs_remote'
# mongo_server = 'customs_remote_lan'

# redis_server = 'local'
# redis_server = 'customs_local'
redis_server = 'local'

database = 'Customs'


if mongo_server == 'local':
    mongo_host = '192.1.8.14'
    # mongo_host = '127.0.0.1'
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
    redis_password = '1234qwer'
elif redis_server == 'office':
    redis_host = '192.168.1.173'
    redis_port = 6379
    redis_password = '1234qwer'
# elif redis_server == 'customs_remote_lan':
#     redis_host = '192.1.8.13'
#     redis_port = 6379
#     redis_username = ''
#     redis_password = ''

# Debug.dprint(text='Redis port')
# Debug.dprint(text=redis_port, type='data')
Debug.dprint(text='Mongo host')
Debug.dprint(text=mongo_host, type='data')
Debug.dprint(text='Redis host')
Debug.dprint(text=redis_host, type='data')
redis_instance = redis.StrictRedis(host=redis_host, port=redis_port, db=0)
# redis_instance = redis.StrictRedis(host=redis_host, port=redis_port, db=0, password=redis_password)
# redisInstance = redis.StrictRedis(host=redis_host, port=redis_port, db=0, password=redis_password)
# client = MongoClient('127.0.0.1', 27017)
client = MongoClient('192.1.8.14', 27017)
db = client.Customs
