__author__ = 'ehsan'


class Cookie:
    def __init__(self):
        pass

    #TODO: should renamed to set
    @classmethod
    def set_cookie(cls, handler, name, data):
        handler.set_secure_cookie(name=name, value=data, expires_days=30,domain="360viral.com")

    #TODO: should renamed to get
    @classmethod
    def get_cookie(cls, handler, name):
        return handler.get_secure_cookie(name)

    @classmethod
    def delete(cls, handler, name):
        return handler.clear_cookie(name)

    @classmethod
    def exists(cls, handler, name):
        return not (handler.get_secure_cookie(name) == "" or handler.get_secure_cookie(name) == None)

