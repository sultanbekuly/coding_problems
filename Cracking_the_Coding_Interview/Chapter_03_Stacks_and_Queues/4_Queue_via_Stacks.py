"""
Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
Hints: #98, #114

#98
The major difference between a queue and a stack is the order of elements. A queue
removes the oldest item and a stack removes the newest item. How could you remove
the oldest item from a stack if you only had access to the newest item?
--
Maybe second stack should be reversed..

#114
We can remove the oldest item from a stack by repeatedly removing the newest item
(inserting those into the temporary stack) until we get down to one element. Then, after
we've retrieved the newest item, putting all the elements back. The issue with this is
that doing several pops in a row will require O ( N) work each time. Can we optimize for
scenarios where we might do several pops in a row?
"""

#stack_newest
#stack_oldest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        N = Node(val)
        N.next = self.top
        self.top = N

    def pop(self):
        if self.isEmpty():
            return None
        val = self.top.val
        self.top = self.top.next
        return val

    def peek(self):
        if self.isEmpty():
            return None
        return self.top.val

    def isEmpty(self) -> bool:
        return self.top == None
        
    def __str__(self):
        arr = []
        node = self.top
        while( node != None ):
            arr.append( str(node.val) )
            node = node.next
        return "->".join(arr)



class MyQueue:
    def __init__(self):
        self.stack_newest = Stack() #always newest on the top - push to here
        self.stack_oldest = Stack() #always oldest on the top - pop from here

    def push(self, val):
        self.stack_newest.push(val)

    def pop(self):
        if(self.isEmpty()):
            return None
        
        if self.stack_oldest.isEmpty():
            #transfer from stack_newest to oldest
            self.transferFromNewToOld()

        return self.stack_oldest.pop()

    def peek(self):
        if(self.isEmpty()):
            return None

        if self.stack_oldest.isEmpty():
            #transfer from stack_newest to oldest
            self.transferFromNewToOld()

        return self.stack_oldest.peek()

    def isEmpty(self) -> bool:
        return  self.stack_newest.isEmpty() and self.stack_oldest.isEmpty()

    def transferFromNewToOld(self):
        while( not ( self.stack_newest.isEmpty() ) ):
            self.stack_oldest.push( self.stack_newest.pop() )

test = MyQueue()


for i in range(5):
    test.push(i)
    #print("stack_newest.top:", test.stack_newest.top.val, "stack_oldest.top:",test.stack_oldest.top )
    print("stack_newest:", test.stack_newest, "stack_oldest:",test.stack_oldest )

for _ in range(7):
    print("pop:", test.pop())
    print("stack_newest:", test.stack_newest, "stack_oldest:",test.stack_oldest )

print("---------------------------------------------------------------------------------------------------------")

for i in range(5):
    test.push(i)
    #print("stack_newest.top:", test.stack_newest.top.val, "stack_oldest.top:",test.stack_oldest.top )
    print("stack_newest:", test.stack_newest, "stack_oldest:",test.stack_oldest )

for _ in range(2):
    print("pop:", test.pop())
    print("stack_newest:", test.stack_newest, "stack_oldest:",test.stack_oldest )

for i in range(5):
    test.push(i)
    #print("stack_newest.top:", test.stack_newest.top.val, "stack_oldest.top:",test.stack_oldest.top )
    print("stack_newest:", test.stack_newest, "stack_oldest:",test.stack_oldest )

for _ in range(10):
    print("pop:", test.pop())
    print("stack_newest:", test.stack_newest, "stack_oldest:",test.stack_oldest )