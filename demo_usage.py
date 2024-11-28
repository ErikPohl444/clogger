from Clogger import Clogger
from jsondiff import diff

__author__ = "Erik Pohl"
__copyright__ = "None"
__credits__ = ["Erik Pohl"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Erik Pohl"
__email__ = "erik.pohl.444@gmail.com"
__status__ = "Beta"

if __name__ == '__main__':
    a = Clogger(True)
    b = 1
    print(a.clog('testing initial clog'))
    b = 2
    print(a.clog('testing second clog'))
    b = 3
    print(a.clog('testing third clog'))
    print('-----------------------')
    for clog_no, clog_val in enumerate(a.get_all_clogging()):
        print(clog_val)
        if clog_no > 0:
            x = a.get_clogging(clog_no - 1)
            y = a.get_clogging(clog_no)
            print(diff(x['locals'], y['locals']))
    print('-----------------------')
    #print(a.get_all_clogging())
