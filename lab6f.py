# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Reina James
# Date: 6/11/2026
# Purpose: Use Dictionary for Problem solving.
# Usage: ./lab5f.py

# TO DO 1: Create function histogram() as instructed in readme.md file. 
# TO DO 2: Create main() function and call histogram(). Call the main() function.
# TO DO 3: Run the script. Take screenshot of code showing the functions histogram() and main(). Also show output in the screenshot.

def histogram(sentence):

    letters = {}

    for ch in sentence:

        #if the letter is already in letters, increment value at that key
        if ch in letters:
            letters[ch] = letters[ch] + 1
        #if letter is not in letters, set value at that key to 1
        else:
            letters[ch] = 1

    #print amount of occurences of each key using stars
    for key,value in letters.items():
        print(key,"", value * "*")

def main():
    histogram("Python is fun")

main()