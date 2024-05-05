"""
Exercises "Functions"
"""

"""
### Function Definition / Execution ###

Define a function called "bark()". When executed, "Woof" should get printed to the console.
Execute the function after its definition and run the program!
"""
def bark():
    print("Woof")

bark()


def bark():
    print("Woof")


bark()

"""
### Function with 1 Argument, additional logic ###

Write a program that asks the user to enter an animal. The program should respond with the corresponding animal sound.
Define a function called "make_Sound(animal)". The function should use the given input to print the correct animal sound.
Add functionality for at least 3 animals and print the right sounds.
If the animal doesn't exists in the program, print "???".
Use a loop to repeatedly ask the user to enter another animal.
Make sure that upper- and lowercase letters both work when entering an animal.

Examples:
    Please enter an animal: >> dog
    Woof
    Please enter an animal: >> Cat
    Meow
    ...
"""

def make_sound(animal):
    animal = animal.lower()
    if animal == "dog":
        print("Woof")
    elif animal == "cat":
        print("Meow")
    elif animal == "cow":
        print("Moo")
    else:
        print("???")

#make_sound("dog")
# make_sound("CAT")
runs 5 times
i = 0
while i < 5:
    animal_input = input("Enter an animal: ").lower()
    make_sound(animal_input)
    i += 1

#for i in range(0,5): copy rest

while True:
    user_input = input("Please enter an animal: ")
    if user_input == "exit":
        print("Bye")
        break
    make_sound(user_input)
"""
 
 Function with 2 Arguments

Write a function named print_many_times(text, times), which takes a string and an integer as arguments. 
The integer argument specifies how many times the string argument should be printed out.

Example:
    print_many_times("Gimme Five!", 5)
    Gimme Five!
    Gimme Five!
    Gimme Five!
    Gimme Five!
    Gimme Five!

Additional Task:
Instead of "hard coding", let the user enter the text and the number of times to print it!
Ask the user repeatedly using a loop.
"""


def print_many_times():
    while True:
        text = input("Enter the text: ")
        if text == "quit":
            break
        times = int(input("Enter the number of times to print: "))
        for _ in range(times):
            print(text)
def print_many_times_again(text: str, times: int):
   print((text + "\n") * times)
   print(f" {text} \n * times)")
# Call the function to start the loop

print_many_times()

"""
### Return Values ###

Define a function named greatest_number, which takes three arguments. The function returns the greatest in value of the 
three. Use the already defined function "print_greatest" and pass the return value of your function to it!

Example:
    return_value = greatest_number(3, 4, 1)
    print_greatest(return_value)
    The greatest number is 4!
    
Additional Task:
Add a type hint to the return value of the function!
"""
def greatest_number(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        return a
def print_greatest(number):
    print(f"The greatest number is {number}!")

return_value = greatest_number(3, 4, 1)
print_greatest(return_value)
print_greatest(greatest_number(3, 4, 1))


"""
### Type Hints ###

Refactor your programs from above and add type hints to all function arguments and return values (if available)!
"""

# No code here, refactor the programs above!
# a: int, b: int, c: int -> int

"""
### Named arguments ###

Define a function named super_print which takes two arguments, a string and a boolean value.
If the boolean value is false, print the text as it was. If its True, print it in all upper case.
Use named arguments to use a different order of the arguments. First, use the string as first argument. For the second
call, use the boolean value as the first argument. Also, make use of type hints for the function arguments.

Example Outputs:
    HELLO WORLD
    hello world
"""

# Write your solution here
def super_print(text: str, upper: bool):
    if upper:
        print(text.upper())
    else:
        print(text)

# Call the function with the string as the first argument
super_print(text="hello world", upper=True)

# Call the function with the boolean value as the first argument
super_print(upper=False, text="hello world")

"""
### Default Values ###

Define a simple function greet() that takes one argument "name". The function should print a greeting for the entered 
name. Ask the user for his/her name and execute the greet function, passing the name as an argument.
If nothing was entered, use a default value for the name to greet "Unknown".

Hint: An empty string is still a value you can pass, be careful :-)

Example:
    Please enter your name: >> René
    Hello René!
    Please enter your name: >> 
    Hello Unknown!
"""

# Write your solution here
def greet(name: str = "Unknown"):
    print(f"Hello {name}!")

# Ask the user for his/her name
user_name = input("Please enter your name: ")

# If the user doesn't enter a name, pass an empty string to the function
if user_name == "":
    greet()
else:
    greet(user_name)
# Write a function is_palindrome taht takes a string as a parameter
# input and returns Boolean value True if the string is a palindrome and False otherwise.
# A palindrome is a word or phrase that reads the same forward and backward ignoring spraces and capitalization.
# make us of hints when declaring them

#Task 2
# write a function named print_multiplication which gets the following arguments passed: two integrer values first
# a certain number for which the multiplication table shall be printed and secondly a number that specifes the number of
# rows.
# only number bigger than 0 are valid. print error message if number zero or negative


"""
Palindromes
"""
#Task 1
# Provide your solution here
def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")
    return s == s[::-1]



print(is_palindrome("taco cat"))  # True
print(is_palindrome("Step on no cats"))  # False
print(is_palindrome("Never odd or even"))  #True
print(is_palindrome("Me no palindrome"))  #False


"""
Multiplication Table
"""
#Task 2
#Provide your solution here

def print_multiplication(number: int, rows: int) -> None:

    if number <= 0 or rows <= 0:
        print("Error: Number and rows cannot be less than 1.")
        return

    for i in range(0, rows + 1):
        print(f"{number} * {i} = {number * i}")

print_multiplication(6, 3)
print_multiplication(10,2)
print_multiplication(0, 0)
print_multiplication(-10, 2)
print_multiplication(2,-2)


