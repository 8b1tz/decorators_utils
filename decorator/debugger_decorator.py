import functools
import pdb

def debugger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        pdb.set_trace()
        return func(*args, **kwargs)
    return wrapper