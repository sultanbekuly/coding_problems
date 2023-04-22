"""
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, 
it might topple. Therefore, in real life, we would likely start a new stack when 
the previous stack exceeds some threshold. Implement a data structure SetOfStacks 
that mimics this. SetO-fStacks should be composed of several stacks and should 
create a new stack once the previous one exceeds capacity. SetOfStacks. push() and 
SetOfStacks. pop() should behave identically to a single stack (that is, pop() should 
return the same values as it would if there were just a single stack).
FOLLOW UP
ImplementafunctionpopAt(int index)whichperformsapopoperationonaspecificsub-stack.
Hints:#64, #87
"""

class stack_node():
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class stack():
    def __init__(self) -> None:
        self.top = None
    def push(self, val):
        T = stack_node(val)
        T.next = self.top
        self.top = T
    def pop(self):
        if(self.top==None):
            return None
        T = self.top
        self.top = self.top.next 
        return T.val
    def peek(self):
        if(self.top == None):
            return None
        return self.top.val
    def isEmpty(self):
        return self.top == None
        
#123..789 10 
#11 .. 19 20

class SetOfStacks():
    def __init__(self, stack_size) -> None:
        self.stack_size = stack_size
        self.counter = 0
        self.superStackTop = None 
        self.top = None


    def push(self, val):
        if( self.counter == self.stack_size):
            self.counter = 0            # reset 






    
# my_stack = stack()

# for i in range(5):
#     my_stack.push(i) #0,1,2,3,4

# print(my_stack.isEmpty())
# print(my_stack.peek())

# for _ in range(5):
#     print("pop:", my_stack.pop())
#     print(my_stack.peek())

# print(my_stack.peek())
# print(my_stack.isEmpty())
