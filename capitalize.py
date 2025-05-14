#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    parts = s.split(" ")
    ans =list()
    
    # Capitalize the first letter of each word, leaving numbers unchanged
    for part in parts:
        ans.append(part.capitalize())
    
    # Join the processed parts back into a string
    return " ".join(ans)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
