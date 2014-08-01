__author__ = 'ehsan'
from models.edit_request import Editrequest as Model


class Editrequest():
    def __init__(self):
        pass

    @classmethod
    def add(cls, id='', user_id='', s_date='', m_date='', violation_id='', reason=''):


        if id != '':
            obj = Model.objects(Kootaj=id).first()

        else:
            obj = Model()

        if obj != None:
            obj.user_id = user_id
            obj.s_date = s_date
            obj.m_date = m_date
            obj.violation_id = violation_id
            obj.reason = reason

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
                    'user_id': obj.user_id,
                    's_date': obj.s_date,
                    'm_date': obj.m_date,
                    'violation_id': obj.violation_id,
                    'reason': obj.reason,

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
                    'user_id': obj.user_id,
                    's_date': obj.s_date,
                    'm_date': obj.m_date,
                    'violation_id': obj.violation_id,
                    'reason': obj.reason,

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
