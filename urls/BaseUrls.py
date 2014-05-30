#################
# URL patterns. #
#################

# Handler imports.

# The patterns.

from controller.BaseController import *
# from controller.error import CreateError,GetErrors,RemoveErrors
from controller.BaseController import PageNotFound
from controller.Violation import *
from controller.IntViolation import *


url_patterns = {
    (r'/', IndexHandler),
    # (r'/error_query[/]?', GetErrorReport),
    (r'/violation[/]?', GetViolation),
    (r'/int_violation[/]?', GetIntviolation),
    (r'/test[/]?', Test),
    # (r'/([^/]*)', PageNotFound),
}

