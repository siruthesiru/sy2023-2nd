# Functions
# The "def" keyword is used to create a function. The syntax is def <functionName>()

# define a function called my_greeting

# Parameteres can be added to the function to have more control to what the inputs for the function will be
def my_greeting(username):
    # code to be run when my_greeting is called back
    print(f"Hello, {username}!")

# Calling/Invoking of the function
my_greeting("Grandmaster of the 7th Chamber Phillip")

# Using return statements
def addition(num1, num2):
    return num1 + num2

sum = addition(1, 2)
print(f"The sum is {sum}.")

# Lambda Functions
# small anonymous function that can be used for callbacks

greeting = lambda person : f'Hello, {person}.'
print(greeting("Curly"))

multiply = lambda a, b : a * b
print(multiply(5, 6))
print(multiply(6, 99))