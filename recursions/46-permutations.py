'''
    Link: https://leetcode.com/problems/permutations/
'''

'''
Start[0:00]

[10:00] -> Had a bruteforce solution that I was dry-testing.
[17:00] -> Had a solution, error in one test case, did not handle
		  the single num array and empty array well.
[20:00] -> submitted a working solution without error.

Solution comparison:
O(N*N!) solution because, I have to check every element and recurse.
The solution were cleaner with less if conditions, for base checks as 
the recursion functions were already checking for it.
Added two conditions for if, instead of two different checks.
Instead of checking len(arra) == 1, used if array, for boolean check.
Done additional useless checks for combining arrays,
	arr[i:], will return [] if i >= len(array)


Clarifications
	- Unique integers (no repetitions)
	- If empty return empty array.

Problem solving:
	SOL1:
	- Initialize the lists
	- Mutiple for loops.
	- Go left to right:
		- Pick an element -
		- store the element in tempArray
		- recurse the same step by passing elements except the choosen elements
		- Pass the tempArray
	- Base case
		- If the array is length == 1, or length  -1
		- Add the number to tempArray
		- add the TempArray to the results Array
		
	Time complexity: O(N*N!)
	Space complexity: O(N*N!) 
	where N is the length of the input array
	
	
	results = [[1,2,3], [1,3,2],[2,1,3],[2,3,1],
	[1, 2, 3]
	 ^ [2, 3]
	    ^  3
	   [2, 3]
	   	2  ^
	[1, 2, 3]
	    ^ [1, 3]
	       ^  3
	      [1, 3]
	   	   1  ^
	[1, 2, 3]
	 ^ [2, 3]
	    ^  3
	   [2, 3]
	   	2  ^

'''

def getPermutations(array):
    results = []
	tempArray = []
	
	def getPermutationsRecursion(tempArray, array):
		if not array and tempArray:
			results.append(tempArray)
			return
	
		for i in range(len(array)):
			getPermutationsRecursion(tempArray + [array[i]], 
									 array[:i] + array[i+1:])

		return
	
	getPermutationsRecursion(tempArray[:], array)
	
	return results
	
	
    