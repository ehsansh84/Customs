#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from controllers.violation import Violation as Controller


class Violation(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('Violation.html')

    def post(self, *args, **kwargs):
        id = self.get_argument('id','')

        sDate = self.get_argument('sDate','')
        mDate = self.get_argument('mDate', '')
        FileNo = self.get_argument('FileNo', '')
        Kootaj = self.get_argument('Kootaj', '')
        CertNo = self.get_argument('CertNo', '')
        sDate1 = self.get_argument('sDate1', '')
        sDate2 = self.get_argument('sDate2', '')
        Policy1 = self.get_argument('Policy1', False)
        Policy2 = self.get_argument('Policy2', False)
        Policy3 = self.get_argument('Policy3', False)
        Policy4 = self.get_argument('Policy4', False)
        Policy5 = self.get_argument('Policy5', False)
        Policy6 = self.get_argument('Policy6', False)
        Policy7 = self.get_argument('Policy7', False)
        Policy8 = self.get_argument('Policy8', False)
        Ezharname = self.get_argument('Ezharname', 0)
        PersonType = self.get_argument('PersonType', False)
        FullName = self.get_argument('FullName', '')
        CardNo = self.get_argument('CardNo', '')
        CodeNo = self.get_argument('CodeNo', '')
        Company = self.get_argument('Company', '')
        EzFullName = self.get_argument('EzFullName', '')
        EzOwner = self.get_argument('EzOwner', '')
        EzAgent = self.get_argument('EzAgent', '')
        EzCardNo = self.get_argument('EzCardNo', '')
        EzCodeNo = self.get_argument('EzCodeNo', '')
        TrFullName = self.get_argument('TrFullName', '')
        TrCodeNo = self.get_argument('TrCodeNo', '')
        TrRegNo = self.get_argument('TrRegNo', '')
        TrNationality = self.get_argument('TrNationality', '')
        TrManager = self.get_argument('TrManager', '')
        TrType = self.get_argument('TrType', False)
        ItemName = self.get_argument('ItemName', '')
        TariffNo = self.get_argument('TariffNo', '')
        Paid = self.get_argument('Paid', 0)
        Different = self.get_argument('Different', 0)
        Fine = self.get_argument('Fine', 0)
        DiffPaid = self.get_argument('DiffPaid', 0)
        ViType1 = self.get_argument('ViType1', False)
        ViType2 = self.get_argument('ViType2', False)
        ViType3 = self.get_argument('ViType3', False)
        ViType4 = self.get_argument('ViType4', False)
        ViType5 = self.get_argument('ViType5', False)
        ViType6 = self.get_argument('ViType6', False)
        ViType7 = self.get_argument('ViType7', False)
        ViTypeOther = self.get_argument('ViTypeOther', '')
        StatedTariff = self.get_argument('StatedTariff', 0)
        StatedValue = self.get_argument('StatedValue', 0)
        StatedWeight = self.get_argument('StatedWeight', 0)
        DeductedTariff = self.get_argument('DeductedTariff', 0)
        DeductedValue = self.get_argument('DeductedValue', 0)
        DeductedWeight = self.get_argument('DeductedWeight', 0)
        Law = self.get_argument('Law', '')
        Detector = self.get_argument('Detector', 0)
        DetectorOther = self.get_argument('DetectorOther', '')
        Commitment = self.get_argument('Commitment', False)
        Results = self.get_argument('Results', '')
        ReceipNo = self.get_argument('ReceipNo', '')
        Details = self.get_argument('Details', '')
        Locked = self.get_argument('Locked', False)
        mRecDate = self.get_argument('mRecDate', '')
        sRecDate = self.get_argument('sRecDate', '')

        Controller.add(id=id, s_date=sDate, m_date=mDate, file_no=FileNo, kootaj=Kootaj, cert_no=CertNo, s_date_1=sDate1, s_date_2=sDate2, policy_1=Policy1,
            policy_2=Policy2, policy_3=Policy3, policy_4=Policy4, policy_5=Policy5, policy_6=Policy6, policy_7=Policy7, Policy_8=Policy8,
            ezharname=Ezharname, person_type=PersonType, full_name=FullName, card_no=CardNo, code_no=CodeNo, company=Company, ez_full_name=EzFullName, ez_owner=EzOwner,
            ez_agent=EzAgent, ez_card_no=EzCardNo, ez_code_no=EzCodeNo, tr_full_name=TrFullName, tr_code_no=TrCodeNo, tr_reg_no=TrRegNo, tr_nationality=TrNationality,
            tr_manager=TrManager, tr_type=TrType, item_name=ItemName, tariff_no=TariffNo, paid=Paid, different=Different, fine=Fine, diff_paid=DiffPaid,
            vi_type_1=ViType1, vi_type_2=ViType2, vi_type_3=ViType3, vi_type_4=ViType4, vi_type_5=ViType5, vi_type_6=ViType6, vi_type_7=ViType7,
            vi_type_other=ViTypeOther, stated_tariff=StatedTariff, stated_value=StatedValue, stated_weight=StatedWeight, deducted_tariff=DeductedTariff, deducted_value=DeductedValue,
            deducted_weight=DeductedWeight, law=Law, detector=Detector, detector_other=DetectorOther, commitment=Commitment, results=Results, receip_no=ReceipNo,
            details=Details, locked=Locked, m_rec_date=mRecDate, s_rec_date=sRecDate)
        self.write(sDate)
        self.write(FileNo)
        self.write(Kootaj)
        self.write('Inserted')
#
# class File(tornado.web.RequestHandler):
#
#     def get(self, *args, **kwargs):
#         self.render('file.html')
#
#     def post(self, *args, **kwargs):
#         kootaj =  = self.get_argument('kootaj', '')
#         desc =  = self.get_argument('desc', '')
#         Controller.add(_id='', kootaj=kootaj, desc=desc)
#         self.write(kootaj)
#         self.write(desc)
#
#
# class GetFile(tornado.web.RequestHandler):
#
#     def get(self, *args, **kwargs):
#         self.write('No get method allowed')
#
#     def post(self, *args, **kwargs):
#         kootaj =  = self.get_argument('kootaj', '')
#
#         if Controller.all(_filter={'kootaj': kootaj}):
#             shape = {
#                 'explain': 'OK EHSAN',
#             }
#         else:
#             shape = {
#                 'explain': 'NO EHSAN',
#             }
#         # if id dont existed , return -2
#         output_result = json.dumps(shape)
#         self.write(output_result)
#         # return -2
