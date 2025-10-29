import logging

# Configure logging to show INFO messages
logging.basicConfig(level=logging.INFO, format='%(message)s')

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b
my_function(4,5)



def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")

    return mfx


@greet
def hello():
    print("Hello world")


@greet
def add(a, b):
    print(a + b)


# greet(hello)()
hello()
# greet(add)(1, 2)
add(1, 2)
