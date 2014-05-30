import linecache
import sys
from classes.error import Error
from datetime import datetime

__author__ = 'ehsan'

def PrintException():
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        error = Error(date=datetime.utcnow(), project='Republishan', subSystem='Test system', section='Test section',
                      severity=1, filename=filename, lineno=lineno, code=line.strip(), messages=str(exc_obj), data='No data')
        error.create()
        return 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)

try:
    a = 10
    b = 0
    print a / b
except:
    print 'shit'
    print PrintException()
