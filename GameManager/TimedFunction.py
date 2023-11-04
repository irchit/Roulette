import threading

from Errors.TimeoutException import TimeoutException


def timeout_handler(self):
    raise TimeoutException("Function call timed out")


class TimedFunction:

    def __init__(self, function_name, time=1, args=None):
        self.__func = function_name
        self.__time = time
        self.__args = args

    def run(self):
        timer = threading.Timer(self.__time, timeout_handler)
        timer.start()
        try:
            if self.__args is not None:
                result = self.__func(self.__args)
            else:
                result = self.__func()
        except TimeoutException as ex:
            print("Function call timed out")
            result = None
        finally:
            timer.cancel()
        return result

