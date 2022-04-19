# ? https://sureshdsk.dev/python-decorator-to-measure-execution-time
# ? https://dev.to/po5i/python-decorator-to-measure-function-s-execution-time-4d26
# ? https://medium.com/pythonhive/python-decorator-to-measure-the-execution-time-of-methods-fa04cb6bb36d
# ? https://stackoverflow.com/a/62522469/16377463
from functools import wraps
import time

"""helper function to estimate view execution time"""
def timer(func):
    @wraps(func)    # used for copying func metadata
    def wrapper(*args, **kwargs):
        # record start time
        start_time = time.perf_counter()
        # func execution
        result = func(*args, **kwargs)
        # record start time
        end_time = time.perf_counter()
        # Calculate time taken in secs
        ## total_time = end_time - start_time
        # Calculating time taken in ms
        total_time = (end_time - start_time) * 1000
        # output execution time to console
        if len(str(round(total_time))) >= 4:
            total_time /= 1000
            print('\n\n ##### Function {}{} {} took {:.4f} secs ##### \n\n'.format(func.__name__, args, kwargs, total_time))    # first item in the args, ie `args[0]` is `self`
        else:
            print('\n\n ##### Function {}{} {} took {:.2f} ms ##### \n\n'.format(func.__name__, args, kwargs, total_time))
        return result
    return wrapper

# Usage :-
# from custom_decorator import timer
# @timer
# def your_function(request):
    # pass