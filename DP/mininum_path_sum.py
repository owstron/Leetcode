'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

Solution:
    start elem1
    Perform DFS until you reach the end 
    have minPathSum
    if minPathSum < the current Path sum :
        update minPathSum.
    
Solution DP
    initalize, first row and first column
    For each cell it would min(grid[i-1][j], grid[i][j-1])
'''



def minPathSumDP(grid):
    cost_array = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    cost_array[0][0] = grid[0][0]
    
    # first row update
    for i in range(1, len(grid[0])):
        cost_array[0][i] = cost_array[0][i - 1] + grid[0][i]
    
    # first colum update
    for i in range(1, len(grid)):
        cost_array[i][0] = cost_array[i-1][0] + grid[i][0]
        
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            cost_array[i][j] = min(cost_array[i-1][j], cost_array[i][j-1]) + grid[i][j]
            
    return cost_array[-1][-1]
    
def minPathSumDPconstantSpace(grid):

    # first row update
    for i in range(1, len(grid[0])):
        grid[0][i] += grid[0][i-1]
    
    # first colum update
    for i in range(1, len(grid)):
       grid[i][0] += grid[i-1][0]
        
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
            
    return grid[-1][-1]
    
#Complexity: Time = O(M*N) where M is number of rows and N is number of cols
#  Space: O(1)




def bruteForce(grid):
    minPathSum = [float('inf')]

    def dfs(grid, cell, tempPathSum):
        tempPathSum += grid[cell[0]][cell[1]]
        if cell[0] < len(grid) -1:
            dfs(grid, [cell[0]+1, cell[1]], tempPathSum)
        
        if cell[1] < len(grid[0]) - 1:
            dfs(grid, [cell[0], cell[1]+1], tempPathSum)
        
        if cell[0] == len(grid) - 1 and cell[1] == len(grid[0]) - 1:
            if tempPathSum < minPathSum[0]:
                minPathSum[0] = tempPathSum
        
        return
                
    dfs(grid, [0,0], 0)
    return minPathSum[0]
            
    

grid1 = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
# print(minPathSum(grid1)) #7
print(bruteForce(grid1)) #
