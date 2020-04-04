'''
Link: https://leetcode.com/problems/move-zeroes/
Given an array nums, write a function to move all 0's to 
the end of it while maintaining the relative order of the non-zero elements.


Seen second time
[10:00] -> Had a working brute force solution with O(N^2), found sliding window approach that was faster
[14:00] -> Completed a O(N) sliding window approach

Solution comparison




Clarifications:
- Duplicates?, handle same
- Empty, return same
- Singleton, return same.

Problem Solving:
- Sol1, Bruteforce:
    - Loop from left to right
    - If elem == 0:
        - pop-in place, and append to end
    
    Complexity: O(N * N) 
        O(N) for single pass
        O(N) for deletion, as we have to move the whole array
        
- Sol2, Sliding window:
    Complexity : O(N^2)
    - Use two pointer i, j
    - Loop from left to right, increasing j pointer
        - If elements != 0, swap the elements at i and j, increase i by 1
            - 
    [0, 0, 1, 2]
           ^     #swap
    [1, 0, 0, 2]
              ^  #swap
    [1, 2, 0, 0]
    
    [0, 0, 1, 2]
    
'''


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Sliding window
        i, j = 0, 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        
        return nums
        

#         # bruteforce:
#         numZerosSeen = 0
#         lenNums = len(nums)
#         i = 0
#         while i < lenNums - numZerosSeen:
#             if nums[i] == 0:
#                 nums.pop(i)
#                 nums.append(0)
#                 numZerosSeen += 1
#             else:
#                 i += 1
            
#         return nums
        