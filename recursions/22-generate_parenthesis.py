'''
[20:00] -- > Found the optimal exhaustive recursive solution




TimeComplexity:  O(B ^ N) where B is branching factor and N is the depth
                there its O(2 ^ N), because Branching factor 2, and N is the number of brackets required
Space: O(B^N) for each permutation.


Generate Paranthesis: https://leetcode.com/problems/generate-parentheses/

    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
                              (
                         /          \
                      / -            \
                  ((                        ()      
                 /  \                      / 
               /     \                   ()(            
            (((        (()               /   \      
             /      /      \          ()((    ()()
           ((()   (()(     (())     ()(())      ()()()
          
          ((())   (()())    (())()

         ((()))
              
             numOpens
             numClosed
         '''
        
        results = []
        
        def helper(numOpens, numClose, tempString):
            if numOpens == 0:
                if numClose == 0:
                    results.append(''.join(tempString))
                else:
                    tempString = tempString + [')'] * numClose
                    results.append(''.join(tempString))
                return
            
            
            if numOpens < numClose:
                helper(numOpens, numClose - 1, tempString + [')'])
            
            helper(numOpens - 1, numClose, tempString + ['('])
            
        helper(n-1, n, ['('])
        
        return results
                
                
            