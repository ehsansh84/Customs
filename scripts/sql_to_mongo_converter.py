#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'ehsan'
import json
from models.violation import Violation
obj = Violation()
for i in range(21):
    # print i
    with open('records/path'+str(i)+'.txt', 'r') as fobj:
    # with open('d:/records/path'+str(i)+'.txt', 'r') as fobj:
        data = json.load(fobj)
    obj = Violation()
    # print data['sDate'],
    # print data['Kootaj'],
    # print data['CertNo']
    # print obj.s_date,
    # print obj.kootaj,
    # print obj.cert_no
    obj.s_date = data['sDate']
    obj.file_no = data['FileNo']
    obj.kootaj = data['Kootaj']
    obj.cert_no = data['CertNo']
    obj.sDate1 = data['sDate1']
    obj.s_date_2 = data['sDate2']
    obj.policy_1 = data['Policy1']
    obj.policy_2 = data['Policy2']
    obj.policy_3 = data['Policy3']
    obj.policy_4 = data['Policy4']
    obj.policy_5 = data['Policy5']
    obj.policy_6 = data['Policy6']
    obj.policy_7 = data['Policy7']
    # obj.Policy8 = data['Policy8']
    obj.ezharname = data['Ezharname']
    obj.person_type = data['PersonType']
    obj.full_name = data['FullName']
    obj.card_no = data['CardNo']
    obj.code_no = data['CodeNo']
    obj.company = data['Company']
    obj.ez_full_name = data['EzFullName']
    obj.ez_owner = data['EzOwner']
    obj.ez_agent = data['EzAgent']
    obj.ez_card_no = data['EzCardNo']
    obj.ez_code_no = data['EzCodeNo']
    obj.tr_full_name = data['TrFullName']
    obj.tr_code_no = data['TrCodeNo']
    obj.tr_reg_no = data['TrRegNo']
    obj.tr_nationality = data['TrNationality']
    obj.tr_manager = data['TrManager']
    obj.tr_type = data['TrType']
    obj.item_name = data['ItemName']
    obj.tariff_no = data['TariffNo']
    obj.paid = data['Paid']
    obj.different = data['Defferent']
    obj.fine = data['Fine']
    obj.locked = data['Locked']
    obj.details = data['Details']
    obj.receip_no = data['ReceipNo']
    obj.results = data['Results']
    obj.commitment = data['Commitment']
    obj.detector_other = data['DetectorOther']
    obj.law = data['Law']
    obj.deducted_value = data['DeductedValue']
    obj.deducted_tariff = data['DeductedTariff']
    obj.stated_value = data['StatedValue']
    obj.stated_tariff = data['StatedTariff']
    obj.vi_type_other = data['ViTypeOther']
    obj.vi_type_1 = data['ViType1']
    obj.vi_type_2 = data['ViType2']
    obj.vi_type_3 = data['ViType3']
    obj.vi_type_4 = data['ViType4']
    obj.vi_type_5 = data['ViType5']
    obj.vi_type_6 = data['ViType6']
    obj.vi_type_7 = data['ViType7']

    obj.Detector = data['Detector']
    obj.StatedWeight = data['StatedWeight']
    obj.DeductedWeight = data['DeductedWeight']
    obj.DiffPaid = data['DiffPaid']
    obj.Ezharname = data['Ezharname']
    obj.save()