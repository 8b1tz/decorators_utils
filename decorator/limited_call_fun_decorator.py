def limited_call(limit):
    def decorator(func):
        execution_count = 0

        def wrapper(*args, **kwargs):
            nonlocal execution_count
            if execution_count == limit:
                raise Exception("Reached the call limit")
            execution_count += 1
            print(f"The function '{func.__name__}' has been called \
                  {execution_count} times")
            return func(*args, **kwargs)
        return wrapper
    return decorator


if __name__ == "__main__":
    @limited_call(limit=3)
    def test():
        print('hi')

    test()
    test()
    test()
    test()
