#Global scope
value = "Global value"

def outer_function():
    #Enclosing scope
    value = "Enclosing value"

    def inner_funtion():
        #Local scope
        nonlocal value
        value = "Local value"
        print("Local value:", value) # This will print the local value

        # To modify the enclosing scope variable, we can use nonlocal
        value = "Modified enclosing value"
        print("Inner function value:", value)

        #Access the global value using globals()
        print("Accessing global value with globals():", globals()['value'])
    inner_funtion()
    print("After inner function, value in outer function:", value)

outer_function()
print("Value in global scope remains:", value)


