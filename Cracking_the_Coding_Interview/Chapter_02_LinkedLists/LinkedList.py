from random import randint
# for ll generation

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self, data) -> None:
        the_node = Node(data)
        self.head = the_node
        self.tail = self.head
        self.length = 1
    def __str__(self) -> str:
        return str(self.__dict__)
    def append(self, data):
        the_node = Node(data)
        self.tail.next = the_node
        self.tail = the_node
        self.length += 1
    def prepend(self, data):
        the_node = Node(data)
        the_node.next = self.head
        self.head = the_node
        self.length += 1
    def print(self):
        currentNode = self.head
        values=[]
        for i in range(self.length):
            values.append(str(currentNode.data))
            # print( "#"+str(i), currentNode.data)
            currentNode = currentNode.next
        print ('-->'.join(values))
    def generate(self, n, min_value, max_value):
        # self.head = self.tail = None
        # self.__init__(randint(min_value, max_value))
        for i in range(n-1):
            self.append(randint(min_value, max_value))
        return self
