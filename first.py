#decorator
from functools import wraps
def logged(func):
    @wraps(func)
    def inner_function(*args, **kwargs):
        print ("You called ",inner_function.__name__,end="")
        print (args,kwargs)
        returnvalue=func(*args, **kwargs)
        return returnvalue
    return inner_function

@logged
def funct(*args):
    return 3 + len(args)

p=funct(4, 4, 4)
print ("It returned", p)
