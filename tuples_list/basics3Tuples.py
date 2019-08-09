# Code that creates tuples
    # a tuple of 5 floating-point numbers
stats = (48, 30.5, 20.2, 100.0, 48.0)

# a tuples of 6 strings
herbs = ("lavender", "pokeroot", "chamomile", "valerian", "nettles", "oatstraw")

# a tuple that stores the data for a movie
movie = ("Monty Python and the Holy Grail", 1975, 9.99)

# Code that accesses items in a tuple 
herbs[0]            # lavender
herbs[-1]           # oatstraw
herbs[1:4]          # ('pokeroot', 'chamomile', 'valerian')

herbs[1] = "red clover"
# TypeError: 'tuple' object does not support item assignment 

# Code that unpacks a tuple
tuple_values = (1, 2, 3)
a, b, c, = tuple_values     # a = 1, b = 2, c = 3

# A function that returns a tuple
def get_location():
    # the code that computes the values for x, y, and z goes here 
    return x, y, z

# Code that calls the get_location() function and unpacks the returned tuple
x, y , z = get_location()

