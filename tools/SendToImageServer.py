#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Hassan'

import datetime

from ErrorHandler import ErrorHandler
from shared_connections import SharedConnections



#noinspection PyBroadException
def send_to_image_server(entry_id=0, pub_date=None, image_url='', watermark='', link=''):
    try:
        tbl_images = SharedConnections.MonitoringDB.images
        try:
            date = pub_date.date().__str__()
        except:
            date = datetime.datetime.utcnow().date().__str__()
        tbl_images.insert({'date': date, 'uid': str(entry_id), 'link': str(image_url), 'watermark': watermark})
        return True

        #j = {'date': date, 'uid': str(entry_id), 'link': str(image_url), 'watermark': watermark}
        #l = [j]
        #json_meta = json.dumps(l)
        #data = dict(images=json_meta)
        #result = requests.post(SharedConnections.BackendImageServer, data=data)
        #if result.content == 'ok':
        #    return True
        #else:
        #    return False
    except:
        try:
            ErrorHandler.log_to_error_server(subSystem='LinkGrabber', section='SendToImageServer', severity='Error',
                                             data=link)
        except:
            pass
        return False