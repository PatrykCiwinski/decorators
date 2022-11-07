#Python decorator
import time


def delay (function):
    time.sleep(2)
    def wrapper_function():
        function()
    return wrapper_function


@delay
def hello():
    print("hello")
@delay
def bye():
    print("bye")

def nothing_to_say():
    print("....")

#two second delay
hello()
#runs just after hello()
nothing_to_say()
