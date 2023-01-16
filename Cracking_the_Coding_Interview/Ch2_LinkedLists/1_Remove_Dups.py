# Remove Dups! Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed? 
# Hints: #9, #40

# Create hashmap 
# add first item to HM
# iterate through input_ll (linked list) 
#   check if curr_node.next.value in HM
#   if so change curr_node.next to curr_node.next.next
#   else add curr_node.next.value to HM
# return the updated input_ll


#TC O(N) - N ll length
#SC O(N) 

#if a temporary buffer is not allowed
#TC O(N^2) - double iteration through ll.
#SC O(1)

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
        for i in range(self.length):
            print( "#"+str(i), currentNode.data)
            currentNode = currentNode.next



def Remove_Dups(ll):
    print(ll)
    hm = {}
    curr_node = ll.head
    hm[curr_node.data] = True
    #while curr_node.next != None:
    for _ in range(ll.length-1):
        # print(curr_node.next.data)
        if curr_node.next.data in hm:
            # print("-duplicate")
            curr_node.next = curr_node.next.next
            ll.length -= 1
        else:
            # print("-add_to_hm")
            hm[curr_node.next.data] = True
            curr_node = curr_node.next
    print(curr_node.data)
    ll.tail = curr_node
    print(hm)
    return ll


    


myLinkedList = LinkedList(1)
myLinkedList.append(2)
myLinkedList.append(3)
myLinkedList.append(1) #duplicate
myLinkedList.append(4)
myLinkedList.append(2) #duplicate
myLinkedList.append(5)
myLinkedList.append(2) #duplicate
print( myLinkedList.head.data, myLinkedList.tail.data, myLinkedList.length)

myLinkedList.print()
print(Remove_Dups(myLinkedList))
myLinkedList.print()
print("tail:",myLinkedList.tail.data)

#do not forget to update tail


