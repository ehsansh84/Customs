#################
# URL patterns. #
#################

# Handler imports.

# The patterns.

from controller.BaseController import *
from views.violation import Violation, ViolationSearch
from views.personnel import Personnel
from views.edit_request import Editrequest, EditrequestList, EditRequestEnd
# from views.personnel import *
# from views.files import *
# from views.borrow import *
from views.test import *
from views.general import *

url_patterns = {
    (r'/', IndexHandler),
    (r'/form', FormHandler),
    (r'/Stepform', StepFormHandler),
    (r'/table', TableHandler),
    (r'/404', ErrorHandler),
    (r'/violation', Violation),
    (r'/violation_search', ViolationSearch),
    (r'/int_violation', IntViolationHandler),
    (r'/personnels', Personnel),
    (r'/edit_request', Editrequest),
    (r'/edit_request_end', Editrequest),
    (r'/edit_requests', EditrequestList),

    (r'/logout', Logout),
    (r'/login', LoginHandler),


    (r'/pull', Pull),
    (r'/zzz', Zzz),


    # (r'/404[/]?', PageNotFound),
    # (r'/settings/info/([^/]*)', GetSettingsInfo),
    # (r'/settings/create[/]?', CreateSetting),
    # (r'/settings/edit/([^/]*)', UpdateSettings),
    # (r'/settings/delete/([^/]*)', DeleteSettings),
    # (r'/entry_report[/]?', GetEntryReport),
    # (r'/monitor/grabber/link/live[/]?', ShowLiveLinkGrabber),

    # (r'/files', File),
    # (r'/borrow', Borrow),

    # (r'/get_personnel', GetPersonnel),
    # (r'/get_file', GetFile),



    # (r'/files', IntViolationHandler),
    # (r'/borrow', IntViolationHandler),
}



