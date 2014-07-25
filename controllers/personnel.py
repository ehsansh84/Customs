__author__ = 'ehsan'
from models.personnel import Personnel as Model


class Personnel():
    def __init__(self):
        pass

    @classmethod
    def add(cls, _id, name='', family='', personnel_id='', district='', username='', password=''):

        obj = Model(name=name, family=family, personnel_id=personnel_id, district=district, username=username,
                    password=password)
        # print 'PERSON'
        print personnel_id
        obj.set_id(_id=_id)
        obj.create()

    @classmethod
    def exists(cls, username):
        obj = Model()
        return obj.find({'username': username})

    @classmethod
    def all(cls, _filter=None, page=-1, perpage=15, sort='family', order=1):
        try:
            obj = Model()
            obj.find(_filter=_filter, page=page, perpage=perpage, sort=sort, order=order)

            result = []
            while not obj.eof:
                result.append({'name': obj.name,
                               'family': obj.family,
                               'personnel_id': obj.personnel_id,
                               'district': obj.district,
                               'username': obj.username,
                               'password': obj.password,
                               '_id': obj.get_id(),
                               })
                obj.next()
            return result
        except Exception, err:
            return err.message

    @classmethod
    def get(cls, _id):
        try:
            obj = Model()
            obj.set_id(_id)
            obj.load()
            result = {'name': obj.name,
                      'family': obj.family,
                      'personnel_id': obj.personnel_id,
                      'district': obj.district,
                      'username': obj.username,
                      'password': obj.password,
                      '_id': obj.get_id(),
                      }
            return result
        except Exception, err:
            return err.message

    @classmethod
    def delete(cls, _id):
        try:
            obj = Model()
            obj.set_id(_id)
            obj.remove()
            return True
        except Exception, err:
            return err.message