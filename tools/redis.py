__author__ = 'ehsan'
from shared_connections import *
import json
from debug import Debug
"""
Using this class:
    assure that you have no unwanted redis variable left in memory
    let you store and retrieve lists and dictionaries
"""


class Redis:
    r = SharedConnections.redisInstance

    def __init__(self):
        pass

    @classmethod
    def get(cls, key, type='string'):
        result = cls.r.get(key)
        if type == 'string':
            return result
        elif type == 'list' or type == 'dic':
            return json.loads(result)


    @classmethod
    def set(cls, key, value, expire=1000, type='string'):
        if type == 'string':
            cls.r.set(key, value, expire)
        elif type == 'list' or type == 'dic':
            cls.r.set(key, json.dumps(value), expire)


    @classmethod
    def search(cls, key, field='', value=''):
        lst = json.loads(cls.r.get(key))
        for item in lst:
            if item[field] == value:
                return item
        return 'not found'