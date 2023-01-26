# Loop Detection: Given a circular linked list, implement an algorithm that returns 
# the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer 
# points to an earlier node, so as to make a loop in the linked list.
# EXAMPLE
# Input: A -> B -> C -> D -> E -> C[thesameCasearlier]
# Output: C
# Hints: #50, #69, #83, #90


# two pointer solution
# two pointers will meet anywat but I do not know how to get the starting point.

# hashmap solution
# go through list 


#Both of the pointers should start at same position

from LinkedList import LinkedList

def loop_detection(ll):
    ll.print()
    p1 = ll.head    #slow pointer
    p2 = ll.head    #fast pointer
    p1 = p1.next        #to not have collision in the head
    p2 = p2.next.next
    while p2.next!=None and p2.next.next!=None:
        p1 = p1.next
        p2 = p2.next.next
        if(p1 == p2):
            break
    if( p2.next==None or p2.next.next==None):
        return None
    print("Collision:", p1.data, p2.data)
    p1 = ll.head
    counter = 0
    while p1 != p2 or counter>1000:
        #print("p1:", p1.data, "p2:", p2.data)
        p1 = p1.next
        p2 = p2.next
        counter += 1
    return p1.data

myll = LinkedList(1)
myll.add_multiple([2,3,4,5,6,7,8,9])
node_to_point = myll.head
print("myll.length:",myll.length)
for i in range(myll.length):
    print("#",i+1)
    myll.tail.next = node_to_point
    print("node_to_point:", node_to_point.data)
    print("loop_detection:::",loop_detection(myll))
    node_to_point = node_to_point.next
#edge case - no collision
myll.tail.next = None
print("node_to_point:", None)
print("loop_detection:::",loop_detection(myll))


#while p2.next!=None and p2.next.next!=None:
