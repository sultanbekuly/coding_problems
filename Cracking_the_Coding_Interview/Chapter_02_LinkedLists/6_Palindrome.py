# Palindrome: Implement a function to check if a linked list is a palindrome. 
# Hints:#5, #13, #29, #61, #101

#recursive solution.
#two pointers
#one pointer +=1
#second pointer += 2
# so that when first one will be on the middle, second one will be on the end
# and will indicate that we need to start testing

#we should return [T/F, node] #node that need to be checked

#A1 A2 A3 A4
#   B1    B2    B3    B4     
#1->2->3->4->5->6->7->8

#A1 A2 A3 
#   B1    B2    B3        
#1->2->3->4->5->6->7

#TC O(N) - N is length of the list
#SC O(N) (due to recursive solution)

from LinkedList import LinkedList

def is_palindrome(ll):
    ll.print()
    p1 = ll.head
    p2 = p1.next
    if(p1 is None or p2 is None):
        return True
    
    def is_p_rec(p1, p2):
        if(p2.next is None):
            return [True, p1.next]
        if(p2.next.next is None):
            return [True, p1.next.next]
        p1 = p1.next
        p2 = p2.next.next
        res = is_p_rec(p1, p2)
        is_pol = res[0]
        node_to_test = res[1]
        if is_pol == False:
            return [False, None]
        if p1.data == node_to_test.data:
            # print (p1.data, node_to_test.data)
            return [True, node_to_test.next]
        else:
            return [False, None]
    return is_p_rec(p1,p2)[0]


    
    
    


ll_true = LinkedList(1)
ll_true.add_multiple([2, 3, 4, 5, 4, 3, 2, 1]) #[1, 2, 3, 4, 5, 4, 3, 2, 1]
print(is_palindrome(ll_true))

ll_true = LinkedList(1)
ll_true.add_multiple([2, 3, 4, 4, 3, 2, 1]) #[1, 2, 3, 4, 4, 3, 2, 1]
print(is_palindrome(ll_true))

ll_false = LinkedList(1)
ll_false.add_multiple([2, 3, 4, 5, 6, 7, 8, 9]) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(is_palindrome(ll_false))

ll_true = LinkedList(1)         #[1]
print(is_palindrome(ll_true))

ll_false = LinkedList(1)
ll_false.append(2)              #[1,2]
print(is_palindrome(ll_false))

ll_true = LinkedList(1)
ll_true.append(1)              #[1,1]
print(is_palindrome(ll_true))

#