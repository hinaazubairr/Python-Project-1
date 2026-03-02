
# Topic: Functions
# Sometimes, a program in Python often repeat the same set of actions defined in a block of code.
# Rather than reqrite the same block of code repeatedly in your program, create a function that you can use anywhere you need.

# Create a Function:
    # In Python, every function has a name, which is what you use to call it.

# Syntax for defining a function:
'''
def function_name():
    action 1
    action 2
'''

# All functions start with the keyword 'def' followed by 'the name of the function' and 'a pair of parentheses'.

# Just below the function is the function body. The function body contains whatever actions you choose to have your function complete.

# Example of a hello_world function that prints the string "Hello World":
def hello_world():
    print("Hello World")


# Call a function: 
# The function in the prior example won't do anything in your program until you call the function.
# Calling a function tells your code to run the code inside the function body.
# To call a function, use the function name and include the parentheses.
hello_world()


# Return:
# You can end the run of a function by including a return statement in the function body.
# A return statement appears at the end of the actions within the function body and can include an expression.
# An expression is a combination of values, variables, operators, and calls to functions.
'''
def function_name():
    action 1
    return
'''
# If an expression is included with the return statement, the expression is evaluated and the value is returned.
# Returning a value is useful as it enables you to use the result value of a function in your code.
# However, if no return statement is included at the end of a function, the function returns None.
def hello_world():
    print("Hello World")
    return
hello_world()


# Parameters
# Sometimes, you may need to provide data with your function to complete the action inside the function body.
# The data that you pass into a function is known as a parameter.
'''
def function_name(parameter1, parameter2):
    action 1
'''
# when you call a function that has parameters, you provide values for the parameters inside the parentheses. These values are known as arguments.
# Python takes the arguments and assigns them to the variables named by the parameters.
# By default functions accept arguments in order and assigns the arguments to the parameters in that order.

# Let's create a good_morning() function that greets a person using their first and last names.
def good_morning(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    return
good_morning('hina','zubair')

# The good_morning() function has 2 parameters, first_name and last_name.
# Inside the function body, a string prints that includes the arguments used in the function call for the good_morning() function.
# when the good_morning() function is called, the two arguments you provide in the parentheses appear in the parameter variable first_name, last_name inside the function.


# its imp to know that a function can accept any type of value as an argument, like an int.

# For example write a function sum() that takes 2 parameters, a and b, and returns the sum of the 2 numbers:

def sum(a,b):
    print(f"1st number is: {a}")
    print(f"2nd number is: {b}")
    sum=a+b
    print(f"The sum of {a} and {b} are:, {sum}")
    return sum
sum(1,2)

# OR

def sum(a,b):
    return a+b
print(sum(1,2))


# Default arguments
# A function can also have default arguments, which makes the parameter optional.
# The function uses the default value unless one is provided when calling the function.

'''
def function_name(parameter=value):
    action 1
'''
# A default value is assigned to a parameter when creating a function.
# When you call a function that has deafult values, the default value is used.

# The following is an example of a function 'favorite_season', which has a parametr season. The default value for the parameter season is 'Summer'.
def favorite_season(season='Summer'):
    print(f"{season} is my favorite season.")
favorite_season()

# in the previous eg, favorite_season) is called without passing a value into the parentheses. as a result, the string summer is my favorite season is pinted.
# if you were to pass a value in the function call, the value provided is used instead and therefore printed.
def favorite_season(season='Summer'):
    print(f"{season} is my favorite season.")
favorite_season('Spring')





# Arbitrary arguments
# You can also create a function without knowing how many arguments will be passed into the function.
# An arbitrary argument is indicated by a * before the parameter name in a function.
# arbitrary arguments are often referred to as *args.
'''
def function_name(*args):
    action 1
    action 2
'''

# consider the following states_traveled() function that returns a string that prints the names of states visited.
def states_traveled(*states):
        for state in states:
            print(f'I visited the {state}.')
    
states_traveled('UK','Italy', 'Florida')
# The for loop created in the body of the states_traveled() function prints a string that includes each of the arguments passed into the function call.



# Keyword arguments
# You also have the option to pass arguments into a function call without maintaining the default order.
# if you dont want to depend on ordering, then you can name the arguments.
# you can name arguments by creating keyword arguments in the function call.
# keyword arguments are often referred to as *kwargs.
'''
function_name(keyword1=value1, keyword2=value2)
'''

# the following gameshow_contestants() function contains 3 parameters, which reflect the names of the contestants.
def gameshow_contestants(contestants_1,contestants_2,contestants_3):
    print(f"Here are today's contestants: {contestants_1}, {contestants_2}, {contestants_3}")
gameshow_contestants(contestants_2='Lucy',contestants_1='pippa',contestants_3='Steven')


# Built-in functions
# you could create your own functions to use in a program, Python also has dozens f builtin functions.
# you've already used few earlier:
# print()------bool()-----float()----int()----input()------len()---range()------slice()-----str()-------type()
# There are more than 60 built in functions available in python.

