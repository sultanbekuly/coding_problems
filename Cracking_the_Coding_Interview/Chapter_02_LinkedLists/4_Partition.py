#Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
#before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
#to be after the elements less than x (see below). The partition element x can appear anywhere in the
#"right partition"; it does not need to appear between the left and right partitions.
#EXAMPLE
#Input:
#Output:
#3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
#3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
#Hints: #3, #24

#Idea is following:
#iterate through ll
#   when we face node.next.data >= x 
#   it need to be appended to the ll
#   and deleted here - node.next = node.next.next
#we need to save the first appended node. so that, when we face it again, we know that we need to stop.
# or stop when node.next is None

#TC - O(N) - N is number of elements in the ll
#SC - o(1)
from LinkedList import LinkedList

def partitioin(ll, partition):
    ll.print()
    print("partition",partition)
    
    the_node = ll.head 
    tail_node = ll.tail
    
    while(not(the_node.next == None) and not(the_node == tail_node) ):
        #print("the_node.data:",the_node.data)
        if(the_node.data >= partition):
            ll.append(the_node.data)
            the_node.data = the_node.next.data 
            the_node.next = the_node.next.next 
            ll.length -= 1 #bacause .append increments the ll.length
            #print("_moved")
        else:
            the_node = the_node.next
            #print("_skipped")
    #if(the_node.next == None): print("1")
    #if(the_node == first_moved_node):print("2___",the_node, the_node.data)


myLL = LinkedList(3)
myLL.add_multiple([5,8,5,10,2,1])
#myLL.print()
partitioin(myLL, 5)
myLL.print()

