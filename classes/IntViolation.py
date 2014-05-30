#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'No Author'

from bson import ObjectId
import json
from republishan2.global_defined import GlobalDefined
from republishan2.tools.tools import Tools2


#noinspection PyBroadException
class Intviolation():
    __db = GlobalDefined.RepublishanDB
    __table_name = __db.Intviolation

    __record_count = 0
    __current_record = -1
    __dataset = None

    def __init__(self, kootaj='', cert_no='', s_date='', m_date='', int_cert_no='', radif_marzi='', s_entry_date='', m_entry_date='', karne_tir_no='', ezhar_1=False, ezhar_2=False, ezhar_3=False, ezhar_4=False, person_type=False, full_name='', card_no='', code_no='', dest_address='', good_bame='', net_weight='', weight='', input_tariff='', good_count=0, price=0, truck_no='', driver_name='', chasis_no='', trailer_no='', tranian_truck=False, truck_address='', truck_type=0, vi_type_1=False, vi_type_2=False, vi_type_3=False, vi_type_4=False, vi_type_5=False, vi_type_6=False, vi_type_7=False, detector=0, detector_other='', fine_receipt_no='', fine_price=0, final_result=0, details='', m_rec_date='', s_rec_date='', locked=False):
        self.__id = ''
        self.kootaj = kootaj
        self.cert_no = cert_no
        self.s_date = s_date
        self.m_date = m_date
        self.int_cert_no = int_cert_no
        self.radif_marzi = radif_marzi
        self.s_entry_date = s_entry_date
        self.m_entry_date = m_entry_date
        self.karne_tir_no = karne_tir_no
        self.ezhar_1 = ezhar_1
        self.ezhar_2 = ezhar_2
        self.ezhar_3 = ezhar_3
        self.ezhar_4 = ezhar_4
        self.person_type = person_type
        self.full_name = full_name
        self.card_no = card_no
        self.code_no = code_no
        self.dest_address = dest_address
        self.good_bame = good_bame
        self.net_weight = net_weight
        self.weight = weight
        self.input_tariff = input_tariff
        self.good_count = good_count
        self.price = price
        self.truck_no = truck_no
        self.driver_name = driver_name
        self.chasis_no = chasis_no
        self.trailer_no = trailer_no
        self.tranian_truck = tranian_truck
        self.truck_address = truck_address
        self.truck_type = truck_type
        self.vi_type_1 = vi_type_1
        self.vi_type_2 = vi_type_2
        self.vi_type_3 = vi_type_3
        self.vi_type_4 = vi_type_4
        self.vi_type_5 = vi_type_5
        self.vi_type_6 = vi_type_6
        self.vi_type_7 = vi_type_7
        self.detector = detector
        self.detector_other = detector_other
        self.fine_receipt_no = fine_receipt_no
        self.fine_price = fine_price
        self.final_result = final_result
        self.details = details
        self.m_rec_date = m_rec_date
        self.s_rec_date = s_rec_date
        self.locked = locked

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
        return self.__id

    def create(self):
        if self.__id == '':
            self.__id = ObjectId()
        result = self.__table_name.update({'_id': self.__id}, {
            '_id': self.__id,
            'kootaj': self.kootaj,
            'cert_no': self.cert_no,
            's_date': self.s_date,
            'm_date': self.m_date,
            'int_cert_no': self.int_cert_no,
            'radif_marzi': self.radif_marzi,
            's_entry_date': self.s_entry_date,
            'm_entry_date': self.m_entry_date,
            'karne_tir_no': self.karne_tir_no,
            'ezhar_1': self.ezhar_1,
            'ezhar_2': self.ezhar_2,
            'ezhar_3': self.ezhar_3,
            'ezhar_4': self.ezhar_4,
            'person_type': self.person_type,
            'full_name': self.full_name,
            'card_no': self.card_no,
            'code_no': self.code_no,
            'dest_address': self.dest_address,
            'good_bame': self.good_bame,
            'net_weight': self.net_weight,
            'weight': self.weight,
            'input_tariff': self.input_tariff,
            'good_count': self.good_count,
            'price': self.price,
            'truck_no': self.truck_no,
            'driver_name': self.driver_name,
            'chasis_no': self.chasis_no,
            'trailer_no': self.trailer_no,
            'tranian_truck': self.tranian_truck,
            'truck_address': self.truck_address,
            'truck_type': self.truck_type,
            'vi_type_1': self.vi_type_1,
            'vi_type_2': self.vi_type_2,
            'vi_type_3': self.vi_type_3,
            'vi_type_4': self.vi_type_4,
            'vi_type_5': self.vi_type_5,
            'vi_type_6': self.vi_type_6,
            'vi_type_7': self.vi_type_7,
            'detector': self.detector,
            'detector_other': self.detector_other,
            'fine_receipt_no': self.fine_receipt_no,
            'fine_price': self.fine_price,
            'final_result': self.final_result,
            'details': self.details,
            'm_rec_date': self.m_rec_date,
            's_rec_date': self.s_rec_date,
            'locked': self.locked,

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
            self.kootaj = entry['kootaj']
            self.cert_no = entry['cert_no']
            self.s_date = entry['s_date']
            self.m_date = entry['m_date']
            self.int_cert_no = entry['int_cert_no']
            self.radif_marzi = entry['radif_marzi']
            self.s_entry_date = entry['s_entry_date']
            self.m_entry_date = entry['m_entry_date']
            self.karne_tir_no = entry['karne_tir_no']
            self.ezhar_1 = entry['ezhar_1']
            self.ezhar_2 = entry['ezhar_2']
            self.ezhar_3 = entry['ezhar_3']
            self.ezhar_4 = entry['ezhar_4']
            self.person_type = entry['person_type']
            self.full_name = entry['full_name']
            self.card_no = entry['card_no']
            self.code_no = entry['code_no']
            self.dest_address = entry['dest_address']
            self.good_bame = entry['good_bame']
            self.net_weight = entry['net_weight']
            self.weight = entry['weight']
            self.input_tariff = entry['input_tariff']
            self.good_count = entry['good_count']
            self.price = entry['price']
            self.truck_no = entry['truck_no']
            self.driver_name = entry['driver_name']
            self.chasis_no = entry['chasis_no']
            self.trailer_no = entry['trailer_no']
            self.tranian_truck = entry['tranian_truck']
            self.truck_address = entry['truck_address']
            self.truck_type = entry['truck_type']
            self.vi_type_1 = entry['vi_type_1']
            self.vi_type_2 = entry['vi_type_2']
            self.vi_type_3 = entry['vi_type_3']
            self.vi_type_4 = entry['vi_type_4']
            self.vi_type_5 = entry['vi_type_5']
            self.vi_type_6 = entry['vi_type_6']
            self.vi_type_7 = entry['vi_type_7']
            self.detector = entry['detector']
            self.detector_other = entry['detector_other']
            self.fine_receipt_no = entry['fine_receipt_no']
            self.fine_price = entry['fine_price']
            self.final_result = entry['final_result']
            self.details = entry['details']
            self.m_rec_date = entry['m_rec_date']
            self.s_rec_date = entry['s_rec_date']
            self.locked = entry['locked']

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
                        dic[item[0]] = Tools.encode(item[1])
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
                        record[item[0]] = Tools.encode(item[1])
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