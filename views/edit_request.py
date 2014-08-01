import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from controllers.edit_request import Editrequest as Controller


class Editrequest(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('Editrequest.html')

    def post(self, *args, **kwargs):
        id = self.get_argument('id','')
        user_id = self.get_argument('user_id', '')
        s_date = self.get_argument('s_date', '')
        m_date = self.get_argument('m_date', '')
        violation_id = self.get_argument('violation_id', '')
        reason = self.get_argument('reason', '')

        self.write('user_id:' + str(user_id)+'<br>')
        self.write('s_date:' + str(s_date)+'<br>')
        self.write('m_date:' + str(m_date)+'<br>')
        self.write('violation_id:' + str(violation_id)+'<br>')
        self.write('reason:' + str(reason)+'<br>')

        Controller.add(id=id, user_id=user_id, s_date=s_date, m_date=m_date, violation_id=violation_id, reason=reason)
