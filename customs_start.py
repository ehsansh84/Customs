# Tornado imports etc..
import tornado
import os
import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from pycket.session import SessionManager
from tornado.options import define, options

# App-specific imports
from urls.BaseUrls import url_patterns


define("port", default=8000, help="run on the given port", type=int)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        url_patterns,debug=True,
        cookie_secret="61oETz3455545gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path= os.path.join(os.path.dirname(__file__), "static"),
        **{
        'pycket': {
            'engine': 'redis',
            'storage': {
                'host': 'localhost',
                'port': 6379,
                'db_sessions': 10,
                'db_notifications': 11,
                'max_connections': 2 ** 31,
                },
            'cookies': {
                'expires_days': 120,
                },
            },
            }

        )


    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()