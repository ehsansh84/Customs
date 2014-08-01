__author__ = 'ehsan'
from models.personnel import Personnel as Model


class UserActions():
    def __init__(self):
        pass

    @classmethod
    def store_in_session(cls, handler, user_id):
        return {}

    @classmethod
    def get_from_session(cls, handler):
        return {}

    @classmethod
    def user_logged(cls, handler):
        return False

    @classmethod
    def user_exists(cls, user_email, username):
        return False

    @classmethod
    def logout(cls, handler):
        # Session.delete(handler=handler, name='user')
        pass

    @classmethod
    def login(cls, handler, username, password):
        # Session.set(handler=handler, name='SocialResult', value=result)
        # handler.redirect("/register")
        pass

    # @classmethod
    # def get_dic(cls, handler):
    #     user_data = cls.get_from_session(handler=handler)
    #     Debug.dprint(text='----------------------------------------- From session', type='data')
    #     Debug.dprint(text=user_data, type='data')
    #     user_info = user_data['user']['user_info']
    #     Debug.dprint(text='----------------------------------------- User info', type='data')
    #     Debug.dprint(text=user_info, type='data')
    #     channels = user_data['user']['channels']
    #     Debug.dprint(text='----------------------------------------- Channel dic', type='data')
    #     Debug.dprint(text=channels, type='data')
    #     return {"user_info": user_info, "channels": channels}
