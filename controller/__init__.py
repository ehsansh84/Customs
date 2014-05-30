from bson import ObjectId
from pycket.session import SessionManager
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from pymongo import MongoClient

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        client = MongoClient()
        session = SessionManager(self)

        id_doctor = session.get('id')


        if(id_doctor != None):
            fname_doctor = session.get('fname')
            lname_doctor = session.get('lname')
            speciality_doctor = session.get('speciality')
            if session.get('photoprofile') == "":
                photoprofile="2014/profile.jpg"
            else:
                photoprofile=session.get('photoprofile')

            list_speciality_doctor =  client.Doctor.Adminsetting.find_one({"_id": ObjectId("52c3efcf0be04b1d84d48abb")},{"specialty": 1})
            list_speciality_doctor = list_speciality_doctor["specialty"]

            find_coounters = client.Doctor.Expert.find_one({"_id": id_doctor},{"percentcompleteprofile":1})
            find_coounters =find_coounters["percentcompleteprofile"]



            self.render('base/doctor/edit_prof/index.html', fname_doctor = fname_doctor,lname_doctor=lname_doctor,speciality_doctor=speciality_doctor,list_speciality_doctor=list_speciality_doctor , find_coounters = find_coounters,photoprofile=photoprofile)
        else:
            self.redirect('/Doctor/DoctorLogin')



class PoemPageHandler(tornado.web.RequestHandler):

    def post(self):

        c = MongoClient()
        c.words.test.insert({"noun1":self.get_argument('noun1'),"noun2": self.get_argument('noun2'),"verb" : self.get_argument('verb'),"noun3" : self.get_argument('noun3')})
        # self.application.db.words.insert({"noun1":self.get_argument('noun1'),"noun2": self.get_argument('noun2'),"verb" : self.get_argument('verb'),"noun3" : self.get_argument('noun3')})
        self.render('base/doctor/edit_prof/index.html')

class ShowHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('base/doctor/edit_prof/show.html')