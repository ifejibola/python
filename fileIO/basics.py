#** Data that's in main memory(RAM) is lost when a program ends. But data that's saved in files on disk is available the next time 
    #a program needs to access it.since this data persists across program restarts, this is known as persistent data storage.
#** A CSV( comma-seperated values) file is a type ofo file that stores multiple values per line, typically using commas to oseprate each value.

# HOW TO OPEN AND CLOSE A FILE

"""
** r - read : if the file doesn't exist, this mode causes a file not found error.
** w - write : if the file doesn't exist, this mode creates it. If the file already exists, this mode erases all existing data.
** a - append : if the file doesn't exist, this mode creates it. If the file already exists, this mode appends the data to the end of the file.
** b - binary : Use for binary files along with 'r' or 'w' mode.

## METHODS
** open(FILE, MODE) : Returns a file object for the specified file with the specified mode.
** close() : Closes the file, which ends all operations and frees all resources

"""

# How to open a file in write mode and close the file manually
outfile = open("test.txt", "w")
outfile.write("Testing")
outfile.close()

# How to use WITH statement to open and close files
    # code that opens a text file in write mode and automatically closes it
with open("test.txt", "w") as outfile:
    outfile.write("Testing using WITH statement")
    
    # Code that opens a text file in read mode and automatically closes it
with open("test.txt", "r") as infile:
    print(infile.readline())

"""

NOTE: If you don't specify a path for the file, the open() function uses the working directory, which is usually the same directory as the program.

"""


"""
** write(str)   : Writes the specified string to the file. If you want to start a new line, you must include the new line character

"""

# How to write one line to a text file
with open("members.txt", "w") as file:
    file.write("John cleese\n")

# How to append one line to a text file 
with open("members.txt", "a") as file:
    file.write("Eric Idle\n")           # John cleese
                                        # Eric Idle

# HOW TO READ A TEXT FILE
"""
THREE READ METHODS OF A FILE OBJECT

*** read()  : Reads the entire file and returns its contents as a string
*** readlines() : Reads the entire file and returns it as a list.
*** readline()  : Reads the next line in the file and return its contents as a string

"""

# How to use a FOR statement to read each line of the file
with open("members.txt") as file:
    for line in file:
        print(line, end="")
    print()

# How to read the entire file as a string
with open("members.txt") as file:
    contents = file.read()
    print(contents)

# How to read the entire file as a list
with open("members.txt") as file:
    members = file.readlines()
    print(members[0], end="")
    print(members[1])

# How to read each line of the file
with open("members.txt") as file:
    member1 = file.readline()
    print(member1, end="")
    member2 = file.readline()
    print(member2)


