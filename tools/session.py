__author__ = 'ehsan'
from pycket.session import SessionManager
from debug import Debug


class Session:
    def __init__(self):
        pass

    @classmethod
    def get(cls, handler, name):
        session = SessionManager(handler)
        # print "Session name is: " + name
        # print "Do we have a session? " + str(session.get(name))
        # if cls.exists(handler, name):
        #     print "There is a session"
        # else:
        #     print "There is not any sessionn"
        return session.get(name)

    @classmethod
    def set(cls, handler, name, value):
        # Debug.dprint(text='INSIDE SESSION SET')
        # Debug.dprint(text='name: ' + name, type='data')
        # Debug.dprint(text='value: ' + str(value), type='data')
        session = SessionManager(handler)
        session.set(name=name, value=value)
        # Debug.dprint(text='INSIDE SESSION SET I GET')
        # Debug.dprint(text='value: ' + str(session.get(name=name)), type='data')
    #TODO not implemented yed
    @classmethod
    def exists(cls, handler, name):
        session = SessionManager(handler)
        # print "Inside exist: " + name + ' ' + str(session.get(name))
        return session.get(name) != None

    @classmethod
    def delete(cls, handler, name):
        session = SessionManager(handler)
        session.delete(name)
