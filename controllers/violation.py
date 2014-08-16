__author__ = 'ehsan'
from models.violation import Violation as Model
from datetime import datetime
from tools.debug import Debug
from connections import db

class Violation():
    def __init__(self):
        pass

    @classmethod
    def add(cls, id='', s_date='', m_date='', file_no='', kootaj='', cert_no='', s_date_1='', s_date_2='',
            policy_1=False, policy_2=False, policy_3=False, policy_4=False, policy_5=False, policy_6=False,
            policy_7=False, ezharname=0, person_type=False, full_name='', card_no='', code_no='', company='',
            ez_full_name='', ez_owner='', ez_agent='', ez_card_no='', ez_code_no='', tr_full_name='', tr_code_no='',
            tr_reg_no='', tr_nationality='', tr_manager='', tr_type=False, item_name='', tariff_no='', paid=0,
            different=0, fine=0, diff_paid=0, vi_type_1=False, vi_type_2=False, vi_type_3=False, vi_type_4=False,
            vi_type_5=False, vi_type_6=False, vi_type_7=False, vi_type_other='', stated_tariff=0, stated_value=0,
            stated_weight=0, deducted_tariff=0, deducted_value=0, deducted_weight=0, law='', detector=0,
            detector_other='', results='', commitment=False, receip_no='', details='', locked=False):


        #TODO Something for this
        vi_type_1 = True if vi_type_1 == 'on' else False
        vi_type_2 = True if vi_type_2 == 'on' else False
        vi_type_3 = True if vi_type_3 == 'on' else False
        vi_type_4 = True if vi_type_4 == 'on' else False
        vi_type_5 = True if vi_type_5 == 'on' else False
        vi_type_6 = True if vi_type_6 == 'on' else False
        vi_type_7 = True if vi_type_7 == 'on' else False

        policy_1 = True if policy_1 == 'on' else False
        policy_2 = True if policy_2 == 'on' else False
        policy_3 = True if policy_3 == 'on' else False
        policy_4 = True if policy_4 == 'on' else False
        policy_5 = True if policy_5 == 'on' else False
        policy_6 = True if policy_6 == 'on' else False
        policy_7 = True if policy_7 == 'on' else False

        print('stated_weight: ' + str(stated_weight))
        print('deducted_weight: ' + str(deducted_weight))
        if id != '':
            obj = Model.objects(Kootaj=id).first()

        else:
            obj = Model()

        if obj != None:
            vi_type_1 = True
            obj.s_date = s_date
            #TODO it should use s_date
            obj.m_date = datetime.now()
            obj.file_no = file_no
            obj.kootaj = kootaj
            obj.cert_no = cert_no
            obj.s_date_1 = s_date_1
            obj.s_date_2 = s_date_2
            obj.policy_1 = policy_1
            obj.policy_2 = policy_2
            obj.policy_3 = policy_3
            obj.policy_4 = policy_4
            obj.policy_5 = policy_5
            obj.policy_6 = policy_6
            obj.policy_7 = policy_7
            obj.ezharname = ezharname
            obj.person_type = person_type
            obj.full_name = full_name
            obj.card_no = card_no
            obj.code_no = code_no
            obj.company = company
            obj.ez_full_name = ez_full_name
            obj.ez_owner = ez_owner
            obj.ez_agent = ez_agent
            obj.ez_card_no = ez_card_no
            obj.ez_code_no = ez_code_no
            obj.tr_full_name = tr_full_name
            obj.tr_code_no = tr_code_no
            obj.tr_reg_no = tr_reg_no
            obj.tr_nationality = tr_nationality
            obj.tr_manager = tr_manager
            obj.tr_type = tr_type
            obj.item_name = item_name
            obj.tariff_no = tariff_no
            obj.paid = paid
            obj.different = different
            obj.fine = fine
            obj.diff_paid = diff_paid
            obj.vi_type_1 = vi_type_1
            obj.vi_type_2 = vi_type_2
            obj.vi_type_3 = vi_type_3
            obj.vi_type_4 = vi_type_4
            obj.vi_type_5 = vi_type_5
            obj.vi_type_6 = vi_type_6
            obj.vi_type_7 = vi_type_7
            obj.vi_type_other = vi_type_other
            obj.stated_tariff = stated_tariff
            obj.stated_value = stated_value
            obj.stated_weight = stated_weight
            obj.deducted_tariff = deducted_tariff
            obj.deducted_value = deducted_value
            obj.deducted_weight = deducted_weight
            obj.law = law
            obj.detector = detector
            obj.detector_other = detector_other
            obj.results = results
            obj.commitment = commitment
            obj.receip_no = receip_no
            obj.details = details
            obj.m_rec_date = datetime.now()
            #TODO: Hard Code! convert not to shanmsi
            obj.s_rec_date = '1393-05-17'
            obj.locked = locked
            Debug.dprint(vi_type_1)

            obj.save()
        print('Controller.add inside is executed')


    @classmethod
    def exists(cls ,kootaj):
        obj = Model()
        return obj.find({{'kootaj': kootaj}})

    @classmethod
    def find(cls, _filter={}, page=-1, per_page=15, sort='personnel_id', order=1):
        #TODO: This shit should be rewrite!
        # client = MongoClient('192.1.8.14', 27017)
        # db = client.Customs
        # collection = db.violation
        # records = list(collection.find())


        collection = db.violation
        records = list(collection.find())
        result = []
        for item in records:
            try:
                result.append({
                    'kootaj': str(item['kootaj']),
                    'file_no': str(item['file_no']),
                    'cert_no': str(item['cert_no']),
                    'card_no': str(item['card_no']),
                    'code_no': str(item['code_no']),
                    'tariff_no': str(item['tariff_no']),
                    'full_name': str(item['full_name']),
                })
            except:
                result.append({
                    'kootaj': 'Error',
                    'file_no': 'Error',
                    'cert_no': 'Error',
                    'company': 'Error',
                    'card_no': 'Error',
                    'code_no': 'Error',
                    'tariff_no': 'Error',
                    'full_name': 'Error',
                })

        # return records
        return result
        # return 'ok'

        # # try:
        # collection = db['violation']
        # records = collection.find()
        # result = []
        # # for item in records:
        # for item in range(5):
        #     # result.append({'kootaj': item['kootaj']})
        #     result.append('Ehsan')
        #     # obj = Model.objects(__raw__=_filter)
        #
        #     # result = []
        #     # for item in obj:
        #     #     result.append({
        #     #         'id': obj.id,
        #     #         's_date': obj.s_date,
        #     #         'm_date': obj.m_date,
        #     #         'file_no': obj.file_no,
        #     #         'kootaj': obj.kootaj,
        #     #         'cert_no': obj.cert_no,
        #     #         's_date_1': obj.s_date_1,
        #     #         's_date_2': obj.s_date_2,
        #     #         'policy_1': obj.policy_1,
        #     #         'policy_2': obj.policy_2,
        #     #         'policy_3': obj.policy_3,
        #     #         'policy_4': obj.policy_4,
        #     #         'policy_5': obj.policy_5,
        #     #         'policy_6': obj.policy_6,
        #     #         'policy_7': obj.policy_7,
        #     #         'ezharname': obj.ezharname,
        #     #         'person_type': obj.person_type,
        #     #         'full_name': obj.full_name,
        #     #         'card_no': obj.card_no,
        #     #         'code_no': obj.code_no,
        #     #         'company': obj.company,
        #     #         'ez_full_name': obj.ez_full_name,
        #     #         'ez_owner': obj.ez_owner,
        #     #         'ez_agent': obj.ez_agent,
        #     #         'ez_card_no': obj.ez_card_no,
        #     #         'ez_code_no': obj.ez_code_no,
        #     #         'tr_full_name': obj.tr_full_name,
        #     #         'tr_code_no': obj.tr_code_no,
        #     #         'tr_reg_no': obj.tr_reg_no,
        #     #         'tr_nationality': obj.tr_nationality,
        #     #         'tr_manager': obj.tr_manager,
        #     #         'tr_type': obj.tr_type,
        #     #         'item_name': obj.item_name,
        #     #         'tariff_no': obj.tariff_no,
        #     #         'paid': obj.paid,
        #     #         'different': obj.different,
        #     #         'fine': obj.fine,
        #     #         'diff_paid': obj.diff_paid,
        #     #         'vi_type_1': obj.vi_type_1,
        #     #         'vi_type_2': obj.vi_type_2,
        #     #         'vi_type_3': obj.vi_type_3,
        #     #         'vi_type_4': obj.vi_type_4,
        #     #         'vi_type_5': obj.vi_type_5,
        #     #         'vi_type_6': obj.vi_type_6,
        #     #         'vi_type_7': obj.vi_type_7,
        #     #         'vi_type_other': obj.vi_type_other,
        #     #         'stated_tariff': obj.stated_tariff,
        #     #         'stated_value': obj.stated_value,
        #     #         'stated_weight': obj.stated_weight,
        #     #         'deducted_tariff': obj.deducted_tariff,
        #     #         'deducted_value': obj.deducted_value,
        #     #         'deducted_weight': obj.deducted_weight,
        #     #         'law': obj.law,
        #     #         'detector': obj.detector,
        #     #         'detector_other': obj.detector_other,
        #     #         'results': obj.results,
        #     #         'commitment': obj.commitment,
        #     #         'receip_no': obj.receip_no,
        #     #         'details': obj.details,
        #     #         'm_rec_date': obj.m_rec_date,
        #     #         's_rec_date': obj.s_rec_date,
        #     #         'locked': obj.locked,
        #     #
        #     #                    })
        #     return result
        #     # return collection.find().count()
        # # except Exception, err:
        # #     return 'ERROR IS: '+err.message

    @classmethod
    def get(cls, id):
        try:
            obj = Model.objects.get(id=ObjectId(id))

            result = {
                    'id': obj.id,
                    's_date': obj.s_date,
                    'm_date': obj.m_date,
                    'file_no': obj.file_no,
                    'kootaj': obj.kootaj,
                    'cert_no': obj.cert_no,
                    's_date_1': obj.s_date_1,
                    's_date_2': obj.s_date_2,
                    'policy_1': obj.policy_1,
                    'policy_2': obj.policy_2,
                    'policy_3': obj.policy_3,
                    'policy_4': obj.policy_4,
                    'policy_5': obj.policy_5,
                    'policy_6': obj.policy_6,
                    'policy_7': obj.policy_7,
                    'ezharname': obj.ezharname,
                    'person_type': obj.person_type,
                    'full_name': obj.full_name,
                    'card_no': obj.card_no,
                    'code_no': obj.code_no,
                    'company': obj.company,
                    'ez_full_name': obj.ez_full_name,
                    'ez_owner': obj.ez_owner,
                    'ez_agent': obj.ez_agent,
                    'ez_card_no': obj.ez_card_no,
                    'ez_code_no': obj.ez_code_no,
                    'tr_full_name': obj.tr_full_name,
                    'tr_code_no': obj.tr_code_no,
                    'tr_reg_no': obj.tr_reg_no,
                    'tr_nationality': obj.tr_nationality,
                    'tr_manager': obj.tr_manager,
                    'tr_type': obj.tr_type,
                    'item_name': obj.item_name,
                    'tariff_no': obj.tariff_no,
                    'paid': obj.paid,
                    'different': obj.different,
                    'fine': obj.fine,
                    'diff_paid': obj.diff_paid,
                    'vi_type_1': obj.vi_type_1,
                    'vi_type_2': obj.vi_type_2,
                    'vi_type_3': obj.vi_type_3,
                    'vi_type_4': obj.vi_type_4,
                    'vi_type_5': obj.vi_type_5,
                    'vi_type_6': obj.vi_type_6,
                    'vi_type_7': obj.vi_type_7,
                    'vi_type_other': obj.vi_type_other,
                    'stated_tariff': obj.stated_tariff,
                    'stated_value': obj.stated_value,
                    'stated_weight': obj.stated_weight,
                    'deducted_tariff': obj.deducted_tariff,
                    'deducted_value': obj.deducted_value,
                    'deducted_weight': obj.deducted_weight,
                    'law': obj.law,
                    'detector': obj.detector,
                    'detector_other': obj.detector_other,
                    'results': obj.results,
                    'commitment': obj.commitment,
                    'receip_no': obj.receip_no,
                    'details': obj.details,
                    'm_rec_date': obj.m_rec_date,
                    's_rec_date': obj.s_rec_date,
                    'locked': obj.locked,

                      }
            return result
        except Exception, err:
            return err.message

    #TODO: need to implementation
    @classmethod
    def delete(cls, id):
        try:
            return True
        except Exception, err:
            return err.message
