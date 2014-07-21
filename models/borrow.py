#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ehsan'

from bson import ObjectId
import json
from bson import json_util
from connections import database

#noinspection PyBroadException
class Borrow():
    __table_name = database.Borrow

    __record_count = 0
    __current_record = -1
    __dataset = None

    def __init__(self, personnel_id=0, file_id=0, date='', flow=[], returned=False):
        self.__id = ''
        self.personnel_id = personnel_id
        self.file_id = file_id
        self.date = date
        self.flow = flow
        self.returned = returned

    def __len__(self):
        return self.__record_count

    def __str__(self):
        return self.get_all_json()

    def __getitem__(self, item):
        if item > self.__record_count - 1 or item < -self.__record_count:
            raise Exception('item index out of range')
        if item < 0:
            item = item + self.__record_count
        return self.__get_json_record(self.__dataset[item])

    @property
    def eof(self):
        return self.__current_record == self.__record_count or self.__record_count <= 0

    @property
    def record_count(self):
        return self.__record_count

    def set_id(self, _id=''):
        if _id == '':
            self.__id = ObjectId()
        else:
            self.__id = ObjectId(_id)

    @property
    def get_id(self):
        #return self.__id
        return json.loads(json.dumps(self.__id, default=json_util.default))['$oid']
    def create(self):
        if self.__id == '':
            self.__id = ObjectId()
        result = self.__table_name.update({'_id': self.__id}, {
            '_id': self.__id,
            'personnel_id': self.personnel_id,
            'file_id': self.file_id,
            'date': self.date,
            'flow': self.flow,
            'returned': self.returned,

        },
            upsert=True, multi=False)
        return result['n'] > 0

    def remove(self):
        result = self.__table_name.remove({'_id': self.__id})
        return result['n'] > 0

    def find(self, _filter=None, page=-1, perpage=15, sort='_id', order=-1):
        _filter = {} if not _filter else _filter
        try:
            self.__init__()
            if page < 0:
                self.__dataset = self.__table_name.find(_filter).sort([(sort, order)])
            else:
                self.__dataset = self.__table_name.find(_filter).skip(page *
                                                                      perpage).limit(perpage).sort([(sort, order)])
            self.__record_count = self.__dataset.count(True)
            if self.__record_count > 0:
                return self.first()
        except:
            return False

    def load(self):
        try:
            self.__dataset = self.__table_name.find({'_id': self.__id})
            self.__record_count = self.__dataset.count()
            if self.__dataset.count() > 0:
                return self.first()
            return False
        except:
            return False

    def first(self):
        try:
            self.__current_record = 0
            return self.set_values()
        except:
            return False

    def next(self):
        try:
            if not self.eof:
                self.__current_record += 1
                return self.set_values()
            else:
                return False
        except:
            return False

    def previous(self):
        try:
            if self.__current_record > 0:
                self.__current_record -= 1
                return self.set_values()
            else:
                return False
        except:
            return False

    def last(self):
        try:
            self.__current_record = self.__record_count - 1
            return self.set_values()
        except:
            return False

    def set_values(self):
        try:
            entry = self.__dataset[self.__current_record]
            self.__id = entry['_id']
            self.personnel_id = entry['personnel_id']
            self.file_id = entry['file_id']
            self.date = entry['date']
            self.flow = entry['flow']
            self.returned = entry['returned']

            return True
        except:
            return False

    def get_json(self, _json=True):
        try:
            json_supported = {'Integer': 1, 'Float': 0.0, 'String': 's', 'Boolean': True, 'Array': []}
            dic = self.__dataset[self.__current_record]
            for item in dic.items():
                type_mach = [v for v in json_supported.values() if type(v) == type(item[1])]
                if len(type_mach) == 0:
                    try:
                        dic[item[0]] = str(item[1])
                    except:
                        dic[item[0]] = Tools2.encode(item[1])
            return json.dumps(dic, ensure_ascii=False) if _json else dic
        except:
            return json.dumps({}, ensure_ascii=False) if _json else {}

    @staticmethod
    def __get_json_record(record):
        try:
            json_supported = {'Integer': 1, 'Float': 0.0, 'String': 's', 'Boolean': True, 'Array': []}
            for item in record.items():
                type_mach = [v for v in json_supported.values() if type(v) == type(item[1])]
                if len(type_mach) == 0:
                    try:
                        record[item[0]] = str(item[1])
                    except:
                        record[item[0]] = Tools2.encode(item[1])
            return record
        except:
            return None

    def get_all_json(self, _json=True):
        try:
            temp = []
            for i in range(self.record_count):
                r = self.__get_json_record(self.__dataset[i])
                if r is not None:
                    temp.append(r)
            return json.dumps(temp, ensure_ascii=False) if _json else temp
        except:
            return json.dumps([], ensure_ascii=False) if _json else []