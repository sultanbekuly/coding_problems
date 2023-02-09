# 3.1 Three in One: Describe how you could use a single array to implement three stacks. 
# Hints: #2, #12, #38, #58

# the stack same as array has pop function which deletes last item
# first idea is to allocate array so that first item will be used by first stack
#   second item for second stack and thrid item for third stack
#   and then it repeats again and again
# additionally we can have three variables which will store last added index for each stack

# pop(): Remove the top item from the stack
#   we will set it to None and update its index variable accordingly
# push(item): Add an item to the top of the stack
#   get ToBe index based on current index
#   check if it available by compating with the array len
#   if not add three None items
#   then update by ToBe index
# peek(): Return the top of the stack
#   it can be easily extracted by using the index variables
# is Empty ():
#   if index negative number then True else False

# This solution is optimal for time but not for memory

#There is better solution
#   to allocate for each stack only one array item
#   [[0],[0,1,2,3],[0,1,2,3,4,5,6]]
#   [[],[],[]] initialization

class ThreeInOne():
    def __init__(self) -> None:
        self.arr = []
        self.ind = [-3,-2,-1]
        # self.ind_f = -3
        # self.ind_s = -2
        # self.ind_t = -1
    def pop(self, stack_num:int): #stack_num = 0/1/2
        if(not(stack_num in [0,1,2])):
            return False
        if self.ind[stack_num] < 0:
            return False
        val = self.arr[ self.ind[stack_num] ]
        self.arr[ self.ind[stack_num] ] = None
        self.ind[stack_num] -= 3 
        return val
    def push(self, stack_num:int, val:int):
        self.ind[stack_num] += 3 
        print(len(self.arr)-1, self.ind[stack_num])
        if( len(self.arr)-1 < self.ind[stack_num]):
            print("AAAAAAAA")
            for _ in range(3):
                self.arr.append(None)
        self.arr[ self.ind[stack_num] ] = val
    def peek(self, stack_num:int):
        if self.ind[stack_num] > 0:
            return self.arr[self.ind[stack_num]]
        return None
    def isEmpty(self, stack_num:int):
        if self.ind[stack_num] > 0:
            return False
        return True

test = ThreeInOne()

print("pop", test.pop(1))
print("pop", test.pop(5))

for i in range(10):
    test.push(i%3,i*2)
print(test.arr)

for _ in range(4):
    print("pop", test.pop(1))
print("pop", test.pop(5))

print("arr:",test.arr)
print("ind:",test.ind)
for i in range(3):
    print("peek:",test.peek(i))

for i in range(3):
    print("isEmpty:",test.isEmpty(i))
