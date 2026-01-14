'''
# Hashing

Hashing is a technique that is frequently used in implementing efficient algorithms. In Python, the data structures set and dict (dictionary) are based on hashing.

In this chapter, we take a look at data structures based on hashing and their use in algorithm design. We will also cover some theory underlying the data structures.
Set

The Python data structure set, based on hashing, maintains a set of elements. The operations on the data structure include:

    the method add adds an element to the set
    the operator in finds if a given element is in the set
    the method remove removes an element from the set

The data structure is implemented so that all of the above operations take O(1)O(1) time.
Example
'''

#-> The following code creates a set numbers and adds elements to the set:
from re import L, U


numbers = set()
numbers.add(1)
numbers.add(2)
numbers.add(3)
print(numbers)

#-> We can also create a set directly from a list:
numbers = set([1, 2, 3])
print(f'creating set directly from a list {numbers}')

#-> The operator in tests if an element is in the set:
print(3 in numbers)
print(4 in numbers)

#-> And we can remove an element from the set with the method remove:
print(numbers)
numbers.remove(2)
print(f'Removed elements from the set {numbers}')


'''
## List vs. set

A list and a set are similar data structures in that both maintain a collection of elements and support additions and removals. However, there are significant differences in their efficiency and other properties.

###Efficiency

Adding an element to a list is efficient, but finding an element and removing it can be slow.

With a set, adding elements, finding elements and removing elements are all efficient operations.

Operation 	            List 	    Set
Adding (append/add) 	O(1)O(1) 	O(1)O(1)
Finding (in) 	        O(n)O(n) 	O(1)O(1)
Removing (remove) 	    O(n)O(n) 	O(1)O(1)

'''

# Indexing

#-> In a list, elements can be accessed using an index:
numbers = [1, 2, 3]
print(numbers[0])  # Output: 1

#-> A set does not support indexing:
# numbers = {1, 2, 3}
#print(numbers[1]) # TypeError: 'set' object is not subscriptable

# Repeated elements

#-> In a list, an element can occur multiple times:
Listnumbers = []
Listnumbers.append(5)
Listnumbers.append(5)
Listnumbers.append(5)
print(Listnumbers)  # Output: [5, 5, 5]

#-> A set contains an element at most once. Adding an element that is already in the set has no effect:
setNumbers = set()
setNumbers.add(5)
setNumbers.add(5)
setNumbers.add(5)
print(setNumbers)  # Output: {5}


'''
### Example: How many numbers?

You are given a list of numbers. How many distinct numbers does it contain?

For example, when the list is [3,1,2,1,5,2,2,3], the desired answer is 4, because the distinct numbers are 1, 2, 3 and 5.
'''


# Slow solution (list)
#-> We could solve the task using a list as follows:

import time
def count_distinct(num):
    seen = []
    for x in num:
        if x not in seen:
            seen.append(x)
    return len(seen)

num = [3,1,2,1,5,2,2,3]

start_time = time.perf_counter()
print(count_distinct(num))

end_time = time.perf_counter()
print(f'Time taken: {end_time - start_time} seconds')

# That number is in scientific notation.
# 8.200000593205914e-06 seconds means:
# The e-06 means "× 10⁻⁶" (move the decimal 6 places to the left).
# So 8.200000593205914e-06 = 0.0000082 seconds.
# That’s 8.2 microseconds (millionths of a second).


'''
The algorithm goes through the numbers and adds a number to a list seen if it is not there already. At the end, the length of the list seen is the desired answer.

This algorithm is correct but not efficient, because every round of the loop calls the operator in, which can take O(n) time. Thus the time complexity of the algorithm is O(n2). However, a simple improvement is to use a set instead of a list.
'''


# Efficient solution (set)
#-> We can solve the task efficiently using a set as follows:

import time
def count_distinct(nums):
    seem = set()
    for x in nums:
        if x not in seem:
            seem.add(x)
    return len(seem)

nums = [3,1,2,1,5,2,2,3]

start_time = time.perf_counter()
print(count_distinct(nums))

end_time = time.perf_counter()
print(f'Time taken: {end_time - start_time} seconds')


'''We can shorten the code further by creating the set directly from the list. Only one line is needed:'''

def count_distinct(numbers):
    return len(set(numbers))
print(count_distinct([3,1,2,1,5,2,2,3]))

'''
## Dictionary

The Python data structure dict or dictionary is based on hashing and stores key-value pairs. The idea is that we can use the key to retrieve the associated value.

A dictionary can be seen as a generalization of a list: In a list, keys are the indices 0…n0…n, while in a dictionary, keys can be arbitrary objects.

Adding, accessing and removing data using a key takes O(1) time.
'''

#Example
#The following code creates a dictionary weights where the keys are strings and the values are numbers.

weights = dict()
weights['apina'] = 100
weights['banaani'] = 1 
weights['cembalo'] = 500

# The same dictionary can also be created as follows:
weights = {'apina': 100, 'banaani': 1, 'cembalo': 500}

# The values in a dictionary can be used in the same way as the elements of a list:
print(weights['apina'])  # Output: 100
weights['apina'] = 150

# The command del removes a key and the associated value from a dictionary:
print(weights)
del weights['banaani']
print(weights)

'''
Using a dictionary
We will next take a look at three common ways to use a dictionary in algorithm design.

Has an element occured
A dictionary can be used similarly to a set to keep track of elements that have been seen:

# seen = {}
# for x in items:
#     seen[x] = True

This code has approximately the same functionality as the following code:

# seen = set()
# for x in items:
#     seen.add(x)

Indeed, a set can be seen as a special case of a dictionary, where each key is associated with the value True (or any fixed value).

Counting occurrences

A common use of dictionaries is counting element occurrences:

# count = {}
# for x in items:
#     if x not in count:
#         count[x] = 0
#     count[x] += 1

This code counts the number of occurrences of each element using the dictionary count. If the element is not yet in the dictionary, the code adds the element as a key with the initial count of zero as the associated value. Then the count is incremented by one for every occurrence of the element.

Position of occurrence

In some algorithms, it is useful to keep track of where each element has occurred.

# pos = {}
# for i, x in enumerate(items):
#     pos[x] = i

Here the dictionary pos stores the index of the most recent occurrence of each element. Using the function enumerate, the code iterates through the list items so that in each round i is the index of an element and x is the element itself.

'''

# Example: Mode

# Task => You are given a list of numbers, and your task is to compute the mode, which is the most frequent number on the list. If the mode is not unique, you can choose any of the possible choices for the most frequent number.

# For example, when the list is [1,2,3,2,2,3,2,2][1,2,3,2,2,3,2,2], the desired answer is 22.
# We can solve the task efficiently by using a dictionary to count the number of occurrences:


def find_mode(numbers):
    count = {}
    mode = numbers[0]
    
    for x in numbers:
        if x not in count:
            count[x] = 0
        count[x] = count[x] + 1
        
        if count[x] > count[mode]:
            mode = x
    print(f"count: {count}")
    print(f"Mode count: {count[mode]}")
    return mode

print(f"Find mode: {find_mode([1,2,3,2,2,3,2,2])}")  # Output: 2

'''
Here count is a dictionary that stores the occurrence count for each element, and the variable mode stores the mode among the elements seen so far. Initially, mode is the first number on the list, and it is updated whenever the just updated count of an element exceeds the count of the current mode. Since the dictionary operations take O(1) time, the time complexity of the algorithm is O(n).
'''

# Here is another way to implement the algorithm:
def find_mode(numbers):
    count = {}
    mode = (0, 0) # (count, number)
    
    for x in numbers:
        if x not in count:
            count[x] = 0
        count[x] = count[x] + 1
        
        mode = max(mode,  (count[x], x))
    print(f"count: {count}")
    print(f"Mode count: {mode[0]}")
    return mode[1]

print(f"Find mode: {find_mode([1,2,3,2,2,3,2,2])}")  # Output: 2

'''
Now the variable mode is a pair, where the first element is the occurrence count of the mode and the second element is the mode itself. For example, the value (5, 2) means that the number 2 has occurred 5 times.

The advantage of this implementation is that we can use the function max to update the mode. Here max uses the first element of the pair as the primary comparison key and the second element as a secondary comparison key. Since the first element is the occurrence count, the pair with the larger count gets chosen by max.

Notice that the two functions may operate differently when there are multiple choices for the mode. The first function chooses the mode that reaches the final count first. The second function chooses the mode with the largest value, since the value of the mode is used as a secondary comparison key.
'''


