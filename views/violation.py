#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from controllers.violation import Violation as Controller
from tools.redis import Redis


class Violation(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        acc_type = Redis.get(key='acc_type')
        if acc_type == 'admin':
            permissions = Redis.get(key='permissions', type='list')
            # self.write(permissions)
            self.render('Violation.html', permissions=permissions, type='list')
        else:
            self.redirect('/login')


    def post(self, *args, **kwargs):
        id = self.get_argument('id','')
        s_date = self.get_argument('s_date', '')
        m_date = self.get_argument('m_date', '')
        file_no = self.get_argument('file_no', '')
        kootaj = self.get_argument('kootaj', '')
        cert_no = self.get_argument('cert_no', '')
        s_date_1 = self.get_argument('s_date_1', '')
        s_date_2 = self.get_argument('s_date_2', '')
        policy_1 = self.get_argument('policy_1', False)
        policy_2 = self.get_argument('policy_2', False)
        policy_3 = self.get_argument('policy_3', False)
        policy_4 = self.get_argument('policy_4', False)
        policy_5 = self.get_argument('policy_5', False)
        policy_6 = self.get_argument('policy_6', False)
        policy_7 = self.get_argument('policy_7', False)
        ezharname = self.get_argument('ezharname', 0)
        person_type = self.get_argument('person_type', False)
        full_name = self.get_argument('full_name', '')
        card_no = self.get_argument('card_no', '')
        code_no = self.get_argument('code_no', '')
        company = self.get_argument('company', '')
        ez_full_name = self.get_argument('ez_full_name', '')
        ez_owner = self.get_argument('ez_owner', '')
        ez_agent = self.get_argument('ez_agent', '')
        ez_card_no = self.get_argument('ez_card_no', '')
        ez_code_no = self.get_argument('ez_code_no', '')
        tr_full_name = self.get_argument('tr_full_name', '')
        tr_code_no = self.get_argument('tr_code_no', '')
        tr_reg_no = self.get_argument('tr_reg_no', '')
        tr_nationality = self.get_argument('tr_nationality', '')
        tr_manager = self.get_argument('tr_manager', '')
        tr_type = self.get_argument('tr_type', False)
        item_name = self.get_argument('item_name', '')
        tariff_no = self.get_argument('tariff_no', '')
        paid = self.get_argument('paid', 0)
        different = self.get_argument('different', 0)
        fine = self.get_argument('fine', 0)
        diff_paid = self.get_argument('diff_paid', 0)
        vi_type_1 = self.get_argument('vi_type_1', False)
        vi_type_2 = self.get_argument('vi_type_2', False)
        vi_type_3 = self.get_argument('vi_type_3', False)
        vi_type_4 = self.get_argument('vi_type_4', False)
        vi_type_5 = self.get_argument('vi_type_5', False)
        vi_type_6 = self.get_argument('vi_type_6', False)
        vi_type_7 = self.get_argument('vi_type_7', False)
        vi_type_other = self.get_argument('vi_type_other', '')
        stated_tariff = self.get_argument('stated_tariff', 0)
        stated_value = self.get_argument('stated_value', 0)
        stated_weight = self.get_argument('stated_weight', 0)
        deducted_tariff = self.get_argument('deducted_tariff', 0)
        deducted_value = self.get_argument('deducted_value', 0)
        deducted_weight = self.get_argument('deducted_weight', 0)
        law = self.get_argument('law', '')
        detector = self.get_argument('detector', 0)
        detector_other = self.get_argument('detector_other', '')
        results = self.get_argument('results', '')
        commitment = self.get_argument('commitment', False)
        receip_no = self.get_argument('receip_no', '')
        details = self.get_argument('details', '')
        m_rec_date = self.get_argument('m_rec_date', '')
        s_rec_date = self.get_argument('s_rec_date', '')
        locked = self.get_argument('locked', False)

        person_type = True if person_type == 1 else False
        tr_type = True if person_type == 1 else False

        Controller.add(id=id, s_date=s_date, m_date=m_date, file_no=file_no, kootaj=kootaj, cert_no=cert_no,
                       s_date_1=s_date_1, s_date_2=s_date_2, policy_1=policy_1, policy_2=policy_2, policy_3=policy_3,
                       policy_4=policy_4, policy_5=policy_5, policy_6=policy_6, policy_7=policy_7, ezharname=ezharname,
                       person_type=person_type, full_name=full_name, card_no=card_no, code_no=code_no, company=company,
                       ez_full_name=ez_full_name, ez_owner=ez_owner, ez_agent=ez_agent, ez_card_no=ez_card_no,
                       ez_code_no=ez_code_no, tr_full_name=tr_full_name, tr_code_no=tr_code_no, tr_reg_no=tr_reg_no,
                       tr_nationality=tr_nationality, tr_manager=tr_manager, tr_type=tr_type, item_name=item_name,
                       tariff_no=tariff_no, paid=paid, different=different, fine=fine, diff_paid=diff_paid,
                       vi_type_1=vi_type_1, vi_type_2=vi_type_2, vi_type_3=vi_type_3, vi_type_4=vi_type_4,
                       vi_type_5=vi_type_5, vi_type_6=vi_type_6, vi_type_7=vi_type_7, vi_type_other=vi_type_other,
                       stated_tariff=stated_tariff, stated_value=stated_value, stated_weight=stated_weight,
                       deducted_tariff=deducted_tariff, deducted_value=deducted_value, deducted_weight=deducted_weight,
                       law=law, detector=detector, detector_other=detector_other, results=results,
                       commitment=commitment, receip_no=receip_no, details=details, locked=locked)
        print('Controller.add is executed')
        # self.render('Violation.html')
        self.redirect('/violation')
        # self.write(policy_5)
        # self.write(person_type)


class ViolationData(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        acc_type = Redis.get(key='acc_type')
        if acc_type == 'admin':
            permissions = Redis.get(key='permissions')
            self.write(permissions)
            # self.render('Violation.html', permissions=permissions, type='list')
        else:
            self.redirect('/login')



class ViolationSearch(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.write('Data')
        # self.write(str(list(Controller.find())))
        acc_type = Redis.get(key='acc_type')
        if acc_type == 'admin' or acc_type == 'user':
            permissions = Redis.get(key='permissions', type='list')
            search = ''
            fields = self.get_argument('fields', '')
            records = {}

            if fields != '':

                #To determone if it's a search or not
                search = 'search'

                fields = fields.split('|')

                perPage = self.get_argument('perPage', 10)
                page = self.get_argument('page', 1)

                fieldSearch = self.get_argument('fieldSearch', '')
                # self.write('FIELDS:')
                # self.write(fieldSearch)
                values = []
                filter = {}
                if fieldSearch != '':

                    fieldSearch = fieldSearch.split('|')

                    for item in fieldSearch:
                        value = {}
                        value['name'] = item
                        value['value'] = self.get_argument(item, '')
                        if value['value'] != '':
                            values.append(value)
                            filter[item] = self.get_argument(item, '')

                self.write('<br>VALUES:')
                self.write(str(values))
                self.write('<br>FILTER:')
                self.write(str(filter))

                records = {
                    'items': [],
                    'record_count': 30
                }

                # for x in range(0, 3):
                #     record = {}
                #     for item in fields:
                #         record[item] = 'Shit?'
                #     records['items'].append(record)

                records['items'] = Controller.find(_filter=filter)
                records['record_count'] = len(records['items'])


            FieldList = [
                {
                'name' : "file_no",
                'label' : "شماره پرونده",
                'default' : True,
                'searchable' : True,
                # 'validation' : "" - "number" - "data" - "email"
                'validation' : "number"
                },
                {
                'name' : "kootaj",
                'label' : "شماره کوتاژ",
                'default' : True,
                'searchable' : True,
                'validation' : "number"
                },
                {
                'name' : "cert_no",
                'label' : "شماره پروانه گمرکی",
                'default' : True,
                'searchable' : True,
                'validation' : "number"
                },
                {
                'name' : "company",
                'label' : "نام شرکت",
                'default' : True,
                'searchable' : True,
                'validation' : ""
                },




                {
                'name' : "card_no",
                'label' : "شماره کارت",
                'default' : True,
                'searchable' : True,
                'validation' : ""
                },
                {
                'name' : "code_no",
                'label' : "شماره کد",
                'default' : True,
                'searchable' : True,
                'validation' : ""
                },
                {
                'name' : "tariff_no",
                'label' : "شماره تعرفه",
                'default' : True,
                'searchable' : True,
                'validation' : ""
                },
                {
                'name' : "full_name",
                'label' : "نام و نام خانوادگی",
                'default' : True,
                'searchable' : True,
                'validation' : ""
                },
                ]

            user_info = {
                'user_id': '666',
                'name': 'احسان',
                'family': 'شیرزادی'
            }

            # self.write(records)
            self.render('Violation_Table.html',
                        search=search,
                        fields=fields,
                        records=records,
                        FieldList=FieldList,
                        user_info=user_info,
                        permissions=permissions
                        )
        else:
            self.redirect('/login')




    def post(self, *args, **kwargs):
        self.write('No post method allowed')
