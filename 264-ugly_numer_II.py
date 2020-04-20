'''
    Write a program to find the n-th ugly number.

    Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

    Example:

    Input: n = 10
    Output: 12
    Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the 
    first 10 ugly numbers.


    1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20
    Note:  

    1 is typically treated as an ugly number.
    n does not exceed 1690.


    Brute force
    Go through each number, check if its prime factors only include 2, 3, 5
        add to an array, or increase counter,
        Return if we found the nth element
        
    Function -> 
        isUglyPrime -> Check and tell whether if its an ugly prime
        -> Find all the factors of the prime numbers.
        -> Check all divisors from 1 to n/2, if n is number.
'''

def uglyNumberDP(n):
    uglyPrimes = set()
    
    if n == 1:
        return 1

    uglyPrimes = set()
    uglyPrimes.add(1)
    i = 1

    while n > 1:
        i += 1
        if ((i / 2) in uglyPrimes) or ((i / 3) in uglyPrimes) or ((i / 5) in uglyPrimes):
            uglyPrimes.add(i)
            n -= 1
    
    print(uglyPrimes)
    return i

def uglyNumber(n):
    ugly = [1]
    idx_2 = 0
    idx_3 = 0
    idx_5 = 0

    for i in range(n):
        ugly2 = 2 * ugly[idx_2]
        ugly3 = 3 * ugly[idx_3]
        ugly5 = 5 * ugly[idx_5]

        next_ugly = min(ugly2, ugly3, ugly5)

        if next_ugly == ugly2:
            idx_2 += 1
        if next_ugly == ugly3:
            idx_3 += 1
        if next_ugly == ugly5:
            idx_5 += 1

        ugly.append(next_ugly)
    
    return ugly[-1]
        
        
# print(uglyNumberDP(11))

print(uglyNumber(11))
        





