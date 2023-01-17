# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
# Hints:#8, #25, #41, #67, #126

#Check if K is not more than LL size

#TC - O(N) wher N is the number of elements in the LL
#SC - O(N) or O(1) if we update it in place

from LinkedList import LinkedList 

def return_kth(ll, k:int):
    ll.print()
    print(k)
    if(k >= ll.length):
        return
    new_ll = LinkedList(1)
    curr_node = ll.head
    for i in range(ll.length):
        if(i==k):
            new_ll.head = curr_node
        elif (i>k):
            new_ll.append(curr_node.data)
        curr_node = curr_node.next
    new_ll.print()
    return new_ll



myLinkedList = LinkedList(1)
myLinkedList.generate(100,0,9)
#myLinkedList.print()

return_kth(myLinkedList, 90)
return_kth(myLinkedList, 98)
return_kth(myLinkedList, 110)



# simplest one is to go through ll and findout its length
# next iteration start returning items from (len-k)

#Recursive solutions
#Each of these recursive solutions take O(N) space due to the recursive calls

def return_kth_withoutLen(ll, k:int):
    print("func(0) - print KthToLast")
    def func(node,k):
        if(node == None):
            return 0
        index = func(node.next, k) + 1
        if(index == k):
            print(k,"th to last node is ", node.data)
        return index
    node = ll.head
    func(node, k)

    print("func2 - return KthToLast .data")
    def func2(node,k):
        if(node == None):
            return [0, 0]
        res = func2(node.next, k)
        index = res[0] + 1
        return_data = res[1]
        if(index > k):
            return_data = return_data
        else:
            return_data = node.data
        return [index, return_data]
    node = ll.head
    print(k ,"th to last node is ", func2(node, k)[1] )

    print("func3 - return KthToLast node")
    def func2(node,k):
        if(node == None):
            return [0, node]
        res = func2(node.next, k)
        index = res[0] + 1
        return_node = res[1]
        if(index > k):
            return_node = return_node
        else:
            return_node = node
        return [index, return_node]
    node = ll.head
    print(k ,"th to last node is ", func2(node, k)[1].data )
            
return_kth_withoutLen(myLinkedList, 1)
return_kth_withoutLen(myLinkedList, 3)

#TC - O(N)
#SC - O(1)
def return_kth_withoutLen_iteratevely(ll, k:int):
    p1 = ll.head
    p2 = ll.head
    #p1 = #0; p2 = p1+k
    
    for i in range(k):
        p2 = p2.next
        if(p2 == None):
            return None
    while(p2):
        p1 = p1.next
        p2 = p2.next

    return(p1)

print(return_kth_withoutLen_iteratevely(myLinkedList, 1).data)
print(return_kth_withoutLen_iteratevely(myLinkedList, 3).data)




#Return Kth to Last
#Kth to Last = 4th to last = arr[-4]

