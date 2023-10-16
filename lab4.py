#Task 1. Tuples, tuples, tuples

#1.1 Write a code snippet that receives a user input (a string without whitespaces) and stores it as a tuple [5 points]

user_input = input("Enter a string without spaces: ")
tuple_1 = tuple(user_input)
print("Created tuple is:", tuple_1)

#1.2 Write a code snippet that converts a tuple in a string, use the tuple from the previous task 1.1 [5 points]
# Assuming tuple_1 contains the tuple from the previous task 1.1
tuple_1 = ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n')

# Convert the tuple to a string
string_1 = ''.join(tuple_1)

# Print the resulting string
print("The string is:", string_1)

#1.3 Write a code snippet that concatenates two tuples, particularly concatenates the first half of the tuple A with the second half of the tuple B [5 points]


# Sample Input
tuple_A = (1, 2, 3, 4, 5, 6, 7)
tuple_B = (5, 6, 7, 9, 7, 1, 10, 10)

# here (1,2,3,4)- the first half of the tuple_A
# (7,1,10,10) - the second half of the tuple_B

# Calculate the mid-point to split the tuples
mid_point = len(tuple_A) // 2

# Concatenate the first half of tuple_A with the second half of tuple_B
tuple_C = tuple_A[:mid_point] + tuple_B[mid_point:]

# Print the resulting concatenated tuple
print(tuple_C)

#1.4 Write a code snippet that calculates how many times one element  occurs in a given tuple and creates another tuple where it stores  the pair of elements and number of its occurrence.  Take into account that we can store string elements in a tuple, or even other data structures. [10 points]

def count_occurrences(input_tuple):
    occurrences = {}
    for item in input_tuple:
        if item in occurrences:
            occurrences[item] += 1
        else:
            occurrences[item] = 1
    occurrences_list = [(key, value) for key, value in occurrences.items()]
    return tuple(occurrences_list)

# Sample Inputs
input_tuple_1 = (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6)
input_tuple_2 = ('55', '6', '777', 54, 6, 7777, 9, 777, 6)
input_tuple_3 = ((1, 2, 3), (['A', 'B']), (1, 2, 3), (['A']))

# Calculate occurrences and create tuples
output_tuple_1 = count_occurrences(input_tuple_1)
output_tuple_2 = count_occurrences(input_tuple_2)
output_tuple_3 = count_occurrences(input_tuple_3)

# Print the resulting tuples
print("Elements and their occurrences:")
print(output_tuple_1)
print(output_tuple_2)
print(output_tuple_3)

#1.5 Write a code snippet that creates tuples to store a specific data objects [10 points]
# Sample data objects
data_objects = (55, 6, 777, 70.0, '7', 'A')

# Create tuples to store specific data objects
tuple_integers = tuple(item for item in data_objects if isinstance(item, int))
tuple_floats = tuple(item for item in data_objects if isinstance(item, float))
tuple_strings = tuple(item for item in data_objects if isinstance(item, str))

# Print the resulting tuples
print(tuple_integers)
print(tuple_floats)
print(tuple_strings)

#2.1 Write a code snippet that receives a user input (a string without whitespaces)
# and stores it as a set. Use of the set comprehensions from Lecture 5, slide #7. [5 points]

# Receive user input as a string without whitespaces
user_input = input("Enter a string without spaces: ")

# Create a set using set comprehensions
created_set = {char for char in user_input}

# Print the resulting set
print("Created set is:", created_set)


#2.2 Write a code snippet that creates a set which is a difference of two sets:

# Sample Input
set_A = {1, 2, 3, 4, 5}
set_B = {5, 7, 8, 9, 2, 10}

# Calculate the difference of set_A and set_B
result_set = set_A.difference(set_B)

# Print the resulting set
print(result_set)

#2.3 Write a code snippet that removes all elements from set A which are also in set B:

# Sample Input
set_A = {1, 2, 3, 4, 5}
set_B = {5, 7, 8, 9, 2, 10}

# Remove elements from set_A that are in set_B
set_A.difference_update(set_B)

# Print the resulting set_A
print(set_A)

#2.4 Write a code snippet that removes an element from set A and adds it to set B if that element is in set C:


# Sample Input
set_A = {1, 2, 3, 4, 7}
set_B = {8, 7, 9, 4, 2, 0, 10}
set_C = {4, 0, 1}

# Check each element in set_A, move to set_B if in set_C
for element in set_A.copy():
    if element in set_C:
        set_A.remove(element)
        set_B.add(element)

# Print the updated sets
print("Updated set_A:", set_A)
print("Updated set_B:", set_B)


#2.5 Write a code snippet that creates a list (size m) of sets of size n, where each element is a unique combination drawn from a superset A:


import random

# Sample Input
A = {1, 2, 3, 4, 5, 6}
n = 3
m = 5

# Create a list of sets with unique combinations
combinations_list = []
for _ in range(m):
    combination = set(random.sample(A, n))
    combinations_list.append(combination)

# Print the list of sets
print(combinations_list)



