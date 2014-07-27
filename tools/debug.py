__author__ = 'ehsan'

# from pprint import pprint
class Color:
    def __init__(self):
        pass

    BLACK = 0
    RED = 1
    LIME = 2
    YELLOW = 3
    BLUE = 4
    PINK = 5
    CYAN = 6
    GRAY = 7


class Debug:

    def __init__(self):
        pass

    @classmethod
    def cprint(cls, text, color=Color.RED):
        print '\033[1;3' + str(color) + 'm' + str(text) + '\033[1;m'

    @classmethod
    def dprint(cls, text, type='msg'):
        types = {'error': Color.RED, 'data': Color.CYAN, 'msg': Color.PINK, 'custom': Color.LIME}
        print '\033[1;3' + str(types[type]) + 'm' + str(text) + '\033[1;m'
