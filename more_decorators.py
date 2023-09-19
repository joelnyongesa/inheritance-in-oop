def hello(name):
    return f"Hello {name}"

# print(hello("Joel"))

greeting = hello

def salutation(func):
    return func("Medrine")

# print(salutation(greeting))

# We can also define functions inside other functions
def say_hello():
    print("Hello from the say_hello() function")

    def greet():
        print("greetings from the greet() function")
    
    # By returning greet without parsentheses, hello() is returning itself
    return greet


def decorator(func):
    def wrapper():
        print("I am the output that lets you know the function is about to be called.")
        func()
        print("I am the output that lets you know the function has been called.")
    return wrapper

# def get_called():
#     print("I am the function and I am being called")

# get_called = decorator(get_called)
# get_called()

# We can also use the pie syntax
@decorator
def get_called():
    print("I am the function and I am being called")

get_called()