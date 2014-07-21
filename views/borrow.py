#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from controllers.file import File as Controller


class Borrow(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('borrow.html')

    def post(self, *args, **kwargs):
        personnel_id = self.get_argument('personnel_id', '')
        file_id = self.get_argument('file_id', '')
        date = self.get_argument('date', '')
        flow = self.get_argument('flow', '')
        returned = self.get_argument('returned', '')
        Controller.add(_id='', personnel_id=personnel_id, file_id=file_id, date=date, flow=flow, returned=returned)
        self.write(personnel_id)
        self.write(file_id)
        self.write(flow)
        self.write(returned)
