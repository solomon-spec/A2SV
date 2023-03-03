#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(x, k):
    def kkk(n):
        if len(n) == 1: return n
        
        num = str(n)
        summ = 0
        for i in num:
            summ += int(i)
        return kkk(str(summ))
    numb = 0
    for i in x:
        numb += int(i)
    
    return kkk(str(numb*k))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
