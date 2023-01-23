# Intersection: Given two (singly) linked lists, determine if the two lists intersect. 
# Return the inter­ secting node. 
# Note that the intersection is defined based on reference, not value.
# That is, if the kth node of the first linked list is the exact 
# same node (by reference) as the jth node of the second linked list, 
# then they are intersecting.
# Hints:#20, #45, #55, #65, #76, #93, #111, #120, #129

# If they have any intersection, their last elements must be the same
# 6>3>4>5
# 1>2>3>4>5
#   6>3>4>5
#So, we can check their length.
#Skip some amounts of the longest and start checking them.
#when intersecting node is found, we will return it.

#TC - O(N) - N is longest linked list or O(A+B)
#SC - O(1)

from LinkedList import LinkedList
from LinkedList import Node

def interction(ll1,ll2):
    ll1.print()
    ll2.print()
    len1 = 0
    len2 = 0
    node = ll1.head
    while(node != None):
        len1 += 1
        node = node.next
    node = ll2.head
    while(node != None):
        len2 += 1
        node = node.next
    print("len-s",len1, len2)
    n1 = ll1.head
    n2 = ll2.head
    if(len1-len2 > 0): #len1 bigger #need to skip some n2
        for _ in range(len1-len2):
            n1 = n1.next
    else:
        for _ in range(len2-len1):
            n2 = n2.next
    print("starting nodes:",n1.data, n2.data) 
    while n1 != None:
        if(n1 == n2):
            return n1
        n1 = n1.next
        n2 = n2.next
    return False


my_ll1 = LinkedList(6)
the_node = Node(3)
#Appending the node
my_ll1.tail.next = the_node
my_ll1.tail = the_node
my_ll1.length +=1
my_ll1.add_multiple([4,5])

my_ll2 = LinkedList(1)
my_ll2.append(2)
my_ll2.tail.next = the_node
the_tail = my_ll2.tail
counter = 0
while (the_tail.next != None):
    the_tail = the_tail.next
    counter += 1
my_ll2.tail = the_tail
my_ll2.length += counter

print("interction:", interction(my_ll1, my_ll2).data)
