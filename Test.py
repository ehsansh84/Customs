__author__ = 'ehsan'
from tools.debug import Debug
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
import json
from pymongo import MongoClient
from tools.debug import Debug
client = MongoClient('192.1.8.14', 27017)
db = client.Customs
collection = db.violation
records = list(collection.find())
# records =  list(collection.find())
# records =  json.dumps(list(collection.find()))
# records = collection.find().count()
# for item in records:
#     Debug.dprint(item['full_name'])

# from controllers.violation import Violation as Controller
from models.violation import Violation as Model
Debug.dprint(text=list(Model.objects()), type='custom')
# Debug.dprint(text=list(Model.objects(__raw__={'file_no': '123456'})), type='custom')
# Debug.dprint(text=str(Controller.find(_filter=filter)), type='custom')
# f = {'file_no': '123456'}
# Debug.dprint(text=str(f), type='error')
# Debug.dprint(text=str(Controller.find(_filter=f)), type='msg')