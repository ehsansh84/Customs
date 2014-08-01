__author__ = 'ehsan'
from models.borrow import Borrow as Model


class Borrow():
    def __init__(self):
        pass

    @classmethod
    def add(cls, id='', personnel_id=0, file_id=0, date='', flow=[], returned=False):


        if id != '':
            obj = Model.objects(Kootaj=id).first()

        else:
            obj = Model()

        if obj != None:
            obj.personnel_id = personnel_id
            obj.file_id = file_id
            obj.date = date
            obj.flow = flow
            obj.returned = returned

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
                    'personnel_id': obj.personnel_id,
                    'file_id': obj.file_id,
                    'date': obj.date,
                    'flow': obj.flow,
                    'returned': obj.returned,

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
                    'personnel_id': obj.personnel_id,
                    'file_id': obj.file_id,
                    'date': obj.date,
                    'flow': obj.flow,
                    'returned': obj.returned,

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
