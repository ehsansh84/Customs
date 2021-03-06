import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from controllers.int_violation import Intviolation as Controller
from tools.redis import Redis


class Intviolation(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        acc_type = Redis.get(key='acc_type')
        if acc_type == 'admin':
            permissions = Redis.get(key='permissions', type='list')
            self.render('IntViolation.html', permissions=permissions)
        else:
            # self.write('Data')
            # self.write(acc_type)
            self.redirect('/login')

    def post(self, *args, **kwargs):

        id = self.get_argument('id','')
        kootaj = self.get_argument('kootaj', '')
        cert_no = self.get_argument('cert_no', '')
        s_date = self.get_argument('s_date', '')
        m_date = self.get_argument('m_date', '')
        int_cert_no = self.get_argument('int_cert_no', '')
        radif_marzi = self.get_argument('radif_marzi', '')
        s_entry_date = self.get_argument('s_entry_date', '')
        m_entry_date = self.get_argument('m_entry_date', '')
        karne_tir_no = self.get_argument('karne_tir_no', '')
        ezhar_1 = self.get_argument('ezhar_1', False)
        ezhar_2 = self.get_argument('ezhar_2', False)
        ezhar_3 = self.get_argument('ezhar_3', False)
        ezhar_4 = self.get_argument('ezhar_4', False)
        person_type = self.get_argument('person_type', False)
        full_name = self.get_argument('full_name', '')
        card_no = self.get_argument('card_no', '')
        code_no = self.get_argument('code_no', '')
        dest_address = self.get_argument('dest_address', '')
        good_name = self.get_argument('good_name', '')
        net_weight = self.get_argument('net_weight', '')
        weight = self.get_argument('weight', '')
        input_tariff = self.get_argument('input_tariff', '')
        good_count = self.get_argument('good_count', 0)
        price = self.get_argument('price', 0)
        truck_no = self.get_argument('truck_no', '')
        driver_name = self.get_argument('driver_name', '')
        chasis_no = self.get_argument('chasis_no', '')
        trailer_no = self.get_argument('trailer_no', '')
        iranian_truck = self.get_argument('iranian_truck', False)
        truck_address = self.get_argument('truck_address', '')
        truck_type = self.get_argument('truck_type', 0)
        vi_type_1 = self.get_argument('vi_type_1', False)
        vi_type_2 = self.get_argument('vi_type_2', False)
        vi_type_3 = self.get_argument('vi_type_3', False)
        vi_type_4 = self.get_argument('vi_type_4', False)
        vi_type_5 = self.get_argument('vi_type_5', False)
        vi_type_6 = self.get_argument('vi_type_6', False)
        vi_type_7 = self.get_argument('vi_type_7', False)
        detector = self.get_argument('detector', 0)
        detector_other = self.get_argument('detector_other', '')
        fine_receipt_no = self.get_argument('fine_receipt_no', '')
        fine_price = self.get_argument('fine_price', 0)
        final_result = self.get_argument('final_result', 0)
        details = self.get_argument('details', '')
        m_rec_date = self.get_argument('m_rec_date', '')
        s_rec_date = self.get_argument('s_rec_date', '')
        locked = self.get_argument('locked', False)

        # self.write('kootaj:' + str(kootaj)+'<br>')
        # self.write('cert_no:' + str(cert_no)+'<br>')
        # self.write('s_date:' + str(s_date)+'<br>')
        # self.write('m_date:' + str(m_date)+'<br>')
        # self.write('int_cert_no:' + str(int_cert_no)+'<br>')
        # self.write('radif_marzi:' + str(radif_marzi)+'<br>')
        # self.write('s_entry_date:' + str(s_entry_date)+'<br>')
        # self.write('m_entry_date:' + str(m_entry_date)+'<br>')
        # self.write('karne_tir_no:' + str(karne_tir_no)+'<br>')
        # self.write('ezhar_1:' + str(ezhar_1)+'<br>')
        # self.write('ezhar_2:' + str(ezhar_2)+'<br>')
        # self.write('ezhar_3:' + str(ezhar_3)+'<br>')
        # self.write('ezhar_4:' + str(ezhar_4)+'<br>')
        # self.write('person_type:' + str(person_type)+'<br>')
        # self.write('full_name:' + str(full_name)+'<br>')
        # self.write('card_no:' + str(card_no)+'<br>')
        # self.write('code_no:' + str(code_no)+'<br>')
        # self.write('dest_address:' + str(dest_address)+'<br>')
        # self.write('good_name:' + str(good_name)+'<br>')
        # self.write('net_weight:' + str(net_weight)+'<br>')
        # self.write('weight:' + str(weight)+'<br>')
        # self.write('input_tariff:' + str(input_tariff)+'<br>')
        # self.write('good_count:' + str(good_count)+'<br>')
        # self.write('price:' + str(price)+'<br>')
        # self.write('truck_no:' + str(truck_no)+'<br>')
        # self.write('driver_name:' + str(driver_name)+'<br>')
        # self.write('chasis_no:' + str(chasis_no)+'<br>')
        # self.write('trailer_no:' + str(trailer_no)+'<br>')
        # self.write('iranian_truck:' + str(iranian_truck)+'<br>')
        # self.write('truck_address:' + str(truck_address)+'<br>')
        # self.write('truck_type:' + str(truck_type)+'<br>')
        # self.write('vi_type_1:' + str(vi_type_1)+'<br>')
        # self.write('vi_type_2:' + str(vi_type_2)+'<br>')
        # self.write('vi_type_3:' + str(vi_type_3)+'<br>')
        # self.write('vi_type_4:' + str(vi_type_4)+'<br>')
        # self.write('vi_type_5:' + str(vi_type_5)+'<br>')
        # self.write('vi_type_6:' + str(vi_type_6)+'<br>')
        # self.write('vi_type_7:' + str(vi_type_7)+'<br>')
        # self.write('detector:' + str(detector)+'<br>')
        # self.write('detector_other:' + str(detector_other)+'<br>')
        # self.write('fine_receipt_no:' + str(fine_receipt_no)+'<br>')
        # self.write('fine_price:' + str(fine_price)+'<br>')
        # self.write('final_result:' + str(final_result)+'<br>')
        # self.write('details:' + str(details)+'<br>')
        # self.write('m_rec_date:' + str(m_rec_date)+'<br>')
        # self.write('s_rec_date:' + str(s_rec_date)+'<br>')
        # self.write('locked:' + str(locked)+'<br>')

        Controller.add(id=id, kootaj=kootaj, cert_no=cert_no, s_date=s_date, m_date=m_date, int_cert_no=int_cert_no,
                       radif_marzi=radif_marzi, s_entry_date=s_entry_date, m_entry_date=m_entry_date,
                       karne_tir_no=karne_tir_no, ezhar_1=ezhar_1, ezhar_2=ezhar_2, ezhar_3=ezhar_3, ezhar_4=ezhar_4,
                       person_type=person_type, full_name=full_name, card_no=card_no, code_no=code_no,
                       dest_address=dest_address, good_name=good_name, net_weight=net_weight, weight=weight,
                       input_tariff=input_tariff, good_count=good_count, price=price, truck_no=truck_no,
                       driver_name=driver_name, chasis_no=chasis_no, trailer_no=trailer_no, iranian_truck=iranian_truck,
                       truck_address=truck_address, truck_type=truck_type, vi_type_1=vi_type_1, vi_type_2=vi_type_2,
                       vi_type_3=vi_type_3, vi_type_4=vi_type_4, vi_type_5=vi_type_5, vi_type_6=vi_type_6,
                       vi_type_7=vi_type_7, detector=detector, detector_other=detector_other,
                       fine_receipt_no=fine_receipt_no, fine_price=fine_price, final_result=final_result,
                       details=details, m_rec_date=m_rec_date, s_rec_date=s_rec_date, locked=locked)
        self.write(str(vi_type_4))
        self.write(str(vi_type_3))
        # self.redirect('/int_violation')
