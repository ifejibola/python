# MORE LIST METHODS
"""
count(item) : Returns the number of occurrences of an item in the list. If the item isn't found in tihe list, this method returns 0

reverse(list) : Reverses the order of the items in the list.
sort([key=function]) : Sorts the list items in place. The optional key argument specifies a function to be called on each item before sorting

"""

# Built-in function for sorting the items in a list

"""
sorted(list[, key=function]) : Returns a new list consisting of the sorted items of the original list. The optional key argument specifies a function to be called on each item before sorting.

"""

# How to use the count(), reverse(), and sort() methods
numlist = [5, 15, 84, 3, 14, 2, 8, 10, 14, 25]
count = numlist.count(14)       # count = 2
numlist.reverse                 # [25, 14, 10, 8, 2, 14, 3, 84, 15, 5]
numlist.sort                    # [2, 3, 5, 8, 10, 14, 14, 15, 25, 84]

# How to use the sort() method with mixed-case lists
# What happens in a simple sort
foodlist = ["orange", "apple", "Pear", "banana"]
foodlist.sort()         # ["Pear", "apple", "banana", "orange"]

#How to use the key argument to fix the sort order
foodlist.sort(key=str.lower)

# result : ["apple", "banana", "orange", "peach", "Pear"]

# How to use the sorted() function with mixed-case lists
    # What happens in a simple sort
foodlist = ["orange", "apple", "Pear", "banana"]
sorted_foodlist = sorted(foodlist)
print(sorted_foodlist)          # ["Pear", "apple", "banana", "orange"]

"""
** min(list)   : Returns the minimum value in the list
** max(list)    : Returns the maximum value in the list.

"""

#Two function of the random module that work with lists
"""
** choice(list)     : Returns a randomly selected item from the list.
** shuffle(list)    : Shuffles the items in the list on a random basis.

"""

# How to use the min() and max() functions 
numlist = [5, 15, 84, 3, 14, 2, 8, 10, 14, 25]
minimum = min(numlist)          # 2
maximum = max(numlist)          # 84

# How to use the choice() and shuffle() functions
import random
numlist = [5, 15, 84, 3, 14, 2, 8, 10, 14]
choice = random.choice(numlist)                 # Returns random item from numlist
random.shuffle(numlist)                         # shuffles numlist items randomly

# How to copy, slice, and concatenate lists
"""
deepcopy(list) : Returns a deep copy of the list. The deep copy is a separate list with no relation to the original list.
"""

#How to make a shallow copy of a list
list_one = [1, 2, 3, 4, 5]
list_two = list_one
list_two[1] = 4
print(list_one)     #[1, 4, 3, 4, 5]
print(list_two)     #[1, 4, 3, 4, 5]

# How to make a deep copy of a list
import copy
list_one = [1, 2, 3, 4, 5]
list_two = copy.deepcopy(list_one)      # [1, 2, 3, 4, 5]
list_two[1] = 4
print(list_one)                         #[1, 4, 3, 4, 5]
print(list_two)                         #[1, 4, 3, 4, 5]

#How to slice a list
    #Code that slices witht he start and end arguments
"""
*** If you only want to supply start and end arguments, you only need to code one colon
*** If you want to start slicing at the beginning of the list, you can omit the start argument.
*** Or if you want to continue slicing to the end of the list, you can omit the end argument
"""
numbers = [52, 54, 56, 58, 60, 62]
numbers[0:2]            # [52, 54]
numbers[:2]             # [52, 54]
numbers[4:]             # [60, 62]

#Code that slices with the step argument
numbers[0:4:2]          # [2, 6]
numbers[::-1]           # [62, 60, 58, 56, 54, 52]

# How to concatenante two lists with the + and += operators
inventory = ["staff", "robe"]
chest = ["scroll", "pestle"]
combined = inventory + chest        # ["staff", "robe", "scroll", "pestle"]
print(inventory)                    # ["staff", "robe"]
inventory += chest                  # ["staff", "robe", "scroll", "pestle"]
print(inventory)                    # ["staff", "robe", "scroll", "pestle"]




