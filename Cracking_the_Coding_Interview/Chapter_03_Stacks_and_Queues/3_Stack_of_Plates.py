"""
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, 
it might topple. Therefore, in real life, we would likely start a new stack when 
the previous stack exceeds some threshold. Implement a data structure SetOfStacks 
that mimics this. SetO-fStacks should be composed of several stacks and should 
create a new stack once the previous one exceeds capacity. SetOfStacks. push() and 
SetOfStacks. pop() should behave identically to a single stack (that is, pop() should 
return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.
Hints:#64, #81
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
    def __init__(self, threshold) -> None:
        self.threshold = threshold
        self.counter = 0
        #self.superStackTop = None 
        self.top = None
        self.arr = []
        self.topStack = stack() #None
        self.arr.append( self.topStack )
        #self.arr.append( [self.top ,counter] )



    def push(self, val):
        if( self.counter == self.threshold):        #counter exceed threshold
            self.counter = 0            # reset 
            self.topStack = None
            #self.arr.append( [self.top ,counter] )
            self.topStack = stack()     #Create new stack
            self.arr.append( self.topStack )

        self.topStack.push(val)
        self.counter += 1

    def pop(self):
        if self.isEmpty():
            return None
        val = self.topStack.pop()
        self.counter -= 1               #double check it
        #print("self.isEmpty():", self.isEmpty())
        #print("len(self.arr)>1", len(self.arr)>1)
        if self.isEmpty() and len(self.arr)>1 : 
            print("if self.isEmpty() and len(self.arr)>1 : ")
            self.arr.pop()
            self.topStack = self.arr[-1]
            self.counter = self.threshold
        return val

    def peek(self):
        if self.isEmpty():
            return None
        return self.topStack.peek()

    def isEmpty(self):
        return self.topStack.isEmpty()


        

test  = SetOfStacks(5)

for i in range(1,15):
    test.push(i)
    print("self.counter:", test.counter, "self.topStack.peek():",test.topStack.peek(), "self.arr:", test.arr)

for i in range(17):
    print("test.pop:", test.pop() )
    print("self.counter:", test.counter, "self.topStack.peek():",test.topStack.peek(), "self.arr:", test.arr)


for i in range(1,5):
    test.push(i)
    print("self.counter:", test.counter, "self.topStack.peek():",test.topStack.peek(), "self.arr:", test.arr)

for i in range(3):
    print("test.pop:", test.pop() )
    print("self.counter:", test.counter, "self.topStack.peek():",test.topStack.peek(), "self.arr:", test.arr)

for i in range(5,10):
    test.push(i)
    print("self.counter:", test.counter, "self.topStack.peek():",test.topStack.peek(), "self.arr:", test.arr)



#FOLLOW UP
#Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.
"""
we can implement it by adding count parameter for array which stores the sub-stacks
or we can make so that the substack will store its counts

It is imported to discuss and get trade-offs with interviewer
(There can be a need to keep all stacks in full capacity)
"""



