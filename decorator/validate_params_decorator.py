def validate_input_integer(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int) or arg <= 0:
                raise ValueError("Arguments must be positive integers")

        for value in kwargs.values():
            if not isinstance(value, int) or value <= 0:
                raise ValueError("Keyword arguments must be positive integers")

        return func(*args, **kwargs)

    return wrapper


if __name__ == "__main__":
    @validate_input_integer
    def calculate_sum(a, b):
        return a + b

    result = calculate_sum(5, 10)
    print("Sum result:", result)
