import time
from functools import wraps


def delay(seconds):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Sleeping for {seconds} seconds before running \
                  {func.__name__}")
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return inner


def create_delay_decorator(param):
    return delay(seconds=param)


decorator = create_delay_decorator(param=int(input("Delay time: ")))


if __name__ == '__main__':
    @decorator
    def print_text():
        print("Hello World")
    print_text()
