__author__ = 'ehsan'
from models.personnel import Personnel as Model


class Personnel():
    def __init__(self):
        pass

    @classmethod
    def add(cls, id='', name='', family='', personnel_id='', username='', password='', district=''):
        print('personnel id:')
        print(personnel_id)

        if id != '':
            obj = Model.objects(Kootaj=id).first()

        else:
            obj = Model()

        if obj != None:
            obj.name = name
            obj.family = family
            obj.personnel_id = personnel_id
            obj.username = username
            obj.password = password
            obj.district = district

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
                    'name': obj.name,
                    'family': obj.family,
                    'personnel_id': obj.personnel_id,
                    'username': obj.username,
                    'password': obj.password,
                    'district': obj.district,

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
                    'name': obj.name,
                    'family': obj.family,
                    'personnel_id': obj.personnel_id,
                    'username': obj.username,
                    'password': obj.password,
                    'district': obj.district,
                      }
            return result
        except Exception, err:
            return err.message

    #TODO: need to implementation
    @classmethod
    def delete(cls, id):
        try:
            Model.objects(id=ObjectId(id)).delete()
            return True
        except Exception, err:
            return err.message
