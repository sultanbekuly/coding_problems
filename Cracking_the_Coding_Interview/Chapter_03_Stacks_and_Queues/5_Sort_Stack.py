#Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
#an additional temporary stack, but you may not copy the elements into any other data structure
#(such as an array). The stack supports the following operations: push, pop, peek, and is Empty.
#Hints:# 15, #32, #43

#H#15
#One way of sorting an array is to iterate through the array and insert each element into
#a new array in sorted order. Can you do this with a stack?

##32
#Imagine your secondary stack is sorted. Can you insert elements into it in sorted order?
#You might need some extra storage. What could you use for extra storage?

##43
#Keep the secondary stack in sorted order, with the biggest elements on the top. Use the
#primary stack for additional storage.


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
    def __str__(self):
        arr = []
        node = self.top
        while( node != None ):
            arr.append( str(node.val) )
            node = node.next
        return "->".join(arr)
        

def sort_stack(s1:stack) -> stack:
    print("sort_stack:", s1)
    s2 = stack()
    while( not s1.isEmpty() ):
        val = s1.peek()
        while s2.isEmpty() and val > s2.peek():
            print("a")

def transferFromNewToOld(s1, s2):
    while( not ( self.stack_newest.isEmpty() ) ):
        self.stack_oldest.push( self.stack_newest.pop() )
        
        

    
stack1 = stack()

stack1.push(1)
stack1.push(2)
stack1.push(4)
stack1.push(3)
stack1.push(5)

print("stack1:", stack1)
sort_stack(stack1)


#for i in range(5):
#    my_stack.push(i) #0,1,2,3,4

#print(my_stack.isEmpty())
#print(my_stack.peek())

#for _ in range(5):
#    print("pop:", my_stack.pop())
#    print(my_stack.peek())

#print(my_stack.peek())
#print(my_stack.isEmpty())

