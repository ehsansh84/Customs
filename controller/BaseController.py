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


# home page
class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('home.html')

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
        self.render('login.html')

    def post(self, *args, **kwargs):
        username = self.get_argument('username', '')
        password = self.get_argument('password', '')
        if username == 'admin' and password == '123':
            Redis.set(key='acc_type', value='admin')
        elif username == 'user' and password == '111111':
            Redis.set(key='acc_type', value='user')
        else:
            Redis.set(key='acc_type', value='no acc')

        # Session.set(handler=self, name='acc_type', value='admin')
        self.write(username)
        self.write(password)
        self.write(str(Redis.get(key='acc_type')))
        # self.write(Session.get(handler=self, name='acc_type'))


class IntViolationHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('IntViolation.html')

class ErrorReportHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('error_report.html')
    def post(self, *args, **kwargs):
        self.render('error_report_table.html')


