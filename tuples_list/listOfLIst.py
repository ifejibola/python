movies = [["Joel", 85, 95, 70], ["Anne", 95, 100, 100], ["Mike", 77, 70, 80, 85]]


# How to define a list of lists

movies = [
    ["The Holy Grail", 1975, 9.99],
    ["Life of Brian", 1979, 12.30],
    ["The Meaning of Life", 1983, 7.50],
]

# How to add to a list of lists through programming
movies = [["The HolyGrail", 1975], ["Life of Brain", 1979]]

movie = []  # Create empty list for next movie
movie.append("The Meaning of Life")  # Add movie name to movie list
movie.append(1983)  # Add movie year to movie list
movie.append(7.5)  # Add movie price to movie list
movies.append(movie)  # Add movie list to movies list

# How to access the items int he lit of movies
movies[0][0]  # "The Holy Grail"
movies[0][2]  # 9.99
movies[0][3]  # IndexError: index out of range
movies[1][0]  # "Life of Brain"

# Print a two-dimensional list
[
    ["The Holy Grail", 1975, 9.99],
    ["Life of Brain", 1979, 12.3],
    ["The Meaning of Life", " 1983", 7.5],
]

# How to loop through the rows and columns of a 2-dimensional list
for movie in movies:
    for item in movie:
        print(item, end=" | ")
    print()
