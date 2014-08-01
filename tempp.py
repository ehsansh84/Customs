# from tools.redis import Redis
# from connections import redis_instance
# Redis.set('name', value='ehsan')
# print(Redis.get('name'))

# r = redis_instance
# r.set('name', 'ehsan', 1000)

# from models.detect import Detect as D

# D.Kootaj = '123'
# D.

from models.file import File as Model
from bson import ObjectId


# shit = Model()
# shit.desc = 'This is the desc 3'
# shit.kootaj = '3'
# shit.save()

# shit = Model.objects(__raw__={})
# for item in shit:
#     print(item.kootaj)
#     print(item.id)
#
#
# ###################### #GET an item by ID
# shit = Model.objects.get(id=ObjectId('53d7a8659fc56b5adcf67483'))
# print shit.id
# print shit.kootaj
# print shit.desc

# a = Model.objects(id='53d016ac9fc56b1dccd0dea7')
# print a


# shit = Model.objects.get(id=ObjectId('53d7a8659fc56b5adcf67483'))
# Model.delete({})
# Model.objects(kootaj='1').delete()
# Model.delete()
# print shit.
# print shit.kootaj
# print shit.desc

# from connections import *
# print 'redis'
# redisInstance.set('name', 'ehsan', ex=1000)
# print redisInstance.get('name')
