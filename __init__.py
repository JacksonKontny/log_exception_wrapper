from functools import wraps
import logging

exception_logger = logging.getLogger()
hdlr = logging.FileHandler('/tmp/exceptions.log')
exception_logger.addHandler(hdlr)

def exception_logging_decorator(func):

    @wraps(func)
    def exception_logged_function(*args, **kwargs):
        try:
            return func()
        except Exception as e:
            exception_logger.exception()

    return exception_logged_function
