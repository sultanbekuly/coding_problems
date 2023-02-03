# A queue implements FIFO (first-in first-out) ordering.
# add (item): Add an item to the end of the list.
# remove(): Remove the first item in the list.
# peek() : Return the top of the queue.
# isEmpty(): Return true if and only if the queue is empty.

class queue_node():
    def __init__(self, val):
        self.val = val
        self.next = None

class queue():
    def __init__(self):
        self.first = None
        self.last = None
    def add(self, val):
        node = queue_node(val)
        if(self.first == None):
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
    def remove(self):
        if self.first == self.last: #if queue is empty or have only one item, it will remain/become empty
            self.first = None
            self.last = None
            return None
        else:
            node = self.first
            self.first = self.first.next
            return node.val
    def peek(self):
        if self.first == None:
            return None
        return self.first.val
    def isEmpty(self):
        return self.first == None

my_queue = queue()

for i in range(5):
    my_queue.add(i) #0,1,2,3,4
    print("added:",i)
    print(my_queue.peek())


print('my_queue.isEmpty():', my_queue.isEmpty())
print('my_queue.peek():', my_queue.peek())

for _ in range(5):
    print("remove:", my_queue.remove())
    print(my_queue.peek())

print(my_queue.peek())
print(my_queue.isEmpty())


