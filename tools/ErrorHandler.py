#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ehsan'

import linecache
import sys
import csv
import os

import requests

from shared_connections import SharedConnections


class Color:
    BLACK = 0
    RED = 1
    LIME = 2
    YELLOW = 3
    BLUE = 4
    PINK = 5
    CYAN = 6
    GRAY = 7

#noinspection PyBroadException


class ErrorHandler():
    def __init__(self):
        pass

    @classmethod
    def Print(self,text,color):
        print '\033[1;3'+str(color)+'m'+str(text)+'\033[1;m'

    #this method write contents in a list format into a csv file
    @classmethod
    def Log(self,contents,filename):
        RESULTS = [contents]
        resultFile = open(filename,'ab')
        wr = csv.writer(resultFile, dialect='excel')
        wr.writerows(RESULTS)
        resultFile.flush()
        return 0

    @classmethod
    def log_to_error_server(cls, subSystem, section, severity, data):
        try:
            exc_type, exc_obj, tb = sys.exc_info()
            f = tb.tb_frame
            lineno = tb.tb_lineno
            filename = f.f_code.co_filename
            linecache.checkcache(filename)
            line = linecache.getline(filename, lineno, f.f_globals)

            error_data = dict(project='Republishan', subSystem=subSystem, section=section, severity=severity,
                              filename=os.path.basename(filename),filepath=filename, lineno=lineno, code=line.strip(), messages=str(exc_obj), data=data)
            result = requests.post(SharedConnections.ErrorReportingServerDomain + '/CreateError', data=error_data)
            return True
        except:
            try:
                #error_data = dict(project='Republishan', subSystem=subSystem, section=section, severity=severity, data=data)
                #result = requests.post(SharedConnections.ErrorReportingServerDomain + '/CreateError', data=error_data)
                #return True
                pass
            except:
                print False

    @classmethod
    def PrintException(self):
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        return 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)

    @classmethod
    def LogException(self,logFilename):
        try:
            log = []
            exc_type, exc_obj, tb = sys.exc_info()
            f = tb.tb_frame
            lineno = tb.tb_lineno
            filename = f.f_code.co_filename
            linecache.checkcache(filename)
            line = linecache.getline(filename, lineno, f.f_globals)
            log.append(filename)
            log.append(str(lineno))
            log.append(line.strip())
            log.append("'"+str(exc_obj)+"'")
            self.Print(log,Color.CYAN)
            resultFile = open(logFilename,'ab')
            #print logFilename
            wr = csv.writer(resultFile, dialect='excel')
            wr.writerows([log])
            resultFile.flush()
        except:
            self.Print(self.PrintException(),Color.RED)
            self.Print(filename,Color.LIME)
            self.Print(lineno,Color.LIME)
            self.Print(line.strip(),Color.LIME)
            self.Print(exc_obj,Color.LIME)

        return 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)