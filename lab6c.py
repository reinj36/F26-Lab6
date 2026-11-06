# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Reina James
# Date: 6/11/2026
# Purpose: Practice Set Operations.
# Usage: ./lab6c.py

# TO DO 1: Copy the code from lab5b.py and paste here.
# TO DO 2: Create the function s3_and_s5_not_s7().
# TO DO 3: Run the script. Take screenshot of only s3_and_s5_not_s7() function. No need to capture main() in the screenshot. Make sure you show the output in the screenshot.

def buildtheSet(divisor):
    # Complete this function

    numbers = set()

    #add i to numbers if divisible by divisor
    for i in range(1, 101):
        if i % divisor == 0:
            numbers.add(i)
    return numbers

def s3_or_s5(s3, s5):

    only_s3 = s3.difference(s5)
    only_s5 = s5.difference(s3)
	
    common_set = s3.intersection(s5)
    result_set = (only_s3.union(only_s5)).difference(common_set)

    return result_set

def main():

    s3 = buildtheSet(3)
    print("s3: ", s3)
    print("----------------------------------------")

    s5 = buildtheSet(5)
    print("s5: ", s5)
    print("----------------------------------------")

    new_s3_s5 = s3_or_s5(s3, s5)

    print("New set: ", new_s3_s5)

main()