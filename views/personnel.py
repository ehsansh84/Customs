#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from controllers.personnel import Personnel as Controller


class Personnel(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        acc_type = Redis.get(key='acc_type')
        if acc_type == 'admin':
            permissions = Redis.get(key='permissions', type='list')
            self.render('personnel.html',
                        permissions=permissions
)
        else:
            self.redirect('/')

    def post(self, *args, **kwargs):
        personnel_id = self.get_argument('personnel_id', '99')
        name = self.get_argument('name', '')
        family = self.get_argument('family', '')
        district = self.get_argument('district', '')
        username = self.get_argument('username', '')
        password = self.get_argument('password', '')
        print(personnel_id)
        Controller.add(id='', name=name, family=family, district=district, username=username, password=password, personnel_id=personnel_id)
        self.write(personnel_id)
        self.write(name)
        self.write(family)
        self.write(district)
        self.write(username)
        self.write(password)


class GetPersonnel(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.write('No get method allowed')

    def post(self, *args, **kwargs):
        id = self.get_argument('id', '')
        # if id dont existed , return -2
        user = {
            'name': 'pooria',
            'family': 'sadeghy',
            'district': '15',
            'username': 'ali',
            'password': '123456'
        }
        output_result = json.dumps(user)
        self.write(output_result)
        # return -2


