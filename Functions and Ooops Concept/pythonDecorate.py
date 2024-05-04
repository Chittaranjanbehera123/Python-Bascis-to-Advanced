# Python Decorators:
# Python decorators are a powerful and versatile tool that allow you to modify the behavior and methods .
# A decorator is a function that takes another function as an argument and return anew function that modifies the behavior of the orginal function.

# Example1:
def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello World")
 
@greet   
def add(a, b):
    print(a+b)
    
hello()
add(1 ,2)

# Example2:
import logging  # Note: 'Logging' should be 'logging' for the module name to be correct

def Log_function_call(fx):
    def decorated(*args, **kwargs):
        logging.info(f"calling {fx.__name__} with args = {args}, kwargs = {kwargs}")
        result = fx(*args, **kwargs)
        logging.info(f"{fx.__name__} returned {result}")
        return result  # Moved this line to the correct indentation level

    return decorated

@Log_function_call
def my_function_call(a, b):
    return a + b

# Example3:
def my_decorator(fx):
    def mfx(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = fx(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return mfx

# Apply the decorator to a function
@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

@my_decorator
def add_numbers(a, b):
    return a + b

# Use the decorated functions
say_hello("John")
result = add_numbers(5, 7)
print(f"Result: {result}")

# Example4:
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@logging_decorator
def add_numbers(a, b):
    return a + b

@logging_decorator
def multiply_numbers(a, b):
    return a * b

class MathOperations:
    @logging_decorator
    def power(self, base, exponent):
        return base ** exponent

# Use the decorated functions and methods
result_add = add_numbers(5, 7)
result_multiply = multiply_numbers(3, 4)

math_operations = MathOperations()
result_power = math_operations.power(2, 3)

print(f"Result of add_numbers: {result_add}")
print(f"Result of multiply_numbers: {result_multiply}")
print(f"Result of power method: {result_power}")