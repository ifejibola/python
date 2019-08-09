# Codes that creates lists

temps = [48.0, 30.5, 20.2, 100.0, 42.0]  # 5 float values
inventory = ["Staff", "hat", "shoes"]  # 3str values
movie = ["The Holy Grail", 1975, 9.99]  # str, int, and float values
test_scores = []

# Repetition operator (*) to create list
scores = [0] * 5  # test scores = [0,0,0,0,0]

# How to get items from a list
temps = [48.0, 30.5, 20.2, 100.0, 42.0]
temp = temps[0]  # temp = 48.0
temp = temps[4]  # temp = 42.0
temp = temps[5]  # IndexError: index out of range


# How to add and remove items

""" 
** append(item) : Appends the specified item to the end of the list, Increases the length of the list by one.
** insert(index, item) : Inserts the specified item at the specified index. This increases the length of the list by one and shits all items after the specified index back by one index.
** remove(item) : Removes the first item in the list that is equal to the specified item. This decreases the length of the list by one and shifts all items after the found item's index forward. If item isn't found, this method raises a ValueError 
** index(item) : Returns the index of the first occurrence of the specified item in the list. If the item isn't found, this method raises a ValueError.
** pop([index]) : If no index argument is specified, this method gets the last item from the list and removes it. Otherwise, this method gets the item at the specified index and removes it.

"""

# How to use the append(), insert, and remove methods

stats = [48.0, 30.5, 20.2, 100.0]
inventory = ["Staff", "hat", "shoes", "bread", "potion"]

stats.append(99.5)  # stats = [48.0, 30.5, 20.2, 100.0, 99.5]
inventory.insert(
    3, "robe"
)  # inventory = ["Staff", "hat", "shoes", "robe", "bread", "potion"]
inventory.remove("shoes")  # inventory = ["Staff", "hat", "robe", "bread", "potion"]

# How to use pop method
inventory = ["staff", "hat", "robe", "bread"]
item = inventory.pop()  # item = "bread"
# inventroy = ["staff", "hat", "robe"]
item = inventory.pop(1)  # item = "hat"
# inventory = ["staff", "robe"]

# How to remove an item by using the index() and pop() methods
inventory = ["staff", "hat", "robe", "bread"]
i = inventory.index("hat")  # i = 1
inventory.pop([i])  # inventory = ["Staff", "robe", "bread"]
"""
    len(list) : Returns the length of the list, which is the number of items in the list.
"""
# How to use IN keyword to check whether an item is in a list
inventory = ["staff", "hat", "bread", "potion"]
item = "bread"
if item in inventory:
    inventory.remove(item)      # inventory = ["staff", "hat", "potion"]
print(inventory) # ['staff', 'hat', 'potion']

#print each item in a list
for items in inventory:
    print (items)           #staff
                            #hat
                            #potion

#Process the items in a list
    #With a for loop
scores = [70, 80, 90, 100]
total = 0
for score in scores:
    total +=score
print(total)        # total =340

    # With a while loop
scores = [70, 80, 90, 100]
total = 0
i = 0
while i < len(scores):
    total += scores[i]
    i+=1
print(total)        # total = 340

# Four immutable types 
"""
str
int 
float
bool

"""
#One mutable type
"""
list
"""
#How to work with arguments of the immutable type
    #The double_the_number() function
def double_the_number(value):
    value = value * 2       # A new int object is created
    return value            # The new int object must be returned 

value1 = 25         # An int object is created 
value2 = double_the_number(value1) 
print(value1)   # 25
print(value2)   # 50

# How to work with argument of the mutable type
    # The add_to_list() function
def add_to_list(list, item):
    list.append(item)       # The list object is changed

inventory = ["staff", "hat", "bread"]   # list object is created 
add_to_list(inventory, "robe")          
print(inventory)                        # ["staff", "hat", "bread", "robe"]
