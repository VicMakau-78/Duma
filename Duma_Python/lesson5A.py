# Python functions
# They are a block of code /statements that performs a given task /action. They can be reused through out the program to perform different tasks.
# functions are defined uing the def keyword(define)
# we have two main types of function i.e:
# 1. Built in functions: these are functions that are already defined in python and we can use them without defining them. e.g print(), input(), len(), type() etc
# 2. User defined functions: these are functions that we define ourselves to perform a specific task.(created by  the programmer)
# defining a function
# you need to give it a name followed by a paranthesis.
# For the functions, it is ususaly indented and to invoke a function we use the function name.

# defining a function
def greetings():
    print("Hello, how are you doing today?")

# Below we call the function by use of its name
greetings()

print("=================================")
# Adding function
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The addition of the two numbers is:", sum)

addition()

print("=================================")
# create a function able to mutiply three values
def multiply():
    num1 = 10
    num2 = 60
    num3 = 5
    product = num1 * num2 * num3
    print("The product of the three numbers is:", product)

multiply()

print("=================================")
# Below is a division function
def division():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    quotient = num1 / num2
    print("The division of the two numbers is:", quotient)
    print("-------------------------------")

division()