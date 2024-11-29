import copy
import inspect
from jsondiff import diff
from _datetime import datetime
import dill


class Clogger:

    def __init__(self, diff_only):
        self._clogging = []
        self.diff_only = diff_only
        if not self.diff_only:
            self.diff_only = False
        self.last_locals = None
        self.last_globals = None

    def clog(self, comment):
        timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        locals_retval = copy.copy(locals())
        globals_retval = copy.copy(globals())
        retval = {
            'timestamp': timestamp_str,
            'lineno': inspect.currentframe().f_back.f_lineno,
            'comment': comment,
            'locals': locals_retval,
            'globals': globals_retval,
            'co_name': inspect.currentframe().f_back.f_code.co_name
        }
        # use co_name to determine if a frame shift has occurred
        if self.diff_only and len(self._clogging) >= 1:
            retval['globals'] = diff(self.last_globals, globals_retval)
            retval['locals'] = diff(self.last_locals, locals_retval)
        self._clogging.append(retval)
        self.last_globals = globals_retval
        self.last_locals = locals_retval

        return retval

    def get_clogging(self, index):
        return self._clogging[index]

    def get_all_clogging(self):
        return self._clogging

    def save_log(self, fname):
        dill.dump(self._clogging, open(fname, "wb"))

    def load_log(self, fname):
        with open(fname, "rb") as fhandle:
            self._clogging = dill.load(fhandle)

    def purge_log(self):
        self._clogging = []


if __name__ == '__main__':
    a = Clogger(True)
    b = 1
    print(a.clog('testing initial clog'))
    b = 2
    print(a.clog('testing second clog'))
    b = 3
    print(a.clog('testing third clog'))
    a.save_log("myClog.p")
    print('-----------------------')
    for clog_no, clog_val in enumerate(a.get_all_clogging()):
        print(clog_val)
        if clog_no > 0:
            x = a.get_clogging(clog_no - 1)
            y = a.get_clogging(clog_no)
            print(diff(x['globals'], y['globals']))
    print('-----------------------')
    print(a.get_all_clogging())
    a.save_log("myClog.p")
    a.load_log("myClog.p")
    print(a.get_all_clogging())
