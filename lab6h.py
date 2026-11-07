# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Reina James
# Date: 6/11/2026
# Purpose: Use Dictionary for Structured Data.
# Usage: ./lab6h.py

# TO DO 1: Copy the code from lab6g.py and paste here.
# TO DO 2: Create function find_movie().
# TO DO 3: Call the function as instructed in readme.md file.
# TO DO 4: Run the script. Take screenshot of code and script.

def add_movie(database, name, director, year, runtime):

    movie = {"name":name, "director":director, "year":year, "runtime":runtime}
    database.append(movie)

def find_movie(database, search_word):

    results = []

    #convert search_word to all lower case and movie names to all lower case to find match
    for movie in database:
        if search_word.lower() in movie["name"].lower():
            results.append(movie)

    return results

def main():
    movie_database = []

    #add 4 movies
    add_movie(movie_database, "Princess Mononoke", "Hayao Miyazaki", 1997, 133)
    add_movie(movie_database, "A Miku Who Can't Sing", "Hiroyuki Hata", 2025, 110)
    add_movie(movie_database, "La La Land", "Damien Chazelle", 2016, 128)
    add_movie(movie_database, "Project Hail Mary", "Phil Lord, Chris Miller", 2026, 156)

    #find two different movies
    print("First search:", find_movie(movie_database, "miku"))
    print()
    print("Second search:", find_movie(movie_database, "hi"))

main()