'''
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.
'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        
        if not self.minStack:
            self.minStack.append(x)
        elif self.minStack[-1] >= x:
            self.minStack.append(x)

    def pop(self) -> None:
        if self.stack:
            lastElem = self.stack.pop()
            
            if lastElem == self.minStack[-1]:
                self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()