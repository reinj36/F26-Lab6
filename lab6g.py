# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Reina James
# Date: 6/11/2026
# Purpose: Use Dictionary for Structured Data.
# Usage: ./lab6g.py

# TO DO 1: Create function add_movie(). 
# TO DO 2: Call the function 4 times.
# TO DO 3: Print the database as instructed in readme.md file.
# TO DO 4: Run the script. Take screenshot of code and script.

def add_movie(database, name, director, year, runtime):

    #initialize values with values from method call and append movie to movie database
    movie = {"name":name, "director":director, "year":year, "runtime":runtime}
    database.append(movie)

def main():
    movie_database = []

    #add 4 movies
    add_movie(movie_database, "Princess Mononoke", "Hayao Miyazaki", 1997, 133)
    add_movie(movie_database, "A Miku Who Can't Sing", "Hiroyuki Hata", 2025, 110)
    add_movie(movie_database, "La La Land", "Damien Chazelle", 2016, 128)
    add_movie(movie_database, "Project Hail Mary", "Phil Lord, Chris Miller", 2026, 156)

    #print all movies in database
    for movie in movie_database:
        print(movie)

main()