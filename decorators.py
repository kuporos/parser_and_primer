# source
# Write a decorator `count_calls` that counts the number of calls to any function
from functools import wraps

def count_calls(f):
    @wraps(f)
    def wrapper(*args):
        wrapper.call_count +=1
        return f(*args)
    wrapper.call_count = 0

    return wrapper


@count_calls
def add(a, b):
    return a + b


@count_calls
def subtract(a, b):
    return a - b


# Some tests

add(1, 2)
add(3, 4)
add(5, 6)

assert add.call_count == 3

subtract(5, 2)
subtract(4, 1)

assert subtract.call_count == 2
assert add.__name__ != subtract.__name__
