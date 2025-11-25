def start_end_decorator(func):

    def wrapper(*args, **kwargs):
        print("starting the function")
        result = func(*args, **kwargs)
        print("ending the function")
        return result
    return wrapper


@start_end_decorator
def print_name(x,y):
    return x + y

result = print_name(3,4)

print(result)



# double number decoratoer



def double_decorator(func):
    def wrapper(x):
     return func(x) * 2
    return wrapper

@double_decorator
def multiply_by_two(x):
    result = x * 2
    return result
print(multiply_by_two(5))







def uppercase_decorator(func):
    def wrapper(name):
        result = func(name)
        return result.upper()
    return wrapper


@uppercase_decorator
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))