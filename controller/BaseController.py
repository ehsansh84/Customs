import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import json
# from classes.error import Error


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
    # session = SessionManager(self)
    # if session.get("LoggedIn","No") != "No" :
    #     session.set('info', {"Ln":"Alavi","Fn":"ali"})
    #     session.set('_id','1233444')
        self.render('index.html')
        # else :
        #     session.set('LoggedIn', {"_id":"12222222","name":"ali"})
        #     self.render('index.html',UN="U Are Not Logged In..")

class Test(tornado.web.RequestHandler):
    def get(self):
        self.render('test_tab.html')

class PageNotFound(tornado.web.RequestHandler):
    def get(self, url):
        self.render('404.html', url=url)

# class GetErrorReport(tornado.web.RequestHandler):
#     def get(self):
#         # self.write('')
#         obj = Error()
#         obj.find(page=0, perpage=20)
#         # self.write(str(obj.record_count))
#         self.render("error_report.html", errors=obj)
#
#     def post(self, *args, **kwargs):
#         # try:
#             query = self.get_argument('query', '{}')
#             page = int(self.get_argument('page', '0'))
#             perpage = int(self.get_argument('perpage', '20'))
#             query = json.loads(query)
#             obj = Error()
#             obj.find(_filter=query, page=page, perpage=perpage)
#             # self.write(str(obj.record_count))
#             self.render("error_report_grid.html", errors=obj,total_pages=111,current_page=20)
