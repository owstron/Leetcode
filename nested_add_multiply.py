'''
    Create a Lisp-like interpreter for basic arithmetic operations.

    Support add/sub/mul/div, and given an input like ( add ( sub 3 2 ) ( div 4 2 ) ) 
    output the result computing all the operations.

Assume that the tokens are all space separated and inputs are always valid
'''

def lispInterpreter(token):
    stack = []

    tokens = token.split(' ')

    for token in tokens:
        if token == '(':
            continue
            
        if token == ')':
            val2 = stack.pop()
            val1 = stack.pop()
            operation = stack.pop()
            stack.append(helper(operation, int(val1), int(val2)))
        
        else:
            stack.append(token)

    return stack[-1]



def helper(operation, val1, val2):
    if operation == 'add':
        return val1 + val2
    elif operation == 'mul':
        return val1 * val2
    elif operation == 'div':
        return val1 / val2
    elif operation == 'sub':
        return val1 - val2

    return None

print(lispInterpreter('( add ( sub 3 2 ) ( div 4 2 ) )'))
