# This is a sample Python script.
import copy
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import inspect
from jsondiff import diff

class clogger:

    def __init__(self):
        self.clogging = []

    def clog(self, comment):
        retval = {'lineno': inspect.currentframe().f_back.f_lineno,
                  'comment': comment,
                  'locals': copy.copy(locals()),
                  'globals': copy.copy(globals())
                  }
        self.clogging.append(retval)
        return retval

    def getclogging(self):
        return self.clogging
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = clogger()
    b = 1
    print(a.clog('testing initial clog'))
    b = 2
    print(a.clog('testing second clog'))
    b = 3
    print(a.clog('testing third clog'))
    print('-----------------------')
    for clog_no, clog_val in enumerate(a.clogging):
        print(clog_val)
        if clog_no > 0:
            print(diff(a.clogging[clog_no-1]['globals'], a.clogging[clog_no]['globals']))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
