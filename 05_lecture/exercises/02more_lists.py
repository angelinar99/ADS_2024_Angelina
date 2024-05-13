"""
Write a function named list_of_stars, which takes a list of integers as its argument.
The function should print out lines of star characters. The numbers in the list specify how many stars each line should contain.

For example, with the function call list_of_stars([3, 7, 1, 1, 2]) the following should be printed out:

    ***
    *******
    *
    *
    **
"""
def list_of_stars(numbers):
    for i in range(len(numbers)):
        print(numbers[i] * "*")
list_of_stars([2, 5, 3, 6])

# Provide your solution here
# def list_of_stars(numbers):
# for i in numbers:
#     print(numbers * "**")
# list_of_stars = [3, 7, 1, 1, 2]
# print(list_of_stars)
#
# def list_of_stars(numbers):
#     starstring = "*" * 5
#     print(starstring)
# list_of_stars([])
# def list_of_stars(numbers):
#     for i in numbers:
#         print(i * "*")
# list_of_stars([1, 2, 10])

"""
Write a function named anagrams, which takes two strings as arguments. 
The function returns True if the strings are anagrams of each other. 
Two words are anagrams if they contain exactly the same characters.

Some examples of how the function should work:

    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False
"""
# def anagrams(str1, srg2) -> bool:
#     str1 = str1.lower().replace("", "")
#     srg2 = srg2.lower().replace("", "")
#     return sorted(str1) == sorted(srg2)
#
#
# print(anagrams("tame", "meta")) # True
# print(anagrams("tame", "mate")) # True
# print(anagrams("tame", "team")) # True
# print(anagrams("tabby", "batty")) # False
# print(anagrams("python", "java")) # False
# Provide your solution here
def anagrams(str1:str, str2:str) -> bool:
    list1 = list(str1)
    list2 = list(str2)
    list1.sort()
    list2.sort()
    if list1 ==list2:
        print(True)
    else:
        print(False)

print(anagrams("tame", "meta")) # True
print(anagrams("tame", "mate")) # True
print(anagrams("tame", "team")) # True
print(anagrams("tabby", "batty")) # False
print(anagrams("python", "java")) # False
"""
Write a function named sum_of_positives, which takes a list of integers as its argument. 
The function returns the sum of the positive values in the list.

    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result) # prints The result is 9

"""
def sum_of_positives(numbers):
    total = 0
    for i in numbers:
        if i > 0:
            total += i
            return total


my_list = [1, -2, 3, -4, 5]
result = sum_of_positives(my_list)
print("The result is", result)


# Provide your solution here


"""
Write a function named even_numbers, which takes a list of integers as an argument. 
The function returns a new list containing the even numbers from the original list.

    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)
    
    Prints:
        original [1, 2, 3, 4, 5]
        new [2, 4]
"""

# Provide your solution here
def even_numbers(nums):
    even_list = []
    for x in nums:
        if x % 2 == 0: # Check if the number is even
            even_list.append(x) # Add the even number to the even_list
    return even_list  # Return the list of even numbers

my_list = [1, 2, 3, 4, 5]
new_list = even_numbers(my_list)
print("original", my_list)
print("new", new_list)

"""
Write a function named list_sum which takes two lists of integers as arguments. 
The function returns a new list which contains the sums of the items at each index in the two original lists. 
You may assume both lists have the same number of items.

An example of the function at work:

    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]
"""
# Provide your solution here
def list_sum(list1, list2):
    result = []
    for i in range(len(list1)):
        sum_i = list1[i] + list2[i]
        result.append(sum_i)
    return result
a = [1, 2, 3]
b = [7, 8, 9]
print(list_sum(a, b))

