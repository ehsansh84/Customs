__author__ = 'ehsan'
from pymongo import MongoClient

host = '127.0.0.1'
# mongo_connection = MongoClient('mongodb://username:password@' + host + ':27017/republishan2')
mongo_connection = MongoClient('mongodb://' + host + ':27017/tempdb')
database = mongo_connection.Customs
