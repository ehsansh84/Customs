import os
import os.path
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options
from tornado.options import define, options
from urls.BaseUrls import url_patterns


# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hi Ehsan, Welcome to Tornado Web Framework.")

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        url_patterns,debug=True,
        cookie_secret="61oETz3455545gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
        xsrf_cookies= False,
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path= os.path.join(os.path.dirname(__file__), "static"),

        **{
                'pycket': {
                    'engine': 'redis',
                    'storage': {
                        'db_sessions': 10,
                        'db_notifications': 11,
                        'max_connections': 2 ** 31,
                        },
                    'cookies': {
                        'expires_days': 120,
                        # 'domain' : SharedConnections.SiteNameUrl[SharedConnections.SiteNameUrl.index(".")+1,-1],
                        'domain' : '360viral.com',

                        },
                    },
                }
    )

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(22111)
    tornado.ioloop.IOLoop.instance().start()