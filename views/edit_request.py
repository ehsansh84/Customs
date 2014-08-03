import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from controllers.edit_request import Editrequest as Controller


class Editrequest(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('Editrequest.html')

    def post(self, *args, **kwargs):
        user_id = self.get_argument('user_id', '999')
        violation_id = self.get_argument('action_no', '')
        reason = self.get_argument('text', '')

        # self.write('user_id:' + str(user_id)+'<br>')
        # self.write('violation_id:' + str(violation_id)+'<br>')
        # self.write('reason:' + str(reason)+'<br>')

        Controller.add(user_id=user_id, violation_id=violation_id, reason=reason)


class EditrequestList(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('edit_requests.html')

    def post(self, *args, **kwargs):
        # user_id = self.get_argument('user_id', '999')
        # violation_id = self.get_argument('action_no', '')
        # reason = self.get_argument('text', '')

        # self.write('user_id:' + str(user_id)+'<br>')
        # self.write('violation_id:' + str(violation_id)+'<br>')
        # self.write('reason:' + str(reason)+'<br>')

        # Controller.add(user_id=user_id, violation_id=violation_id, reason=reason)
        pass