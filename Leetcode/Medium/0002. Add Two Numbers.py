#https://leetcode.com/problems/add-two-numbers/description/

#remainder = 0
#go through the ll while one of them is not none
#sum digits + remainder
# if more that 10 get last digit and append to result ll
# remainder = 1
# else remainder = 0 

# edge case - 9>9 + 9>9 = 8>9>1
    # input: two digits, output: three digits
# edge case - 1 + 1>1>1

#TC - O(N) - N is longest length of LL
#SC - O(N) 

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

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        remainder = 0
        res = ListNode()
        curr_node = res
        while(l1 != None and l2 != None):
            Sum = l1.val + l2.val + remainder
            if(Sum>9):
                remainder = 1
                Sum = Sum%10
            else:
                remainder = 0
            curr_node.next = ListNode(Sum)
            curr_node = curr_node.next
            l1 = l1.next
            l2 = l2.next

        #one of them is must be None
        if(l1 == None):
            l1 = l2
        while(l1 != None):
            Sum = l1.val + remainder
            if(Sum>9):
                remainder = 1
                Sum = Sum%10
            else:
                remainder = 0
            curr_node.next = ListNode(Sum)
            curr_node = curr_node.next
            l1 = l1.next

        if(remainder > 0):
            curr_node.next = ListNode(remainder)

        return res.next #because first one is empty



test = Solution()

list1 = ListNode(2,ListNode(4,ListNode(3) ) )
list2 = ListNode(5,ListNode(6,ListNode(4) ) )
print(list1, " + ",list2)
print(test.addTwoNumbers( list1, list2 ))
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

list1 = ListNode(0 )
list2 = ListNode(0 )
print(list1, " + ",list2)
print(test.addTwoNumbers( list1, list2 ))
# Input: l1 = [0], l2 = [0]
# Output: [0]

list1 = ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9 )))))))
list2 = ListNode(9,ListNode(9,ListNode(9,ListNode(9)) ) )
print(list1, " + ",list2)
print(test.addTwoNumbers( list1, list2 ))
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]








