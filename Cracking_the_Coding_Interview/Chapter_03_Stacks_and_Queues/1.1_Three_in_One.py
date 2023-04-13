# 3.1 Three in One: Describe how you could use a single array to implement three stacks. 
# Hints: #2, #12, #38, #58

# Note: the array size is limited and cannot be changed.

"""
two ways of solution:
1. Simple but with some limitations
    Divide the array to three parts and each of the stacks can work only in its area
    Cons:
        One stack can be full while others are almost empty
2. Harder but smarter
    stack start and end points will be flexible
    so that if one stack is full. other stacks can move to free space.
    So, the memory will be used to 100%
    Even the third stack is being full while first is empty.
    the stack should wrap around the list and continue in the start.
"""



