#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countPalindromes' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

'''
    Complexity = O(N^2) as we do a double loop
    
'''
def countPalindromes(s):
    lenString = len(s)
    result = 0
    for center in range(2*lenString - 1):
        left = center // 2
        right = left + center % 2
        while left >= 0 and right < lenString and s[left] == s[right]:
            result += 1
            left -= 1
            right += 1
    return result
if __name__ == '__main__':