
__author__ = 'ehsan'

from models.borrow import Borrow as Model


class Borrow():
    def __init__(self):
        pass
        # self.personnel_id = personnel_id
        # self.file_id = file_id
        # self.date = date
        # self.flow = flow
        # self.returned = returned

    @classmethod
    def add(cls, _id, personnel_id='', file_id='', date='', flow='', returned=False):
        obj = Model(personnel_id=personnel_id, file_id=file_id, date=date, flow=flow, returned=returned)
        obj.set_id(_id=_id)
        obj.create()

    @classmethod
    def exists(cls, username):
        obj = Model()
        return obj.find({'username': username})

    @classmethod
    def all(cls, _filter=None, page=-1, perpage=15, sort='personnel_id', order=1):
        try:
            obj = Model()
            obj.find(_filter=_filter, page=page, perpage=perpage, sort=sort, order=order)

            result = []
            while not obj.eof:
                result.append({
                               '_id': obj.get_id(),
                               'personnel_id': obj.personnel_id,
                               'file_id': obj.file_id,
                               'personnel_id': obj.personnel_id,
                               'date': obj.date,
                               'flow': obj.flow,
                               'returned': obj.returned,
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
            result = {
                       '_id': obj.get_id(),
                       'personnel_id': obj.personnel_id,
                       'file_id': obj.file_id,
                       'personnel_id': obj.personnel_id,
                       'date': obj.date,
                       'flow': obj.flow,
                       'returned': obj.returned,
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