import functools
import pdb


def debugger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        pdb.set_trace()
        return func(*args, **kwargs)
    return wrapper


if __name__ == '__main__':
    @debugger
    def my_function(x, y):
        result = x + y
        return result

    result = my_function(3, 5)
    print("Result:", result)
