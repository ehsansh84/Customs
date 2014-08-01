__author__ = 'ehsan'
from models.file import File as Model


class File():
    def __init__(self):
        pass

    @classmethod
    def add(cls, id='', kootaj='', desc=''):


        if id != '':
            obj = Model.objects(Kootaj=id).first()

        else:
            obj = Model()

        if obj != None:
            obj.kootaj = kootaj
            obj.desc = desc

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
                    'desc': obj.desc,

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
                    'desc': obj.desc,

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
