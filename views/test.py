#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

# from controllers.old.file import File as Controller
import os
# from tools.redis import Redis
# from connections import redis_instance
# from tools.session import Session
from pycket.session import SessionManager
# from controllers.violation import Violation
from models.violation import Violation as Model
from pymongo import MongoClient


class Pull(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.write(os.path.dirname(os.path.realpath(__file__)))
        self.write('<br>')
        os.system("mkdir ehsan")
        self.write(os.path.dirname(os.path.realpath(__file__)))

class Zzz(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        # redis_instance.set(name='name', value='EHSAN')
        # self.write(redis_instance.get(name='name'))
        session = SessionManager(self)
        # session.set('key', 'OMG')
        session['key'] = 'OMG'
        self.write('done')
        #
        # Session.set(handler=self, name='name', value='EHSAN Omg')
        # self.write(str(Session.get(handler=self, name='name')))

class Yyy(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        # redis_instance.set(name='name', value='EHSAN')
        # self.write(redis_instance.get(name='name'))
        session = SessionManager(self)

        self.write(str(session.keys()))
        # self.write(str(session['key']))
        #
        # Session.set(handler=self, name='name', value='EHSAN Omg')
        # self.write(str(Session.get(handler=self, name='name')))

class Data(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client.Customs
        collection = db['violation']
        records = collection.find()
        # records = list(Model.objects.all())
        # records = Violation.find()
        self.write('ok?')
        self.write(str(records))