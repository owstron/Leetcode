'''
Link: https://leetcode.com/problems/subsets/

[10:00] - Ideated, Brute force and recursive solution and Started coding the recursive solution
[16:00] - Solved recursive solution, with all output 

Solution comparision:
 Recurisive approach was same, drawback maximum depth of 1000
 
 Iterative approach, can go ounlimited depts

Clarifications
- empty set(), return the same
- Singleton, empty array and the same array
- Dulicates: Set so, no duplicates

Problem Solving
- Brute force
	- Multiple for loops, with increasing range to N
	- Size 1
		- Add each element into the array
	- Size 2:
		- Add two elements into the array
	- Size 3:
		- Triple loop, add thre elements into the array
	- Until size N
	
- Recrusion.
  - Initalize results with [[]]
  - For loop form left to right.
  	- Call recursive function with the current elem
		- Add curr_Elem to tempArray
		- Get another elem with tempArray
		- Add the next elem to tempArray
			- Add it to results.
		- If there exist element, call another element
		- until we reach end.
  
  Complexity: O(N * 2^N), N for first pass. 2^N foreach recursion
  Space: O(N * 2^N) for first pass, and 2^N for each recursion.
'''
def powerset(array):
    
	
	def recursion(tempArray, array, idx):
		'''
		[1, 2, 3]
		 ^
		[1],^
		    [1,2],^
			      [1,2,3]
		    [1, 3]
		    $
		'''
		tempArray.append(array[idx])
		results.append(tempArray)
		
		for j in range(idx+1, len(array)):
			recursion(tempArray[:], array, j)
		
	
	# results = [[]]
	# for idx in range(len(array)):
	# 	recursion([], array, idx)
	# return results
	
	########
	# iterative approach
	results = [[]]
	
	for elem in array:
		for i in range(len(results)):
			curr_subset = results[i]
			results.append(curr_subset + [elem])
			
	return results
			
	

		

