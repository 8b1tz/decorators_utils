def count_decorator(func):
    count = 0

    def wrapper():
        nonlocal count
        count += 1
        func()

    def get_count():
        return count
    wrapper.get_count = get_count
    return wrapper


if __name__ == '__main__':
    @count_decorator
    def test():
        return 1 + 1

    test()
    test()
    print(test.get_count())
    test()
    test()
    print(test.get_count())
    test()
    print(test.get_count())
