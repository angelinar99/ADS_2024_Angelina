"""
Exercises "Lists"
"""

"""
### List Initialization and Accessing Items ###

Create a list named "colors" containing at least five different colors as strings. 
Print the third color in the list.
"""
colors_list = ["red", "green", "blue", "orange", "purple"]
print(colors_list[2])
# Write your solution here

"""
### List Mutability ###

Initialize a list of numbers from 1 to 5. Change the second number in the list to 10.
Print the modified list.
"""
list_numbers = [1, 2, 3, 4, 5]
print(list_numbers)
third_number = list_numbers[1]
list_numbers[1] = 10
print(list_numbers)
# Write your solution here

"""
### Append and Insert Method ###

Create an empty list named "pets". Use the append method to add "dog", "cat", and "bird" to the list.
Then use the insert method to add "lizard" at the second position in the list.
Print the updated list.
"""
pets = []
pets.append("dog")
pets.append("cat")
pets.append("bird")
pets.insert(1, "lizard")
print(pets)
# Write your solution here

"""
### Removing Items ###

Given the list ['apple', 'banana', 'cherry', 'date'], 
write a program that removes 'banana' using the remove() method and 'date' using the pop() method. 
Print the final list after these operations.
"""

list_of_fruits = ['apple', 'banana', 'cherry', 'date']
list_of_fruits.remove("banana")
print(list_of_fruits)
list_of_fruits.pop(-1)
print(list_of_fruits)
# Write your solution here

"""
### Sort Method and Sorting Function ###

Create a list of integers like: [5, 2, 9, 1, 5, 6].
Sort this list using the sort() method and then print it.
Next, use the sorted() function on the list ['orange', 'apple', 'banana'] and print the result.
"""

list_of_unsorted_fruits = ['orange', 'apple', 'banana']
num_list = [5, 2, 9, 1, 5, 6]
num_list.sort()
print(num_list)
list_of_unsorted_fruits.sort()
print(list_of_unsorted_fruits)
# Write your solution here

"""
### Min, Max, and Sum Functions ###

Given a list of numbers [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
Print the minimum, maximum, and sum of the list.
"""

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
less = min(list_of_numbers)
great = max(list_of_numbers)
sum_list = sum(list_of_numbers)
print(less, great, sum_list)
# Write your solution here

"""
### Slicing Lists Without Step and With Step ###

Create a list of the first 10 even numbers. Slice and print the first half of the list.
Then, slice and print every second number from the sliced list.
"""
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(List[:5])
print(List[::2])
# Write your solution here
