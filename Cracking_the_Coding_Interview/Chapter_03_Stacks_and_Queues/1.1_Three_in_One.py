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
"""
Hints:
#2: A stack is simply a data structure in which the most recently added elements are
removed first. Can you simulate a single stack using an array? Remember that there are
many possible solutions, and there are tradeoffs of each.
#12: We could simulate three stacks in an array by just allocating the first third of the array to
the first stack, the second third to the second stack, and the final third to the third stack.
One might actually be much bigger than the others, though. Can we be more flexible
with the divisions?
#38: If you want to allow for flexible divisions, you can shift stacks around. Can you ensure
that all available capacity is used?
#58: Try thinking about the array as circular, such that the end of the array "wraps around"to
the start of the array.
"""

import math

class stackNode():
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class stackThreeInOne():
    def __init__(self, arr_size) -> None:
        self.arr_stack = [None for _ in range(arr_size) ]

        self.stack_start = [0 for _ in range(3)]
        self.stack_end = [0 for _ in range(3)]
        self.stack_top = [0 for _ in range(3)]

        self.stack_start[0] = 0
        self.stack_end[0] = math.floor((arr_size-1)/3)

        self.stack_start[1] = self.stack_end[0] + 1
        self.stack_end[1] = math.floor(2*((arr_size-1)/3))
        
        self.stack_start[2] = self.stack_end[1] + 1
        self.stack_end[2] = arr_size-1

        self.stack_top[0] = None
        self.stack_top[1] = None
        self.stack_top[2] = None

        #print(self.arr_stack)
        for i in self.stack_start:
            print("self.stack_start:",i)
        for i in self.stack_end:
            print("self.stack_start:",i)
        for i in self.stack_top:
            print("self.stack_start:",i)

    def push(self, arr_num, val): #arr_num 0/1/2
        #if stack top+1 is equal to start of next one, then we need to move to one cell the next stack

        stack_top_index = self.stack_top[arr_num]
        if stack_top_index == None:                     #None -> place to 0
            self.stack_top[arr_num] = self.stack_start[arr_num] #stack top initialization
            self.arr_stack[ self.stack_top[arr_num] ] = val
        else:
            self.arr_stack[ stack_top_index + 1 ] = val  #0/1 -> place to 1/2
            self.stack_top[arr_num] += 1

        
    def pop(self, arr_num):
        stack_top_index = self.stack_top[arr_num]
        if(stack_top_index == None):
            return None

        val = self.arr_stack[ stack_top_index ]
        self.arr_stack[ stack_top_index ] = None
        self.stack_top[arr_num] -= 1                            #this one should be checked for array wrapping
        if self.stack_top[arr_num] < self.stack_start[arr_num]:
            self.stack_top[arr_num] = None
        return val
    #def peek(self):
    #    if(self.top == None):
    #        return None
    #    return self.top.val
    #def isEmpty(self):
    #    return self.top == None
        
stackTiO = stackThreeInOne(15)
#0 4 5 9 10 14

for i in range(3):
    stackTiO.push(0,i)
    stackTiO.push(1,i)
    stackTiO.push(2,i)
print("stackTiO.arr_stack:",stackTiO.arr_stack )

for i in range(4):
    print("pop:",stackTiO.pop(0))
    print("pop:",stackTiO.pop(1))
    print("pop:",stackTiO.pop(2))
    print("stackTiO.arr_stack:",stackTiO.arr_stack )



#stackTiO = stackThreeInOne(10)
#stackTiO = stackThreeInOne(100)
#stackTiO = stackThreeInOne(3)
#0 3    4 6     7 9
#0 33   34 66   67 99
#0 0    1 1     2 2
#stacks start end



