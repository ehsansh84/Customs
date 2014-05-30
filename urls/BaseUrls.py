#################
# URL patterns. #
#################

# Handler imports.

# The patterns.

from controller.BaseController import *
from controller.error import CreateError,GetErrors,RemoveErrors
from controller.BaseController import PageNotFound



url_patterns = {
    (r'/', IndexHandler),
    (r'/error_query[/]?', GetErrorReport),
    (r'/([^/]*)', PageNotFound),
}

