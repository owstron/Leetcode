'''
From AlgoExpert: Link: https://www.algoexpert.io/questions/Lowest%20Common%20Manager

Similar to https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

'''

'''
[10:00] -> Started coding the solution. 
			Wasted time to figure out how input is passed.
			
[20:00] -> Found solution, with bugs
[28:00] -> found solution that solved all the code.
[43:00] -> found solution with optimization that found both nodes in single pass

Compelxity:
	Time: O(N) + O(N),
		O(N) for comparing the paths
		O(N) for checking every nodes
	
	Space: O(N)*2 for two paths

Solution comparison
- Instead of finding two paths, they are directly finding the actual common ancestor
- A external variable to check if both reports are found
- If reports, found, tehn the current manager it the LCM




Clarification:
 - Both nodes in the tree?
 - Tree empty ?
 - If the one node is parent of other, parent is the common node
 
Problem Solving
Solution 1:
	Two_arrays to store the path of each node.
	
	- Traverse, In-Order, and record the node
	- Check left node == target Node, return
		Else: leftnode = Root, and traverse
	- Check right node == target Node
		Else: rightnode = Root and traverse.
	- If node found return the whole path
	
	Do the same for the other report.
	Loop through both paths, until the paths diverge.
	

Issues:
 - Duplications doing the tree swipes twice.
	
 
'''
def getLowestCommonManager(topManager, reportOne, reportTwo):
    
	paths = {
		reportOne.name: [],
		reportTwo.name: []
	}
	
	def findNode(root, reportOne, reportTwo, path):
		path.append(root)
	
		if paths[reportOne.name] and paths[reportTwo.name]:
			return	
		
		if root == reportOne:
			paths[reportOne.name] = path
		elif root == reportTwo:
			paths[reportTwo.name] = path
		
		for node in root.directReports:
			findNode(node, reportOne, reportTwo, path[:])
			
	findNode(topManager, reportOne, reportTwo, [])
	print(paths)
	
	i = 0
	for i in range(min(len(paths[reportOne.name]), len(paths[reportTwo.name]))):
		if paths[reportOne.name][i] != paths[reportTwo.name][i]:
			i -= 1
			break
	
	
	return paths[reportOne.name][i]
			