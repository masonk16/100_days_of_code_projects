import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        start = time.time()
        function()
        end = time.time()
        run_speed = end - start
        print(f'{function.__name__} run speed: {run_speed}s')

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()


class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])

    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("Mason")
new_user.is_logged_in = True
create_blog_post(new_user)


# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        function(args[0], args[1], args[2])
        print(f"You called {function.__name__}{args[0], args[1], args[2]}")
        print(f"It returned: {function(args[0], args[1], args[2])}")

    return wrapper


# Use the decorator 👇
@logging_decorator
def calculate(a, b, c):
    return a + b + c

calculate(1, 2, 3)