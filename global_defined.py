__author__ = 'Hassan'

#from elasticsearch import Elasticsearch
#from cqlengine import connection
#import pysolr
import redis
from pymongo import MongoClient


class GlobalDefined():
    def __init__(self):
        pass

    # redisInstance = redis.StrictRedis(host='127.0.0.1')
    # redisInstance = redis.StrictRedis(host='127.0.0.1', port=6379, db=0, password='1234qwer')
    MongoConnection = MongoClient()
    # MongoConnection = MongoClient('mongodb://republishan2:27debc6ae243377d65e7@127.0.0.1:27017/republishan2')
    # MongoConnection = MongoClient('mongodb://republishan2:27debc6ae243377d65e7@192.168.1.173:27017/republishan2')
    # MongoConnection=MongoClient('mongodb://repubads:cTj6JW7p@192.168.156.11:27017/repubmon')
    #MongoConnectionForAdvertise=MongoClient('mongodb://republishan:29f8g34@192.168.156.11:27017/republishan')
    # ------------------- Internal Connection--------------------
    RepublishanDB = MongoConnection.republishan2
    #AdvertiseDB=MongoConnectionForAdvertise.republishan
    # ------------------ Mongo Connection -------------------------

    # ----------------- Cassandra Connection ---------------------
    #connection.setup(['127.0.0.1:9160'])
    #connection.setup(['192.168.136.89:9160'])
    # ----------------- Cassandra Connection ---------------------

    # -----------------  Solr Connection --------------------
    #solr = pysolr.Solr('http://127.0.0.1:8983/solr/entry', timeout=10)
    #solr = pysolr.Solr('http://192.168.139.247:8983/solr/entry', timeout=10)
    # -----------------  Solr Connection --------------------

    # -----------------  Solr Connection --------------------
    #kafka = KafkaClient("localhost", 9092, pool_size=20, auto_connect=True)
    # -----------------  Solr Connection --------------------
    # -----------------  Sitename --------------------
    #SiteName = "real24"
    # -----------------  Sitename --------------------

    #ElasticsearchConnection = Elasticsearch(host='173.255.234.246', port=9200)

#    -------------- connection query solr -------------------
#   solr_connection_query="http://solr.360republish.com/solr/entry/"

#    -------------- connection query solr -------------------

#     Main Server
#    MainServerStatServiceUrl = 'http://192.168.189.154:2323/republishan/'
#    MainServerStatServiceUrlFormonitoring = 'http://192.168.189.154:2323/republishan/statInfo'
#    MainServerRedis=redis.StrictRedis(host='192.168.139.199', port=6379, db=0,password='1234qwer')
#
#    # Test Server Local IP
#    TestServerStatServiceUrl = 'http://192.168.136.89:2323/republishan/'
#    TestServerStatServiceUrlFormonitoring = 'http://192.168.136.89:2323/republishan/statInfo'

#redis-cli -h 192.168.139.247 -a 1234qwer -p 6379

#MainServer1=23.239.8.188 Grabber Server


# redis-cli -h 192.168.139.199 -a 1234qwer -p 6379


# MongoConnection = MongoClient('mongodb://republishan2:27debc6ae243377d65e7@127.0.0.1:27017/republishan2')
# redisInstance = redis.StrictRedis(host='127.0.0.1', port=6379, db=0, password='1234qwer')