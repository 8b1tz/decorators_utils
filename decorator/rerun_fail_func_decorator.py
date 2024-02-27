import time


def retry(max_attempts=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f'Attempt {attempt} failed:', str(e))
                    if attempt < max_attempts:
                        print(f'Retrying in {delay} seconds...')
                        time.sleep(delay)
            else:
                print(f'Function {func.__name__} failed after {max_attempts} \
                      attempts.')

        return wrapper
    return decorator


if __name__ == "__main__":
    @retry(max_attempts=3, delay=1)
    def teste():
        1/0

    print(teste())
