from functools import wraps
import time

def generic(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before call:", time.time())
        result = func(*args, **kwargs)
        print("After call:", time.time())
        return result
    return wrapper

@generic
def hi(name):
    print(f"Hi {name}")

hi("TAP")
