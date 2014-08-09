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
from connections import redis_instance


class Pull(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.write(os.path.dirname(os.path.realpath(__file__)))
        self.write('<br>')
        os.system("mkdir ehsan")
        self.write(os.path.dirname(os.path.realpath(__file__)))

class Zzz(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.write('Begin\n\n')
        redis_instance.set(name='name', value='EHSAN')
        self.write(redis_instance.get(name='name'))
        # self.write(Redis.get(key='name'))
