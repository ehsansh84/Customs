__author__ = 'ehsan'
from connections import redis_instance
import json
from debug import Debug
"""
Using this class:
    assure that you have no unwanted redis variable left in memory
    let you store and retrieve lists and dictionaries
"""


class Redis:
    # r = connections.redis_instance

    def __init__(self):
        pass

    @classmethod
    def get(cls, key, type='string'):
        result = redis_instance.get(key)
        if type == 'string':
            return result
        elif type == 'list' or type == 'dic':
            return json.loads(result)


    @classmethod
    def set(cls, key, value, expire=1000, type='string'):
        Debug.dprint(text=key)
        Debug.dprint(text=value)
        if type == 'string':
            redis_instance.set(key, value, expire)
        elif type == 'list' or type == 'dic':
            redis_instance.set(key, json.dumps(value), expire)



    @classmethod
    def search(cls, key, field='', value=''):
        lst = json.loads(redis_instance.get(key))
        for item in lst:
            if item[field] == value:
                return item
        return 'not found'