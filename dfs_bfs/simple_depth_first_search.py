'''
    Perform a depth first search and list all the node names, you should go left nodes in the beginning
'''
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        
		def dfs(node, visited, results):
			if not node:
				return
			
			results.append(node.name)
			visited.add(node)
			
			for child in node.children:
				if child not in visited:
					dfs(child, visited, results)
		
		visited = set()
		dfs(self, visited, array)
		return array
		
# 		Iterative approach
# 		stack = []
		
# 		stack.append(self)
# 		visited = set()
		
# 		while stack:
# 			node = stack.pop()
# 			visited.add(node)
# 			array.append(node.name)
# 			for i in range(len(node.children) -1, -1, -1):
# 				if node.children[i] not in visited:
# 					stack.append(node.children[i])
		
# 		return array
		

'''
    Their solution
    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            depthFirstSearch(child, array)

        return array
'''

