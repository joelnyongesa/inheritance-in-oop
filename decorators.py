'''
    Decorators in Python allows us to modify the functionality
    of a function by wrapping it in another function.
'''

def check_validity(func):
    def wrapper(age):
        if age >= 18:
            func(age)
        else:
            print("Not permitted")
    return wrapper

@check_validity
def allowed_to_drink(age):
    print("Allowed to drink")

@check_validity
def allowed_to_drive(age):
    print("Allowed to drive")

age = 17
allowed_to_drink(age)