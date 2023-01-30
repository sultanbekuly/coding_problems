#https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        str_res = ""
        str_res += str(self.val)+"->" 
        next = self.next
        while(next != None):
            str_res += str(next.val)+"->" 
            next = next.next
        return str_res

# we can solve it recursively
# when recursion will get to the end it will return 0  (base case)
# then every return value need to be added to one 
#       and checked if it equal to n

#if so cur_node.next = cur_node.next.next

#TC - O(N) - N is length of the ll
#SC - O(N) - due to recursion

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        def rec(cur_node, n):
            if(cur_node.next == None):
                return [0, False]
            rec_res = rec(cur_node.next, n)
            num = rec_res[0] + 1
            if(rec_res[1]):
                return [num, True]
            if(num == n):
                cur_node.next = cur_node.next.next
                return [num, True]
            return [num, False]

        if(head.next == None and n==1):
            return None
        else:
            if(rec(head, n)[1] == False):
                return head.next

        return head


test = Solution()

list1 = ListNode(1,ListNode(2,ListNode(3 ,ListNode(4 ,ListNode(5 ))) ) )
n = 2
print(list1, " ; ",n)
print(test.removeNthFromEnd( list1, n ))
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]


list1 = ListNode(1)
n = 1
print(list1, " ; ",n)
print(test.removeNthFromEnd( list1, n ))
# Input: head = [1], n = 1
# Output: []

list1 = ListNode(1,ListNode(2 ) )
n = 1
print(list1, " ; ",n)
print(test.removeNthFromEnd( list1, n ))
# Input: head = [1,2], n = 1
# Output: [1]

list1 = ListNode(1,ListNode(2 ) )
n = 2
print(list1, " ; ",n)
print(test.removeNthFromEnd( list1, n ))
# Input: head = [1,2], n = 2
# Output: [2]




#edge case:
#only one item in the list Input: head = [1], n = 1;  Output: []

#edge case:
#we cannot delete head..




