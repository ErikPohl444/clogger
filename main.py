# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import inspect

class clogger:

    def clog(self):
        retval = {'lineno': inspect.currentframe().f_back.f_lineno,
                  'locals': locals(),
                  'globals': globals()
                  }

        return retval

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = clogger()
    print(a.clog())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
