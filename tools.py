#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Hassan'

import re


#noinspection PyBroadException
class Tools:
    def __init__(self):
        pass

    @classmethod
    def encode(cls, text):
        try:
            l = re.findall(r'&#(.*?);', text)
            for sub in l:
                a = '&#'+sub+';'
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