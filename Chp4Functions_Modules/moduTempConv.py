# The conver Temparature program
#Using/importing a Module


import temperature as temp

def display_menu():
    print("Menu")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print()

def convert_temp():

    option = int(input("Enter a menu option: "))
    if option == 1:
        f = int(input("Enter degree Fahrenheit"))
        c = temp.to_celsius(f)
        c = round(c, 2)
        print("Degrees Celsius:", c)
    elif option == 2:
        c = int(input("Enter defrees Celsius:"))
        f = temp.to_fahrenheit(c)
        f = round(f, 2)
        print("Degrees Fahrenheit:", f)
    else:
        print("You must enter a valid menu number.")


def main():
    display_menu()
    again = "y"
    while again.lower() == "y":
        convert_temp()
        print()
        again = input("Convert another temparature? (y/n): ")

if __name__ == "__main__":
    main()
