#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'No Author'

from bson import ObjectId
import json
from global_defined import GlobalDefined
# from republishan2.tools.tools import Tools2


#noinspection PyBroadException
class Violation():
    __db = GlobalDefined.RepublishanDB
    __table_name = __db.Violation

    __record_count = 0
    __current_record = -1
    __dataset = None

    def __init__(self, s_date='', m_date='', fileNo='', kootaj='', cert_no='', s_date_1='', s_date_2='', policy_1=False, policy_2=False, policy_3=False, policy_4=False, policy_5=False, policy_6=False, policy_7=False, policy_8=False, ezharname=0, person_type=False, full_name='', card_no='', code_no='', company='', ez_full_name='', ez_owner='', ez_agent='', ez_card_no='', ez_code_no='', tr_full_name='', tr_code_no='', tr_reg_no='', tr_nationality='', tr_manager='', tr_type=False, item_name='', tariff_no='', paid=0, different=0, fine=0, diff_paid=0, vi_type_1=False, vi_type_2=False, vi_type_3=False, vi_type_4=False, vi_type_5=False, vi_type_6=False, vi_type_7=False, vi_type_other='', stated_tariff=0, stated_value=0, stated_weight=0, deducted_tariff=0, deducted_value=0, deducted_weight=0, law='', detector=0, detector_other='', results='', commitment=False, receip_no='', details='', m_rec_date='', s_rec_date='', locked=False):
        self.__id = ''
        self.s_date = s_date
        self.m_date = m_date
        self.fileNo = fileNo
        self.kootaj = kootaj
        self.cert_no = cert_no
        self.s_date_1 = s_date_1
        self.s_date_2 = s_date_2
        self.policy_1 = policy_1
        self.policy_2 = policy_2
        self.policy_3 = policy_3
        self.policy_4 = policy_4
        self.policy_5 = policy_5
        self.policy_6 = policy_6
        self.policy_7 = policy_7
        self.policy_8 = policy_8
        self.ezharname = ezharname
        self.person_type = person_type
        self.full_name = full_name
        self.card_no = card_no
        self.code_no = code_no
        self.company = company
        self.ez_full_name = ez_full_name
        self.ez_owner = ez_owner
        self.ez_agent = ez_agent
        self.ez_card_no = ez_card_no
        self.ez_code_no = ez_code_no
        self.tr_full_name = tr_full_name
        self.tr_code_no = tr_code_no
        self.tr_reg_no = tr_reg_no
        self.tr_nationality = tr_nationality
        self.tr_manager = tr_manager
        self.tr_type = tr_type
        self.item_name = item_name
        self.tariff_no = tariff_no
        self.paid = paid
        self.different = different
        self.fine = fine
        self.diff_paid = diff_paid
        self.vi_type_1 = vi_type_1
        self.vi_type_2 = vi_type_2
        self.vi_type_3 = vi_type_3
        self.vi_type_4 = vi_type_4
        self.vi_type_5 = vi_type_5
        self.vi_type_6 = vi_type_6
        self.vi_type_7 = vi_type_7
        self.vi_type_other = vi_type_other
        self.stated_tariff = stated_tariff
        self.stated_value = stated_value
        self.stated_weight = stated_weight
        self.deducted_tariff = deducted_tariff
        self.deducted_value = deducted_value
        self.deducted_weight = deducted_weight
        self.law = law
        self.detector = detector
        self.detector_other = detector_other
        self.results = results
        self.commitment = commitment
        self.receip_no = receip_no
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
            's_date': self.s_date,
            'm_date': self.m_date,
            'fileNo': self.fileNo,
            'kootaj': self.kootaj,
            'cert_no': self.cert_no,
            's_date_1': self.s_date_1,
            's_date_2': self.s_date_2,
            'policy_1': self.policy_1,
            'policy_2': self.policy_2,
            'policy_3': self.policy_3,
            'policy_4': self.policy_4,
            'policy_5': self.policy_5,
            'policy_6': self.policy_6,
            'policy_7': self.policy_7,
            'policy_8': self.policy_8,
            'ezharname': self.ezharname,
            'person_type': self.person_type,
            'full_name': self.full_name,
            'card_no': self.card_no,
            'code_no': self.code_no,
            'company': self.company,
            'ez_full_name': self.ez_full_name,
            'ez_owner': self.ez_owner,
            'ez_agent': self.ez_agent,
            'ez_card_no': self.ez_card_no,
            'ez_code_no': self.ez_code_no,
            'tr_full_name': self.tr_full_name,
            'tr_code_no': self.tr_code_no,
            'tr_reg_no': self.tr_reg_no,
            'tr_nationality': self.tr_nationality,
            'tr_manager': self.tr_manager,
            'tr_type': self.tr_type,
            'item_name': self.item_name,
            'tariff_no': self.tariff_no,
            'paid': self.paid,
            'different': self.different,
            'fine': self.fine,
            'diff_paid': self.diff_paid,
            'vi_type_1': self.vi_type_1,
            'vi_type_2': self.vi_type_2,
            'vi_type_3': self.vi_type_3,
            'vi_type_4': self.vi_type_4,
            'vi_type_5': self.vi_type_5,
            'vi_type_6': self.vi_type_6,
            'vi_type_7': self.vi_type_7,
            'vi_type_other': self.vi_type_other,
            'stated_tariff': self.stated_tariff,
            'stated_value': self.stated_value,
            'stated_weight': self.stated_weight,
            'deducted_tariff': self.deducted_tariff,
            'deducted_value': self.deducted_value,
            'deducted_weight': self.deducted_weight,
            'law': self.law,
            'detector': self.detector,
            'detector_other': self.detector_other,
            'results': self.results,
            'commitment': self.commitment,
            'receip_no': self.receip_no,
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
            self.s_date = entry['s_date']
            self.m_date = entry['m_date']
            self.fileNo = entry['fileNo']
            self.kootaj = entry['kootaj']
            self.cert_no = entry['cert_no']
            self.s_date_1 = entry['s_date_1']
            self.s_date_2 = entry['s_date_2']
            self.policy_1 = entry['policy_1']
            self.policy_2 = entry['policy_2']
            self.policy_3 = entry['policy_3']
            self.policy_4 = entry['policy_4']
            self.policy_5 = entry['policy_5']
            self.policy_6 = entry['policy_6']
            self.policy_7 = entry['policy_7']
            self.policy_8 = entry['policy_8']
            self.ezharname = entry['ezharname']
            self.person_type = entry['person_type']
            self.full_name = entry['full_name']
            self.card_no = entry['card_no']
            self.code_no = entry['code_no']
            self.company = entry['company']
            self.ez_full_name = entry['ez_full_name']
            self.ez_owner = entry['ez_owner']
            self.ez_agent = entry['ez_agent']
            self.ez_card_no = entry['ez_card_no']
            self.ez_code_no = entry['ez_code_no']
            self.tr_full_name = entry['tr_full_name']
            self.tr_code_no = entry['tr_code_no']
            self.tr_reg_no = entry['tr_reg_no']
            self.tr_nationality = entry['tr_nationality']
            self.tr_manager = entry['tr_manager']
            self.tr_type = entry['tr_type']
            self.item_name = entry['item_name']
            self.tariff_no = entry['tariff_no']
            self.paid = entry['paid']
            self.different = entry['different']
            self.fine = entry['fine']
            self.diff_paid = entry['diff_paid']
            self.vi_type_1 = entry['vi_type_1']
            self.vi_type_2 = entry['vi_type_2']
            self.vi_type_3 = entry['vi_type_3']
            self.vi_type_4 = entry['vi_type_4']
            self.vi_type_5 = entry['vi_type_5']
            self.vi_type_6 = entry['vi_type_6']
            self.vi_type_7 = entry['vi_type_7']
            self.vi_type_other = entry['vi_type_other']
            self.stated_tariff = entry['stated_tariff']
            self.stated_value = entry['stated_value']
            self.stated_weight = entry['stated_weight']
            self.deducted_tariff = entry['deducted_tariff']
            self.deducted_value = entry['deducted_value']
            self.deducted_weight = entry['deducted_weight']
            self.law = entry['law']
            self.detector = entry['detector']
            self.detector_other = entry['detector_other']
            self.results = entry['results']
            self.commitment = entry['commitment']
            self.receip_no = entry['receip_no']
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