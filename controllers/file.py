__author__ = 'ehsan'
from models.file import File as Model


class File():
    def __init__(self):
        pass

    @classmethod
    def add(cls, _id, kootaj, desc=''):
        obj = Model(kootaj=kootaj, desc=desc)
        obj.set_id(_id=_id)
        obj.create()

    @classmethod
    def exists(cls, kootaj):
        obj = Model()
        return obj.find({'kootaj': kootaj})

    @classmethod
    def all(cls, _filter=None, page=-1, perpage=15, sort='kootaj', order=1):
        try:
            obj = Model()
            obj.find(_filter=_filter, page=page, perpage=perpage, sort=sort, order=order)

            result = []
            while not obj.eof:
                result.append({'kootaj': obj.kootaj,
                               'desc': obj.desc,
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
            result = {'kootaj': obj.kootaj,
                      'desc': obj.desc,
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