#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ehsan'

import linecache
import sys
import csv
import re
import json
from datetime import datetime
import dateutil.parser
import time

from bs4 import BeautifulSoup
from dateutil import parser

from shared_connections import SharedConnections


redisInstance = SharedConnections.redisInstance

class Color:
    BLACK = 0
    RED = 1
    LIME = 2
    YELLOW = 3
    BLUE = 4
    PINK = 5
    CYAN = 6
    GRAY = 7


class Tools:
    @classmethod
    def Print(self,text,color):
        print '\033[1;3'+str(color)+'m'+str(text)+'\033[1;m'

    #this method write contents in a list format into a csv file
    @classmethod
    def Log(self,contents,filename):
        #RESULTS = [['apple','cherry','orange','pineapple','strawberry']]
        RESULTS = [contents]
        #resultFile = open("c:\\temp\\output4.csv",'wb')
        resultFile = open(filename,'ab')
        wr = csv.writer(resultFile, dialect='excel')
        wr.writerows(RESULTS)
        resultFile.flush()
        return 0

    #this method write contents in a list format into a csv file
    @classmethod
    def BigLog(self,contents,filename):
        #RESULTS = [['apple','cherry','orange','pineapple','strawberry']]
        RESULTS = contents
        #resultFile = open("c:\\temp\\output4.csv",'wb')
        resultFile = open(filename,'ab')
        wr = csv.writer(resultFile, dialect='excel')
        wr.writerows(RESULTS)
        resultFile.flush()
        return 0

    @classmethod
    def BigLog(self,contents,filename,mode):
        #RESULTS = [['apple','cherry','orange','pineapple','strawberry']]
        RESULTS = contents
        #resultFile = open("c:\\temp\\output4.csv",'wb')
        resultFile = open(filename,mode)
        wr = csv.writer(resultFile, dialect='excel')
        wr.writerows(RESULTS)
        resultFile.flush()
        return 0

    #def __init__(self, name, salary):
    #      self.name = name
    #      self.salary = salary
    #      Employee.empCount += 1

    #this method returns the exception in text format
    @classmethod
    def PrintException(self):
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        return 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)

    #this method returns the exception in list format
    @classmethod
    def PrintExceptionList(self):
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        return [filename, lineno, line.strip(), exc_obj]

    #this method returns the exception in list format
    @classmethod
    def LogErrorToRedis(self, type, link):
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        json_meta = json.dumps({"link": link, "type": type, "filename": filename, "lineNo": lineno, "line": line, "message": str(exc_obj)})
        redisInstance.hset('Errors', datetime.now(), json_meta)
        redisInstance.sadd("ErrorTypes", type)
        #TODO return may be changed
        return [filename, lineno, line.strip(), exc_obj]

    ##this method returns the exception in list format
    #@classmethod
    #def LogErrorToLogServer(self, sub_system, type, detail, severity, tags):
    #    exc_type, exc_obj, tb = sys.exc_info()
    #    f = tb.tb_frame
    #    lineno = tb.tb_lineno
    #    filename = f.f_code.co_filename
    #    linecache.checkcache(filename)
    #    line = linecache.getline(filename, lineno, f.f_globals)
    #    str_filename = filename.replace(settings.SITE_ROOT, "")
    #    json_meta = json.dumps({"detail": detail, "type": type, "file_name": str_filename, "line_no": lineno, "line": line, "message": str(exc_obj), "sub_system": sub_system, "project": "republishan", "severity": severity, "tags": tags})
    #    data = dict(err=json_meta)
    #    vv = requests.post("http://error.360republish.com/insert", data=data)
    #    print vv.content
    #    #TODO return may be changed
    #    return [filename, lineno, line.strip(), exc_obj]

    #this method logs the exception into logFilename
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

    @classmethod
    def Encode(self,text):
        text=BeautifulSoup(text).get_text()
        try:
            l=re.findall(r'&#(.*?);',text)
            for sub in l:
                try :
                    a='&#'+sub+';'
                    bc=int(sub)
                    text = text.replace(a,unichr(bc))
                except :
                    pass
        except:
            text=text
        # tag = False
        # quote = False
        # out = ""
        # for c in text:
        #     if c == '<' and not quote:
        #         tag = True
        #     elif c == '>' and not quote:
        #         tag = False
        #     elif (c == '"' or c == "'") and tag:
        #         quote = not quote
        #     elif not tag:
        #         out = out + c
        return text

    #@classmethod
    #def ProjectFolder(self):
    #    try:
    #        from admin.Viral360 import settings
    #        return settings.SITE_ROOT
    #    except:
    #        self.LogErrorToRedis('', '')

    @classmethod
    def SaveErrorToFile(self,filename):
        error_list = redisInstance.hgetall('Errors')
        Exception_Log = open(filename,'a')
        Exception_Log.write("Link" + ',' + "Type" + ',' + "File Name" + ',' + "Line Number" + ',' + "Line" + ',' + "Message" + '\n')
        for field in error_list:
            dic = json.loads(error_list[field])
            error_column = dic["link"] + ',' + dic["type"] + ',' + dic["filename"] + ',' + str(dic["lineNo"]) + ',' + dic["line"] + ',' + dic["message"] + '\n'
            Exception_Log.write(error_column)
            print error_column

        print "Errors Writen To: " + filename

    @classmethod
    def startTimer(self, name):
        date_start = datetime.now()
        redisInstance.hset("TimerList", name, date_start)
        return date_start

    @classmethod
    def endTimer(self, name):
        if redisInstance.hexists("TimerList", name):
            date_end = datetime.now()
            date_start = parser.parse(redisInstance.hget("TimerList", name))
            redisInstance.hdel("TimerList", name)
            return (date_end - date_start).total_seconds()
        else:
            return -1

    @classmethod
    def incCounter(self, name):
        return redisInstance.hincrby("CounterList", name, 1)

    @classmethod
    def getCounter(self, name, deleteTimer = False):
        if redisInstance.hexists("CounterList", name):
            ret = redisInstance.hget("CounterList", name)
            if deleteTimer:
                redisInstance.hdel("CounterList", name)
            return ret
        else:
            return 0

    @classmethod
    def sendEmail(self, to, subject, message):
        print "Email sent to "+ to+ "\nsubject: "+subject+"\nMessage: "+message


#noinspection PyBroadException
class Tools2:
    def __init__(self):
        pass

    @classmethod
    def encode(cls, text):
        try:
            l = re.findall(r'&#(.*?);', text)
            for sub in l:
                a = '&#' + sub + ';'
                bc = int(sub)
                text = text.replace(a, unichr(bc))
        except:
            text = text
        return text

    @classmethod
    def check_jalali_date(cls, jyear, jmonth, jday):
        if jday > 31:
            return False
        if jmonth > 12:
            return False
        if jday < 1:
            return False
        if jmonth < 1:
            return False
        if jmonth < 12:
            if jmonth > 6:
                if jday > 30:
                    return False
        if jmonth == 12:
            if jyear % 4 != 3:
                if jday > 29:
                    return False
        return True


class DateTimeUtility:
    def __init__(self):
        pass

    @classmethod
    def iso_date_to_timestamp(cls, datetime_in_iso):
        stringdate = json.dumps(datetime_in_iso)
        t = (int(stringdate[1:5]), int(stringdate[6:8]), int(stringdate[9:11]), int(stringdate[12:14]), int(stringdate[15:17]), int(stringdate[18:20]), 0, 0, 0)
        return int(time.mktime(t))

    @classmethod
    def date_to_timestamp(cls, date):
        stringdate = json.dumps(date.isoformat())
        t = (int(stringdate[1:5]), int(stringdate[6:8]), int(stringdate[9:11]), int(stringdate[12:14]), int(stringdate[15:17]), int(stringdate[18:20]), 0, 0, 0)
        return int(time.mktime(t))

    @classmethod
    def iso_date_to_short(cls, datetime_in_iso):
        dt = dateutil.parser.parse(datetime_in_iso)
        return dt.strftime("%d %b-%I:%M%p")
    #
    #@classmethod
    #def format_date_social(cls, date):
    #    week_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    #    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Augest', 'September', 'October', 'November', 'December']
    #    return "%s, %s %s %s %s:%s:%s GMT" % (week_days[date.weekday()],
    #                                          datetime.utcnow().day,
    #                                          month_names[date.month],
    #                                          date.year,
    #                                          date.hour,
    #                                          date.minute,
    #                                          date.second)
