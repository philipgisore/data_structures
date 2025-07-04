## This script demonstrates the use of namespaces in Python.
# It shows how variables can be defined in different scopes and how they can be accessed or modified
def counting_function():
    count = 10
    print("Inside counting_function, count =", count)
def logging_function():
    count = "Log entry #1"
    print("Inside logging_function, count =", count)

counting_function()
logging_function()