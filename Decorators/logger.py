import os
from datetime import datetime
from functools import wraps
from pathlib import Path


def logger(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        date = datetime.now()
        result = old_function(*args, **kwargs)
        with open('logs.txt', 'w') as f:
            f.write(f'{date} {old_function.__name__} {args} {kwargs} {result}')
        return result

    return new_function


def path_file(path_):
    def _logg(old_function):

        @wraps(old_function)
        def new_function(*args, **kwargs):
            date = datetime.now()
            result = old_function(*args, **kwargs)
            with open(path_, 'w') as f:
                f.write(f'{date} {old_function.__name__} {args} {kwargs} {result}')
            return result

        return new_function

    return _logg
