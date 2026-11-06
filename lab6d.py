# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Reina James
# Date: 6/11/2026
# Purpose: Creating dictionary.
# Usage: ./lab6d.py

# TO DO 1: Create function times_ten as instructed in readme.md file. 

def times_ten(start_index: int, end_index: int):
    my_dict = {}

    #for each key between start_index and end_index, multiply value by 10
    for num in range(start_index, end_index + 1):
        my_dict[num] = num * 10

    return my_dict

# TO DO 2: Run the script.

def main():
    dictionary = times_ten(2,6)

    print(dictionary)

main()