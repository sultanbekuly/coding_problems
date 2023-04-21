"""
Stack Min: How would you design a stack which, in addition to push and pop, 
has a function min which returns the minimum element? Push, pop and min should 
all operate in 0(1) time.
Hints:#27, #59, #78
"""

"""
56789 1234
    5    1
stack of mins..
"""

"""
We can (maybe) do a bit better than this by using an additional stack which keeps track of the mins.
"""
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.next_min = None

class StackMin:
    def __init__(self) -> None:
        self.top = None
        self.min = None

    def push(self, val):
        N = Node(val)
        N.next = self.top
        self.top = N
        
        if self.min == None or self.min.val > val:
            N.next_min = self.min
            self.min = N
            print("push - min - updated")
        
        
    def pop(self):
        if self.isEmpty():
            return None
        val = self.top.val
        if self.top == self.min:
            self.min = self.min.next_min
            print("pop - min - updated")
        self.top = self.top.next

        return val

    def peek(self):
        if self.isEmpty():

            return None
        val = self.top.val
        return val
    
    def peek_min(self):
        if self.isEmpty():
            return None
        min = self.min.val
        return min

    def isEmpty(self):
        return self.top == None

test = StackMin()

for i in range(5,9):
    test.push(i)
    print("test.peek():",test.peek() , "test.min:", test.peek_min())

for i in range(0,5):
    test.push(i)
    print("test.peek():",test.peek() , "test.min:", test.peek_min())

for i in range(12):
    print("pop:",test.pop() , "test.min:", test.peek_min())

#---------------------------------------------------------------------------

class Node2:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class StackMin2:
    def __init__(self) -> None:
        self.top = None
        self.min = None

    def push(self, val):
        N = Node2(val)
        N.next = self.top
        self.top = N
        
        if self.min == None or self.min.val >= val:
            M = Node2(val)
            M.next = self.min
            self.min = M
            print("push - min - updated")
        
        
    def pop(self):
        if self.isEmpty():
            return None
        val = self.top.val
        if val == self.min.val:
            self.min = self.min.next
            print("pop - min - updated")

        self.top = self.top.next
        return val

    def peek(self):
        if self.isEmpty():
            return None
        val = self.top.val
        return val
    
    def peek_min(self):
        if self.isEmpty():
            return None
        min = self.min.val
        return min

    def isEmpty(self):
        return self.top == None

test2 = StackMin2()

for i in range(5,9):
    test2.push(i)
    print("test.peek():",test2.peek() , "test.min:", test2.peek_min())

for i in range(0,5):
    test2.push(i)
    print("test.peek():",test2.peek() , "test.min:", test2.peek_min())

for i in range(12):
    print("pop:",test2.pop() , "test.min:", test2.peek_min())






