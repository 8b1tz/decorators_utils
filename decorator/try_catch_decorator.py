def try_catch(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            print("An exception occurred:", error)
    return wrapper


if __name__ == "__main__":
    @try_catch
    def divide(a, b):
        return a / b

    divide(10, 0)
