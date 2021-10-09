from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before
        result = func(*args, **kwargs)
        # Do Something after
        return result
    return wrapper


@decorator
def func():
    pass
