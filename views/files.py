#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from controllers.file import File as Controller
import json


class File(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('file.html')

    def post(self, *args, **kwargs):
        kootaj = self.get_argument('kootaj', '')
        desc = self.get_argument('desc', '')
        Controller.add(_id='', kootaj=kootaj, desc=desc)
        self.write(kootaj)
        self.write(desc)


class GetFile(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.write('No get method allowed')

    def post(self, *args, **kwargs):
        kootaj = self.get_argument('kootaj', '')

        if Controller.all(_filter={'kootaj': kootaj}):
            shape = {
                'explain': 'OK EHSAN',
            }
        else:
            shape = {
                'explain': 'NO EHSAN',
            }
        # if id dont existed , return -2
        output_result = json.dumps(shape)
        self.write(output_result)
        # return -2
