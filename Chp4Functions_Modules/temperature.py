# Modules
# USE: file that contains reusable code like functions
# To create module store one or more functions in py file
# Convert fahrenheit to celsius
# Convert celsius to fahrenheit

"""
This module contains functions for converting temparature between degrees Fahrenheit 
and degrees Celsius 
"""

def to_celsius(fahrenheit):
    """
    Accepts degrees in Fahrenheit (fahrenheit argument)
    returns defrees Celsius
    """
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def to_fahrenheit(celsius):
    """
    Accepts defrees Celsius(celsius argument)
    Returns degrees Fahrenheit
    """
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


def main():
    for temp in range(0, 212, 40):
        print(temp, "Fahrenheit =", round(to_celsius(temp)), "Celsius")

    print()

    for temp in range(0, 100, 20):
        print(temp, "Celsius =", round(to_fahrenheit(temp)), "Fahrenheit")


if __name__ == "__main__":
    main()
