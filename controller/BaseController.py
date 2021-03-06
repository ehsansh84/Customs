#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
# import datetime
# import json
# import time
# from pycket.session import SessionManager
# from tornado.options import define, options
# from tools.session import Session
from tools.redis import Redis
from models.user import User


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('login.html', msg='')

# home page
class FormHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('form.html')

class TableHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('table.html')

class ErrorHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('404.html')

class StepFormHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('step_form.html')

class LoginHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('login.html', msg='')

    def post(self, *args, **kwargs):
        username = self.get_argument('username', '')
        password = self.get_argument('password', '')
        # obj = User()
        # self.write(str(User.objects(__raw__={'username': username, 'password': password})))
        # self.write(username)
        # self.write(password)
        # self.write('USERS: ')
        records = User.objects(__raw__={'username': username, 'password': password})
        if len(records) > 0:
            type = records[0].type
            Redis.set(key='acc_type', value=type)
            # self.write()
            # self.write(records[0].name)
            if type == 'admin':
                permission = {'main': True,
                              'violation': True,
                              'int_violation': True,
                              'login':True,
                              'logout': True,
                              'report': True}
                Redis.set(key='permissions', value=permission, type='list')
                self.redirect('/violation')
            elif type == 'user':
                permission = {'main': True,
                              'violation': False,
                              'int_violation': False,
                              'login':True,
                              'logout': True,
                              'report': True}
                Redis.set(key='permissions', value=permission, type='list')
                self.redirect('/violation_search')

            # self.write('Yes')
        else:
            self.render('login.html', msg='اطلاعات کاربری صحیح نیست')

            self.write('No!')

        # self.write(str(len(User.objects(__raw__={'username': username, 'password': password}))))

        # if User.objects.first() == None:
        #     self.write('NO USER')
        # else:
        #     self.write('HAS USER')

        # if username == 'admin' and password == '123':
        #     Redis.set(key='acc_type', value='admin')
        #     permission = {'main': True,
        #                   'violation': True,
        #                   'int_violation': True,
        #                   'login':True,
        #                   'logout': True,
        #                   'report': True}
        #     Redis.set(key='permissions', value=permission, type='list')
        #     self.redirect('/violation')
        # elif username == 'user' and password == '111111':
        #     Redis.set(key='acc_type', value='user')
        #     permission = {'main': True,
        #                   'violation': False,
        #                   'int_violation': False,
        #                   'login':True,
        #                   'logout': True,
        #                   'report': True}
        #     Redis.set(key='permissions', value=permission, type='list')
        #     self.redirect('/violation_search')
        # elif username == 'bazrasi' and password == 'Ax@1245':
        #     Redis.set(key='acc_type', value='user')
        #     permission = {'main': True,
        #                   'violation': False,
        #                   'int_violation': False,
        #                   'login':True,
        #                   'logout': True,
        #                   'report': True}
        #     Redis.set(key='permissions', value=permission, type='list')
        #     self.redirect('/violation_search')
        # elif username == 'harasat' and password == 'Xd@1394':
        #     Redis.set(key='acc_type', value='user')
        #     permission = {'main': True,
        #                   'violation': False,
        #                   'int_violation': False,
        #                   'login':True,
        #                   'logout': True,
        #                   'report': True}
        #     Redis.set(key='permissions', value=permission, type='list')
        #     self.redirect('/violation_search')
        # else:
        #     # Redis.set(key='acc_type', value='no acc')
        #     self.render('login.html')













        # Session.set(handler=self, name='acc_type', value='admin')
        # self.write(username)
        # self.write(password)
        # self.write(str(Redis.get(key='acc_type')))
        # self.write(Session.get(handler=self, name='acc_type'))


#
# class IntViolationHandler(tornado.web.RequestHandler):
#
#     def get(self):
#         acc_type = Redis.get(key='acc_type')
#         if acc_type == 'admin':
#             self.render('IntViolation.html')
#         else:
#             self.redirect('/login')

class ErrorReportHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('error_report.html')
    def post(self, *args, **kwargs):
        self.render('error_report_table.html')


