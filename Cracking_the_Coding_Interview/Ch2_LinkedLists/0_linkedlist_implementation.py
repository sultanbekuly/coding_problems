#(1--->)10 --> 5 --> 16
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedLists:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def __str__(self):
        return str(self.__dict__)

    def append(self, value):
        this_Node = Node(value)
        self.tail.next = this_Node
        self.tail = this_Node
        self.length += 1

    def prepend(self, value):
        this_Node = Node(value)
        this_Node.next = self.head
        self.head = this_Node
        self.length += 1

    def printList(self):
        arr = []
        currentNode = self.head
        while(currentNode != None):
            # print("pL",currentNode.data)
            arr.append(currentNode.data)
            currentNode = currentNode.next
        return arr
    
    def insert(self, index, value):
        #check
        if(index==0):
            self.prepend(value)
        if(index>=self.length):
            self.append(value)

        this_Node = Node(value)
        currentNode = self.head
        i = 0
        while(True):
            if(i==index-1):
                currentNode.next,this_Node.next  = this_Node, currentNode.next
                self.length += 1
                return True
            currentNode = currentNode.next
            i+=1
        return False

    def remove(self, index):
        #check
        if(type(index)!=int or index>=self.length):
            return "error input"
        
        currentNode = self.head
        if(index == 0):#index==0
            self.head = self.head.next
        elif(index == self.length-1):#index==-1
            for _ in range(0,index-1):
                currentNode = currentNode.next
            currentNode.next = None
            self.tail = currentNode
        else:
            for _ in range(0,index-1):
                currentNode = currentNode.next
            currentNode.next = currentNode.next.next
        self.length -= 1
    
    def reverse2(self):
        #reverse the linked list
        arr = self.printList()
        self.head = Node(arr[-1])
        arr.pop()
        currentNode = self.head
        for i in reversed(arr):
            new_node = Node(i)
            currentNode.next = new_node
            currentNode = new_node
        self.tail = currentNode

    def reverse(self):
        if(not self.head.next):#check
            return self.head
        
        self.tail = self.head
        first = self.head
        second = first.next 
        while(second != None):
            # print(first.data, second.data)
            currentNode = second.next
            second.next = first
            first = second
            second = currentNode
            
        self.head = first
        self.tail.next = None
        return self.__str__


myLinkedLists = LinkedLists(10)

print(myLinkedLists.head.data)
print(myLinkedLists.head.next)

myLinkedLists.append(5)
myLinkedLists.append(16)

print(myLinkedLists.head.next)

print(myLinkedLists.tail.data)
print(myLinkedLists.tail.next)

myLinkedLists.prepend(1)

print(myLinkedLists.printList())

print("myLinkedLists.insert(1,7)")
myLinkedLists.insert(1,7)

print(myLinkedLists.printList())

print("myLinkedLists.insert(3,3)")
myLinkedLists.insert(3,3)



print(myLinkedLists.printList())
print(myLinkedLists.length)
print("##reverse",myLinkedLists.reverse())
print(myLinkedLists.head.data)
print(myLinkedLists.head.next.data)

print(myLinkedLists.tail.data)
print("end")
print(myLinkedLists.printList())


myLinkedLists.remove(5)
myLinkedLists.remove(3)
myLinkedLists.remove(0)

print(myLinkedLists.printList())
print(myLinkedLists.head.data)
print(myLinkedLists.tail.data)

print(myLinkedLists.__str__())
print(myLinkedLists.__dict__)
