import time
import functools


def cache(func):
    cache_data = {}
    fastest_duration = float('inf')
    slowest_duration = float('-inf')

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal fastest_duration, slowest_duration

        key = args + tuple(kwargs.items())
        if key not in cache_data:
            start_time = time.time()
            cache_data[key] = func(*args, **kwargs)
            duration = time.time() - start_time

            if duration < fastest_duration:
                fastest_duration = duration
            if duration > slowest_duration:
                slowest_duration = duration

        return cache_data[key]

    def get_fastest_duration():
        return fastest_duration

    def get_slowest_duration():
        return slowest_duration

    wrapper.get_fastest_duration = get_fastest_duration
    wrapper.get_slowest_duration = get_slowest_duration

    return wrapper


if __name__ == '__main__':
    @cache
    def expensive_func(x):
        start_time = time.time()
        time.sleep(2)
        print(f"{expensive_func.__name__} ran in \
              {time.time() - start_time:.2f} secs")
        return x

    print(expensive_func(1))
    print(expensive_func(5))

    print(expensive_func.get_fastest_duration(),
          expensive_func.get_slowest_duration())
