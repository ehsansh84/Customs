__author__ = 'ehsan'
from models.detect import Detect as Model


class Detect():
    def __init__(self):
        pass

    @classmethod
    def add(cls, id='', sDate='', mDate='', FileNo='', Kootaj='', CertNo='', sDate1='', sDate2='', Policy1=False,
            Policy2=False, Policy3=False, Policy4=False, Policy5=False, Policy6=False, Policy7=False, Policy8=False,
            Ezharname=0, PersonType=False, FullName='', CardNo='', CodeNo='', Company='', EzFullName='', EzOwner='',
            EzAgent='', EzCardNo='', EzCodeNo='', TrFullName='', TrCodeNo='', TrRegNo='', TrNationality='',
            TrManager='', TrType=False, ItemName='', TariffNo='', Paid=0, Defferent=0, Fine=0, DiffPaid=0,
            ViType1=False, ViType2=False, ViType3=False, ViType4=False, ViType5=False, ViType6=False, ViType7=False,
            ViTypeOther='', StatedTariff=0, StatedValue=0, StatedWeight=0, DeductedTariff=0, DeductedValue=0,
            DeductedWeight=0, Law='', Detector=0, DetectorOther='', Commitment=False, Results='', ReceipNo='',
            Details='', Locked=False, mRecDate='', sRecDate=''):


        if id != '':
            obj = Model.objects(Kootaj=id).first()

        else:
            obj = Model()

        if obj != None:
            obj.sDate = sDate
            obj.mDate=mDate
            obj.FileNo=FileNo
            obj.Kootaj=Kootaj
            obj.CertNo=CertNo
            obj.sDate1=sDate1
            obj.sDate2=sDate2
            obj.Policy1=Policy1
            obj.Policy2=Policy2
            obj.Policy3=Policy3
            obj.Policy4=Policy4
            obj.Policy5=Policy5
            obj.Policy6=Policy6
            obj.Policy7=Policy7
            obj.Policy8=Policy8
            obj.Ezharname=Ezharname
            obj.PersonType=PersonType
            obj.FullName=FullName
            obj.CardNo=CardNo
            obj.CodeNo=CodeNo
            obj.Company=Company
            obj.EzFullName=EzFullName
            obj.EzOwner=EzOwner
            obj.EzAgent=EzAgent
            obj.EzCardNo=EzCardNo
            obj.EzCodeNo=EzCodeNo
            obj.TrFullName=TrFullName
            obj.TrCodeNo=TrCodeNo
            obj.TrRegNo=TrRegNo
            obj.TrNationality=TrNationality
            obj.TrManager=TrManager
            obj.TrType=TrType
            obj.ItemName=ItemName
            obj.TariffNo=TariffNo
            obj.Paid=Paid
            obj.Defferent=Defferent
            obj.Fine=Fine
            obj.DiffPaid=DiffPaid
            obj.ViType1=ViType1
            obj.ViType2=ViType2
            obj.ViType3=ViType3
            obj.ViType4=ViType4
            obj.ViType5=ViType5
            obj.ViType6=ViType6
            obj.ViType7=ViType7
            obj.ViTypeOther=ViTypeOther
            obj.StatedTariff=StatedTariff
            obj.StatedValue=StatedValue
            obj.StatedWeight=StatedWeight
            obj.DeductedTariff=DeductedTariff
            obj.DeductedValue=DeductedValue
            obj.DeductedWeight=DeductedWeight
            obj.Law=Law
            obj.Detector=Detector
            obj.DetectorOther=DetectorOther
            obj.Commitment=Commitment
            obj.Results=Results
            obj.ReceipNo=ReceipNo
            obj.Details=Details
            obj.Locked=Locked
            obj.mRecDate=mRecDate
            obj.sRecDate=sRecDate
            print(Kootaj)
            print(obj.Kootaj)
            obj.save()


    @classmethod
    def exists(cls ,kootaj):
        obj = Model()
        return obj.find({'kootaj': kootaj})

    @classmethod
    def all(cls, _filter=None, page=-1, perpage=15, sort='kootaj', order=1):
        try:
            obj = Model()
            obj.find(_filter=_filter, page=page, perpage=perpage, sort=sort, order=order)

            result = []
            while not obj.eof:
                result.append({'kootaj': obj.kootaj,
                               'desc': obj.desc,
                               '_id': obj.get_id(),
                               })
                obj.next()
            return result
        except Exception, err:
            return err.message

    @classmethod
    def get(cls, _id):
        try:
            obj = Model()
            obj.set_id(_id)
            obj.load()
            result = {'kootaj': obj.kootaj,
                      'desc': obj.desc,
                      '_id': obj.get_id(),
                      }
            return result
        except Exception, err:
            return err.message

    @classmethod
    def delete(cls, _id):
        try:
            obj = Model()
            obj.set_id(_id)
            obj.remove()
            return True
        except Exception, err:
            return err.message
