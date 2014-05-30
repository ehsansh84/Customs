
__author__ = 'No author'
import json

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.options
import tornado.websocket
from classes.Violation import Violation

class GetViolation(tornado.web.RequestHandler):
    def get(self):
        obj = Violation()
        obj.find()
        self.render("Violation.html", Violation=obj.get_all_json(False))

    def post(self, *args, **kwargs):
        try:
            action = self.get_argument('action', '')
            _id = self.get_argument('id', '')
            s_date = self.get_argument('s_date','')
            m_date = self.get_argument('m_date','')
            fileNo = self.get_argument('fileNo','')
            kootaj = self.get_argument('kootaj','')
            cert_no = self.get_argument('cert_no','')
            s_date_1 = self.get_argument('s_date_1','')
            s_date_2 = self.get_argument('s_date_2','')
            policy_1 = self.get_argument('policy_1','')
            policy_2 = self.get_argument('policy_2','')
            policy_3 = self.get_argument('policy_3','')
            policy_4 = self.get_argument('policy_4','')
            policy_5 = self.get_argument('policy_5','')
            policy_6 = self.get_argument('policy_6','')
            policy_7 = self.get_argument('policy_7','')
            policy_8 = self.get_argument('policy_8','')
            ezharname = self.get_argument('ezharname','')
            person_type = self.get_argument('person_type','')
            full_name = self.get_argument('full_name','')
            card_no = self.get_argument('card_no','')
            code_no = self.get_argument('code_no','')
            company = self.get_argument('company','')
            ez_full_name = self.get_argument('ez_full_name','')
            ez_owner = self.get_argument('ez_owner','')
            ez_agent = self.get_argument('ez_agent','')
            ez_card_no = self.get_argument('ez_card_no','')
            ez_code_no = self.get_argument('ez_code_no','')
            tr_full_name = self.get_argument('tr_full_name','')
            tr_code_no = self.get_argument('tr_code_no','')
            tr_reg_no = self.get_argument('tr_reg_no','')
            tr_nationality = self.get_argument('tr_nationality','')
            tr_manager = self.get_argument('tr_manager','')
            tr_type = self.get_argument('tr_type','')
            item_name = self.get_argument('item_name','')
            tariff_no = self.get_argument('tariff_no','')
            paid = self.get_argument('paid','')
            different = self.get_argument('different','')
            fine = self.get_argument('fine','')
            diff_paid = self.get_argument('diff_paid','')
            vi_type_1 = self.get_argument('vi_type_1','')
            vi_type_2 = self.get_argument('vi_type_2','')
            vi_type_3 = self.get_argument('vi_type_3','')
            vi_type_4 = self.get_argument('vi_type_4','')
            vi_type_5 = self.get_argument('vi_type_5','')
            vi_type_6 = self.get_argument('vi_type_6','')
            vi_type_7 = self.get_argument('vi_type_7','')
            vi_type_other = self.get_argument('vi_type_other','')
            stated_tariff = self.get_argument('stated_tariff','')
            stated_value = self.get_argument('stated_value','')
            stated_weight = self.get_argument('stated_weight','')
            deducted_tariff = self.get_argument('deducted_tariff','')
            deducted_value = self.get_argument('deducted_value','')
            deducted_weight = self.get_argument('deducted_weight','')
            law = self.get_argument('law','')
            detector = self.get_argument('detector','')
            detector_other = self.get_argument('detector_other','')
            results = self.get_argument('results','')
            commitment = self.get_argument('commitment','')
            receip_no = self.get_argument('receip_no','')
            details = self.get_argument('details','')
            m_rec_date = self.get_argument('m_rec_date','')
            s_rec_date = self.get_argument('s_rec_date','')
            locked = self.get_argument('locked','')


            obj = Violation(s_date=s_date, m_date=m_date, fileNo=fileNo, kootaj=kootaj, cert_no=cert_no, s_date_1=s_date_1, s_date_2=s_date_2, policy_1=policy_1, policy_2=policy_2, policy_3=policy_3, policy_4=policy_4, policy_5=policy_5, policy_6=policy_6, policy_7=policy_7, policy_8=policy_8, ezharname=ezharname, person_type=person_type, full_name=full_name, card_no=card_no, code_no=code_no, company=company, ez_full_name=ez_full_name, ez_owner=ez_owner, ez_agent=ez_agent, ez_card_no=ez_card_no, ez_code_no=ez_code_no, tr_full_name=tr_full_name, tr_code_no=tr_code_no, tr_reg_no=tr_reg_no, tr_nationality=tr_nationality, tr_manager=tr_manager, tr_type=tr_type, item_name=item_name, tariff_no=tariff_no, paid=paid, different=different, fine=fine, diff_paid=diff_paid, vi_type_1=vi_type_1, vi_type_2=vi_type_2, vi_type_3=vi_type_3, vi_type_4=vi_type_4, vi_type_5=vi_type_5, vi_type_6=vi_type_6, vi_type_7=vi_type_7, vi_type_other=vi_type_other, stated_tariff=stated_tariff, stated_value=stated_value, stated_weight=stated_weight, deducted_tariff=deducted_tariff, deducted_value=deducted_value, deducted_weight=deducted_weight, law=law, detector=detector, detector_other=detector_other, results=results, commitment=commitment, receip_no=receip_no, details=details, m_rec_date=m_rec_date, s_rec_date=s_rec_date, locked=locked,)
            obj.set_id(_id)

            full_data = {}
            if action in ['add', 'edit']:
                ret = str(obj.get_id) if obj.create() else 'error'
                obj.load()
                full_data = obj.get_json(False)
            elif action == 'delete':
                ret = _id if obj.remove() else 'error'
            elif action == 'info':
                ret = 'error'
                if obj.load():
                    full_data = obj.get_json(False)
                    ret = str(obj.get_id)
            else:
                ret = 'error'

            dic = {
                'action': action,
                'ret': str(ret),
                'full_data': full_data
            }
            self.write(json.dumps(dic))
        except Exception, err:
            dic = {
                'action': 'error',
                'ret': err.message,
                'full_data': {}
            }
            self.write(json.dumps(dic))
