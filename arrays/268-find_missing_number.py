'''
    Problem: 
    https://leetcode.com/problems/missing-number/
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
               
        # using Hashset
        setNums = set(nums)
        for i in range(len(nums)):
            if i not in setNums:
                return i
        return i + 1

        # Using XOR
        missing = len(nums)
        for idx, val in enumerate(nums):
            missing ^= (idx ^ val)
        return missing
        

        # Using expected value and actual value
        expected = 0
        actual = 0
        for i in range(len(nums)):
            actual += nums[i]
            expected += (i+1)
        return expected - actual