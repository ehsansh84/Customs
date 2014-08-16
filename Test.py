__author__ = 'ehsan'

# a = 10
# print a

# for i in range(10):
#     print i


# a = [1, 2, 3, 4, 5]
# # print a[0]
# for item in a:
#     print item

# from connections import *
#
# table = database.T
# table.update({'_id':''}, {
#             '_id': '',
#             'index': 111,
#             'name': 222
#         },
#             upsert=True, multi=False)

# from models.personnel import Personnel
# a = Personnel()
# a.name = 'ehsan'
# a.create()



# from controllers.violation import Violation as Controller
# print Controller.find()
# print Controller.find()
# from connections import db
from pymongo import MongoClient
client = MongoClient('192.1.8.14', 27017)
db = client.Customs
collection = db.violation
records = list(collection.find())
# records = collection.find().count()
print records
