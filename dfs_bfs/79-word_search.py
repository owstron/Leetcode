'''
    79. Word Search
    https://leetcode.com/problems/word-search/
    
    
    [20:00] found the solution but still fixing the bug.
    [35:00] found the final solution but, the final solution had a large complexity, review to reduce complexity.
    
    TimeComplexity:
        O(M*N * K)
            M is number of rows
            N is number of columns
            
    Space:
        O(K) where K is number of elements for recursion stack
        O(M*N) for the visited set, 
            
'''

import copy
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
            2 for loops for going through all the elements.
            If the element is first character of the word
                Do DFS
            else
                move to another element
                
                board =
                    [
                      ['A','B','C','E'],
                      ['S','F','C','S'],
                      ['A','D','E','E']
                    ]
                    
                    [
                      [C, A, A],
                      [A, A, A],
                      [B, C, D]
                    ]
                    
                    
                neighbos
                word_idx = 4  , C
                
                ABCCED
                
                [["A","B","C","E"],
                ["S","F","E","S"],
                ["A","D","E","E"]]
              
                "ABCEFSADEESE"

        '''
        
        def dfs(board, word, word_idx, cell, visited):
                
            visited.add(cell)
            
            if word_idx == len(word) - 1:
                return True
            
            word_idx += 1
            for neighbor in getNeighbors(board, cell, visited):
                if neighbor not in visited:
                    if board[neighbor[0]][neighbor[1]] == word[word_idx]:
                        if dfs(board, word, word_idx, neighbor, copy.deepcopy(visited)):
                            return True
                    
            return False
            
            
            
        def getNeighbors(board, cell, visited):
            moves = [(0,1), (1,0), (-1,0), (0,-1)]
            neighbors = []
            
            for move in moves:
                neighbor = (cell[0] + move[0], cell[1] + move[1])
                if 0 <= neighbor[0] < len(board) and 0 <= neighbor[1] < len(board[0]):
                    neighbors.append(neighbor)
            
            return neighbors
            
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(board, word, 0, (i, j), set()):
                        return True
        
        return False
                
        
        