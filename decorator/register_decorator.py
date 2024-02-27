import functools
import logging


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(func.__name__)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s \
                                      - %(message)s')
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        logger.info("Function {} is being called...".format(func.__name__))
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            logger.critical("Function {} raised an exception! {}"
                            .format(func.__name__, e))
        logger.info("Function {} completed.".format(func.__name__))
        return result
    return wrapper


if __name__ == "__main__":
    @log
    def sum(a, b):
        return a + 'a'

    print(sum(2, 3))
