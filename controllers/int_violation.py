__author__ = 'ehsan'
from models.int_violation import Intviolation as Model
from datetime import datetime


class Intviolation():
    def __init__(self):
        pass

    @classmethod
    def add(cls, id='', kootaj='', cert_no='', s_date='', m_date='', int_cert_no='', radif_marzi='', s_entry_date='',
            m_entry_date='', karne_tir_no='', ezhar_1=False, ezhar_2=False, ezhar_3=False, ezhar_4=False,
            person_type=False, full_name='', card_no='', code_no='', dest_address='', good_name='', net_weight='',
            weight='', input_tariff='', good_count=0, price=0, truck_no='', driver_name='', chasis_no='', trailer_no='',
            iranian_truck=False, truck_address='', truck_type=0, vi_type_1=False, vi_type_2=False, vi_type_3=False,
            vi_type_4=False, vi_type_5=False, vi_type_6=False, vi_type_7=False, detector=0, detector_other='',
            fine_receipt_no='', fine_price=0, final_result=0, details='', m_rec_date='', s_rec_date='', locked=False):


        if id != '':
            obj = Model.objects(Kootaj=id).first()
        else:
            obj = Model()

        if obj != None:
            obj.kootaj = kootaj
            obj.cert_no = cert_no
            obj.s_date = s_date
            #TODO it should use s_date
            obj.m_date = datetime.now()
            obj.int_cert_no = int_cert_no
            obj.radif_marzi = radif_marzi
            obj.s_entry_date = s_entry_date
            #TODO it should use s_entry_date
            obj.m_entry_date = datetime.now()
            obj.karne_tir_no = karne_tir_no
            obj.ezhar_1 = ezhar_1
            obj.ezhar_2 = ezhar_2
            obj.ezhar_3 = ezhar_3
            obj.ezhar_4 = ezhar_4
            obj.person_type = person_type
            obj.full_name = full_name
            obj.card_no = card_no
            obj.code_no = code_no
            obj.dest_address = dest_address
            obj.good_name = good_name
            obj.net_weight = net_weight
            obj.weight = weight
            obj.input_tariff = input_tariff
            obj.good_count = good_count
            obj.price = price
            obj.truck_no = truck_no
            obj.driver_name = driver_name
            obj.chasis_no = chasis_no
            obj.trailer_no = trailer_no
            obj.iranian_truck = iranian_truck
            obj.truck_address = truck_address
            obj.truck_type = truck_type
            obj.vi_type_1 = vi_type_1
            obj.vi_type_2 = vi_type_2
            obj.vi_type_3 = vi_type_3
            obj.vi_type_4 = vi_type_4
            obj.vi_type_5 = vi_type_5
            obj.vi_type_6 = vi_type_6
            obj.vi_type_7 = vi_type_7
            obj.detector = detector
            obj.detector_other = detector_other
            obj.fine_receipt_no = fine_receipt_no
            obj.fine_price = fine_price
            obj.final_result = final_result
            obj.details = details
            obj.m_rec_date = datetime.now()
            #TODO: Hard Code! convert not to shanmsi
            obj.s_rec_date = '1393-05-17'
            obj.locked = locked

            obj.save()


    @classmethod
    def exists(cls ,kootaj):
        obj = Model()
        return obj.find({{'kootaj': kootaj}})

    @classmethod
    def find(cls, _filter={}, page=-1, per_page=15, sort='personnel_id', order=1):
        try:
            obj = Model.objects(__raw__=_filter)

            result = []
            for item in obj:
                result.append({
                    'id': obj.id,
                    'kootaj': obj.kootaj,
                    'cert_no': obj.cert_no,
                    's_date': obj.s_date,
                    'm_date': obj.m_date,
                    'int_cert_no': obj.int_cert_no,
                    'radif_marzi': obj.radif_marzi,
                    's_entry_date': obj.s_entry_date,
                    'm_entry_date': obj.m_entry_date,
                    'karne_tir_no': obj.karne_tir_no,
                    'ezhar_1': obj.ezhar_1,
                    'ezhar_2': obj.ezhar_2,
                    'ezhar_3': obj.ezhar_3,
                    'ezhar_4': obj.ezhar_4,
                    'person_type': obj.person_type,
                    'full_name': obj.full_name,
                    'card_no': obj.card_no,
                    'code_no': obj.code_no,
                    'dest_address': obj.dest_address,
                    'good_name': obj.good_name,
                    'net_weight': obj.net_weight,
                    'weight': obj.weight,
                    'input_tariff': obj.input_tariff,
                    'good_count': obj.good_count,
                    'price': obj.price,
                    'truck_no': obj.truck_no,
                    'driver_name': obj.driver_name,
                    'chasis_no': obj.chasis_no,
                    'trailer_no': obj.trailer_no,
                    'iranian_truck': obj.iranian_truck,
                    'truck_address': obj.truck_address,
                    'truck_type': obj.truck_type,
                    'vi_type_1': obj.vi_type_1,
                    'vi_type_2': obj.vi_type_2,
                    'vi_type_3': obj.vi_type_3,
                    'vi_type_4': obj.vi_type_4,
                    'vi_type_5': obj.vi_type_5,
                    'vi_type_6': obj.vi_type_6,
                    'vi_type_7': obj.vi_type_7,
                    'detector': obj.detector,
                    'detector_other': obj.detector_other,
                    'fine_receipt_no': obj.fine_receipt_no,
                    'fine_price': obj.fine_price,
                    'final_result': obj.final_result,
                    'details': obj.details,
                    'm_rec_date': obj.m_rec_date,
                    's_rec_date': obj.s_rec_date,
                    'locked': obj.locked,

                               })
            return result
        except Exception, err:
            return err.message

    @classmethod
    def get(cls, id):
        try:
            obj = Model.objects.get(id=ObjectId(id))

            result = {
                    'id': obj.id,
                    'kootaj': obj.kootaj,
                    'cert_no': obj.cert_no,
                    's_date': obj.s_date,
                    'm_date': obj.m_date,
                    'int_cert_no': obj.int_cert_no,
                    'radif_marzi': obj.radif_marzi,
                    's_entry_date': obj.s_entry_date,
                    'm_entry_date': obj.m_entry_date,
                    'karne_tir_no': obj.karne_tir_no,
                    'ezhar_1': obj.ezhar_1,
                    'ezhar_2': obj.ezhar_2,
                    'ezhar_3': obj.ezhar_3,
                    'ezhar_4': obj.ezhar_4,
                    'person_type': obj.person_type,
                    'full_name': obj.full_name,
                    'card_no': obj.card_no,
                    'code_no': obj.code_no,
                    'dest_address': obj.dest_address,
                    'good_name': obj.good_name,
                    'net_weight': obj.net_weight,
                    'weight': obj.weight,
                    'input_tariff': obj.input_tariff,
                    'good_count': obj.good_count,
                    'price': obj.price,
                    'truck_no': obj.truck_no,
                    'driver_name': obj.driver_name,
                    'chasis_no': obj.chasis_no,
                    'trailer_no': obj.trailer_no,
                    'iranian_truck': obj.iranian_truck,
                    'truck_address': obj.truck_address,
                    'truck_type': obj.truck_type,
                    'vi_type_1': obj.vi_type_1,
                    'vi_type_2': obj.vi_type_2,
                    'vi_type_3': obj.vi_type_3,
                    'vi_type_4': obj.vi_type_4,
                    'vi_type_5': obj.vi_type_5,
                    'vi_type_6': obj.vi_type_6,
                    'vi_type_7': obj.vi_type_7,
                    'detector': obj.detector,
                    'detector_other': obj.detector_other,
                    'fine_receipt_no': obj.fine_receipt_no,
                    'fine_price': obj.fine_price,
                    'final_result': obj.final_result,
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
