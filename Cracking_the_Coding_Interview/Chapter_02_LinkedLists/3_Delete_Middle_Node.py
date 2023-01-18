#2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
#the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
#that node.
#EXAMPLE
#lnput:the node c from the linked lista->b->c->d->e->f
#Result: nothing is returned, but the new linked list looks like a->b->d->e- >f
#Hints:#72

#This task can be resolved with two pointers
#First pointer will do one move while second pointer will do two moves
   #1234567890
#p2 -a-b-c-d-e 
#p1 abcde
# When second pointer is None, first pointer will be in the ~ middle
# p1.next = p1.next.next

#TC - O(N) - N is number of elements in the LL
#SC - O(1)

from LinkedList import LinkedList 
from LinkedList import Node 

def Delete_Middle_Node(ll):
    p1 = ll.head
    p2 = p1.next
    print(p1.data, p2.data)
    while(p2.next!=None and p2.next.next != None):
        p1 = p1.next
        p2 = p2.next.next
    print(p1.data)
    p1.next = p1.next.next
    ll.length -= 1


myLL = LinkedList(1)
myLL.generate(10,0,9)
myLL.print()
Delete_Middle_Node(myLL)
myLL.print()
#1-->1-->2-->6-->9-->1-->8-->8-->8-->4
#1 1
#9
#1-->1-->2-->6-->9-->8-->8-->8-->4

myLL = LinkedList(1)
myLL.generate(3,0,9)
myLL.print()
Delete_Middle_Node(myLL)
myLL.print()
#1-->9-->2
#1 9
#1
#1-->2

myLL = LinkedList(1)
myLL.generate(5,0,9)
myLL.print()
Delete_Middle_Node(myLL)
myLL.print()
#1-->5-->6-->4-->9
#1 5
#5
#1-->5-->4-->9

def Delete_Middle_Node2(node):
    if(node.next == None):
        return False
    node.data = node.next.data
    node.next = node.next.next
    return True
    


myLL = LinkedList(1)
myLL.add_multiple([2,3,4])
the_node = myLL.append(5)
myLL.add_multiple([6,7])

myLL.print()
if( Delete_Middle_Node2(the_node)): myLL.length -= 1
myLL.print()



#! #ll.length -= 1
# given only access to that node.
