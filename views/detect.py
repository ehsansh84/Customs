#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'ehsan'
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from controllers.detect import Detect as Controller


class Detect(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('violation.html')

    def post(self, *args, **kwargs):
        sDate = self.get_argument('sDate', '')
        mDate = self.get_argument('mDate', '')
        FileNo = self.get_argument('FileNo', '')
        Kootaj = self.get_argument('Kootaj', '')
        CertNo = self.get_argument('CertNo', '')
        sDate1 = self.get_argument('sDate1', '')
        sDate2 = self.get_argument('sDate2', '')
        Policy1 = self.get_argument('Policy1', '')
        Policy2 = self.get_argument('Policy2', '')
        Policy3 = self.get_argument('Policy3', '')
        Policy4 = self.get_argument('Policy4', '')
        Policy5 = self.get_argument('Policy5', '')
        Policy6 = self.get_argument('Policy6', '')
        Policy7 = self.get_argument('Policy7', '')
        Policy8 = self.get_argument('Policy8', '')
        Ezharname = self.get_argument('Ezharname', '')
        PersonType = self.get_argument('PersonType', '')
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
        TrType = self.get_argument('TrType', '')
        ItemName = self.get_argument('ItemName', '')
        TariffNo = self.get_argument('TariffNo', '')
        Paid = self.get_argument('Paid', '')
        Different = self.get_argument('Different', '')
        Fine = self.get_argument('Fine', '')
        DiffPaid = self.get_argument('DiffPaid', '')
        ViType1 = self.get_argument('ViType1', '')
        ViType2 = self.get_argument('ViType2', '')
        ViType3 = self.get_argument('ViType3', '')
        ViType4 = self.get_argument('ViType4', '')
        ViType5 = self.get_argument('ViType5', '')
        ViType6 = self.get_argument('ViType6', '')
        ViType7 = self.get_argument('ViType7', '')
        ViTypeOther = self.get_argument('ViTypeOther', '')
        StatedTariff = self.get_argument('StatedTariff', '')
        StatedValue = self.get_argument('StatedValue', '')
        StatedWeight = self.get_argument('StatedWeight', '')
        DeductedTariff = self.get_argument('DeductedTariff', '')
        DeductedValue = self.get_argument('DeductedValue', '')
        DeductedWeight = self.get_argument('DeductedWeight', '')
        Law = self.get_argument('Law', '')
        Detector = self.get_argument('Detector', '')
        DetectorOther = self.get_argument('DetectorOther', '')
        Commitment = self.get_argument('Commitment', '')
        Results = self.get_argument('Results', '')
        ReceipNo = self.get_argument('ReceipNo', '')
        Details = self.get_argument('Details', '')
        Locked = self.get_argument('Locked', '')
        mRecDate = self.get_argument('mRecDate', '')
        sRecDate = self.get_argument('sRecDate', '')
        try:
            Controller.add(id='', sDate = sDate, mDate=mDate, FileNo=FileNo, Kootaj=Kootaj, CertNo=CertNo, sDate1=sDate1,
                           sDate2=sDate2, Policy1=Policy1, Policy2=Policy2, Policy3=Policy3, Policy4=Policy4,
                           Policy5=Policy5, Policy6=Policy6, Policy7=Policy7, Policy8=Policy8, Ezharname=Ezharname,
                           PersonType=PersonType, FullName=FullName, CardNo=CardNo, CodeNo=CodeNo, Company=Company,
                           EzFullName=EzFullName, EzOwner=EzOwner, EzAgent=EzAgent, EzCardNo=EzCardNo, EzCodeNo=EzCodeNo,
                           TrFullName=TrFullName, TrCodeNo=TrCodeNo, TrRegNo=TrRegNo, TrNationality=TrNationality,
                           TrManager=TrManager, TrType=TrType, ItemName=ItemName, TariffNo=TariffNo, Paid=Paid,
                           Different=Different, Fine=Fine, DiffPaid=DiffPaid, ViType1=ViType1, ViType2=ViType2,
                           ViType3=ViType3, ViType4=ViType4, ViType5=ViType5, ViType6=ViType6, ViType7=ViType7,
                           ViTypeOther=ViTypeOther, StatedTariff=StatedTariff, StatedValue=StatedValue,
                           StatedWeight=StatedWeight, DeductedTariff=DeductedTariff, DeductedValue=DeductedValue,
                           DeductedWeight=DeductedWeight, Law=Law, Detector=Detector, DetectorOther=DetectorOther,
                           Commitment=Commitment, Results=Results, ReceipNo=ReceipNo, Details=Details, Locked=Locked,
                           mRecDate=mRecDate, sRecDate=sRecDate)
        except Exception, ex:
            return ex.message
        return 1

