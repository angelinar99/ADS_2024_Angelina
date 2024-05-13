"""
Write a program which asks the user for a string and an amount.
The program then prints out the string as many times as specified by the amount.
The printout should all be on one line, with no extra spaces or symbols added.

Example:
    Please type in a string: >> hey
    Please type in an amount: >> 4
    heyheyheyhey
"""
# Ask the user for a string and an amount
input_string = input("Please enter a string: ")
amount = int(input("Please enter the amount of times to repeat: "))

# Print the string as many times as specified by the amount
print(input_string * amount, end="")


"""
Write a program which asks the user for two strings and then prints out whichever is the longer of the two - 
that is, whichever has the more characters. If the strings are of equal length, the program 
should print out "The strings are equally long".

Examples:

    Please type in string 1: >> hello
    Please type in string 2: >> world
    The strings are equally long
    
    Please type in string 1: >> hey
    Please type in string 2: >> world
    world is longer
"""

# Write your solution here
input_string = input("Please enter a string: ")
input_string_2 = input("Please enter a string: ")

if len(input_string) > len(input_string_2):
    print(f"{input_string} is greater")
elif len(input_string) < len(input_string_2):
    print(f"{input_string} is less")
else:
    print("equal")
"""

Write a program which asks the user for a string. The program then prints out the input string in reversed order, 
from end to beginning. Each character should be on a separate line.
Try to solve this example in 2 ways:
    * once using positive indeces
    * once using negative indeces
"""
str = input("String here: ")
for i in range(-1, -len(str) - 1, -1):
    print(str[i])

for i in range(len(str) - 1, -1, -1):
    print(str[i])

# Write your solution here

# user_string = input("Please enter a string: ")
# for i in range(len(user_string)-1, -1, -1,):
#     print(user_string[i])
# user_string = input("Please enter a string: ")
# for i in range(-1, -len(user_string)-1, -1):
#     print(user_string[i])
# Ask the user for input
user_input = input("Please enter a string: ")

# Method 1: Using positive indices
print("Using positive indices:")
reversed_string = user_input[::-1]  # Reverse the characters using slicing
for char in reversed_string:
    print(char)  # Print each character

# Method 2: Using negative indices
print("\nUsing negative indices:")
length = len(user_input)
for i in range(length - 1, -1, -1):  # Iterate through the characters from end to beginning
    print(user_input[i])  # Print each character


"""
Write a program which asks the user for a string. 
The program then prints out a message based on whether the second character and the second to last character 
are the same or not. See the examples below.

Examples:
    Please type in a string: >> python
    The second and the second to last characters are different
    
    Please type in a string: >> pascal
    The second and the second to last characters are a
"""
# Write your solution here
# Ask the user for a string
input_string = input("Please enter a string: ")

# Check if the second character and the second to last character are the same
if len(input_string) >= 2 and input_string[1] == input_string[-2]:
    print("The second character and the second to last character are the same.")
else:
    print("The second character and the second to last character are not the same.")


"""
Write a program which prints out a line of hash characters, the width of which is chosen by the user.

Examples:
    Width: >> 8
    ########
    
    Width: >> 2
    ##
"""
# # Write your solution here
# # Ask the user for the width of the line
width = int(input("Please enter the width of the line: "))

# Print a line of hash characters with the specified width
print("#" * width)

"""
Modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly.

Example:
    Width: >> 10
    Height: >> 3
    ##########
    ##########
    ##########
"""
# Write your solution here
# Ask the user for the width of the line
width = int(input("Please enter the width of the line: "))
height = int(input("Please enter the height of the line: "))
# Print a rectangle of hash characters with the specified width and height
for x in range(height): #for _ I can use i
    print("#" * width)

"""
Write a program which asks the user for a string and then prints it out so that exactly 20 characters are displayed. 
If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.

You may assume the input string is at most 20 characters long.

Examples:
    Please type in a string:hello
    ***************hello
    
    Please type in a string:helloworld
    **********helloworld 
"""
# Write your solution here
# Ask the user for a string
input_string = input("Please enter a string: ")

# Calculate the number of * characters needed to fill the beginning of the line
num_stars = 20 - len(input_string)

# Print the line with * characters filled in at the beginning, if needed
print("*" * num_stars + input_string)

"""
Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre. 
The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.

If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.

Examples:
    Word: >> testing
    
    ******************************
    *          testing           *
    ******************************

"""
#Write your solution here
# user_string = input("Please enter a string: ")
frame_width = 30
padding = (frame_width - len(user_string) - 2) // 2
print('*' * frame_width)
print('*' + ' ' * padding + user_string + ' ' * padding + '*')
print('*' * frame_width)



"""
Write a program which asks the user to type in a string. 
The program then prints out all the substrings which begin with the first character, 
from the shortest to the longest. Have a look at the example below.

Example:
    Please type in a string: >> test
    t
    te
    tes
    test
"""
# Write your solution here

user_string = input("Please type in a string: ")
for i in range(0, len(user_string) + 1):
    print(user_string[:i])

# Run the function


"""
Write a program which asks the user to input a string. The program then prints out different messages if the string 
contains any of the vowels a, e or o.

You may assume the input will be in lowercase entirely. Have a look at the examples below.

    Please type in a string: >> hello there
    a not found
    e found
    o found
    
    Please type in a string: >> hiya
    a found
    e not found
    o not found
"""
# Write your solution here
user_string = input("Please type in a string: ")

if 'a' in user_string:
    print('a found')
else:
    print('a not found')

if 'e' in user_string:
    print('e found')
else:
    print('e not found')

if 'o' in user_string:
    print('o found')
else:
    print('o not found')


"""
Write a program which asks the user to type in a string and a single character. The program then 
prints the first three character slice which begins with the character specified by the user. 
You may assume the input string is at least three characters long. The program must print out three characters, 
or else nothing.

Pay special attention to when there are less than two characters left in the string after the first occurrence of 
the character looked for. In that case nothing should be printed out, and there should not be any indexing errors 
when executing the program.

Examples:

    Please type in a word: >> mammoth
    Please type in a character: >> m
    mam
    
    Please type in a word: >> banana
    Please type in a character: >> n
    nan
    
"""
# Write your solution here
user_string = input("Please type in a word: ")
user_char = input("Please type in a character: ")

index = user_string.find(user_char)
if index != -1 and index <= len(user_string) - 3:
    print(user_string[index:index+3])
# print("IndexQ"
"""
Write a program which finds the second occurrence of a substring. If there is no second (or first) occurrence, 
the program should print out a message accordingly.

In this exercise the occurrences cannot overlap. For example, in the string aaaa the second occurrence of the 
substring aa is at index 2.

Examples:

    Please type in a string: >> abcabc
    Please type in a substring: >> ab
    The second occurrence of the substring is at index 3.
    
    Please type in a string: >> methodology
    Please type in a substring: >> o
    The second occurrence of the substring is at index 6.
    
    Please type in a string: >> aybabtu
    Please type in a substring: >> ba
    The substring does not occur twice in the string.
"""
# Write your solution here
user_string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

first_occurrence = user_string.find(substring)
if first_occurrence == -1:
    print("The substring does not occur in the string.")
else:
    second_occurrence = user_string.find(substring, first_occurrence + len(substring))
    if second_occurrence == -1:
        print("The substring does not occur twice in the string.")
    else:
        print("The second occurrence of the substring is at index {}.".format(second_occurrence))
