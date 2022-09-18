
def function_1():
    # assigning a string as a member of the function object
    function_1.variable = [1,2]
    print("function_1 has been called")
def function_2():
    print("function_2 has been called")
    print(function_1.variable)
function_1()
function_2()