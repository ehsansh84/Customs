#################
# URL patterns. #
#################

# Handler imports.

# The patterns.

from controller.BaseController import *
from views.personnel import *
from views.files import *
from views.borrow import *


url_patterns = {
    (r'/', IndexHandler),
    # (r'/form', FormHandler),
    # (r'/Stepform', StepFormHandler),
    # (r'/table', TableHandler),
    # (r'/404', ErrorHandler),
    # (r'/login', LoginHandler),
    # (r'/violation', ViolationHandler),
    # (r'/intViolation', IntViolationHandler),


    # (r'/404[/]?', PageNotFound),
    # (r'/settings/info/([^/]*)', GetSettingsInfo),
    # (r'/settings/create[/]?', CreateSetting),
    # (r'/settings/edit/([^/]*)', UpdateSettings),
    # (r'/settings/delete/([^/]*)', DeleteSettings),
    # (r'/entry_report[/]?', GetEntryReport),
    # (r'/monitor/grabber/link/live[/]?', ShowLiveLinkGrabber),


    # (r'/personnels', Personnel),
    # (r'/files', File),
    # (r'/borrow', Borrow),

    # (r'/get_personnel', GetPersonnel),
    # (r'/get_file', GetFile),



    # (r'/files', IntViolationHandler),
    # (r'/borrow', IntViolationHandler),
}



