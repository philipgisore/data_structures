count = 0

def get_count():
    count = 5
    print("Inside get_count, count =", count)
get_count()
print("Before calling get_count, count =", count)

#Accessing Global variable inside a function
message = "Hello, World!"

def print_message():
    global message # Declare message as global to modify it
    print("Message inside function:", message)
    message = "Hello, Python!"  # Modify the global variable
print_message()
print("Outside function, message = ", message)

#using nonlocal keyword(accessing variable from outer scope in nested/enclosing function)
def outer_function():
    count = 0

    def inner_function():
        nonlocal count
        count += 1
        print("Inner count:", count)
    inner_function()
    inner_function()
    print("Final count in outer:", count)
outer_function()
