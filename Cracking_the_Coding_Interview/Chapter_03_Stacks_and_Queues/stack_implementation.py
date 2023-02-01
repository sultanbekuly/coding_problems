# Stack uses LIFO (last-in first-out) ordering.
# pop(): Remove the top item from the stack
# push(item): Add an item to the top of the stack
# peek(): Return the top of the stack
# is Empty (): Return true if and only if the stack is empty

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
        
    
my_stack = stack()

for i in range(5):
    my_stack.push(i) #0,1,2,3,4

print(my_stack.isEmpty())
print(my_stack.peek())

for _ in range(5):
    print("pop:", my_stack.pop())
    print(my_stack.peek())

print(my_stack.peek())
print(my_stack.isEmpty())
