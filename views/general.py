__author__ = 'ehsan'
#!/usr/bin/env python
# -*- coding: utf-8 -*-


import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tools.redis import Redis


class Logout(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        Redis.set(key='acc_type', value='')
        self.render('login.html', msg='')
