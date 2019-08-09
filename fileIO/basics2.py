#How to work with a list in a text file
    # How write the items in a list to a file
members = ["John Cleese", "Erric Idle"]
with open("members.txt", "w") as file:
    for m in members:
        file.write(m + "\n")        # Adds new line character

# How to read the lines in a file into a list
members = []
with open("members.txt") as file:
    for line in file:
        line = line.replace("\n", "")       # removes new line character 
        members.append(line)
print(members)                              # ["John Cleese", "Eric Idle"]

# How to write the item in a list to a file
years = [1975, 1979, 1983]
with open("years.txt") as years_file:
    for year in years:
        years_file.write(str(year) + "\n") # Converts int to str

# How to read the items in a list from a file
years = []
with open("years.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        years.append(int(line))             # convers str to int
print(years)                                # [1975, 1979, 1983]


