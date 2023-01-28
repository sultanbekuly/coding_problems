#https://leetcode.com/problems/remove-duplicates-from-sorted-list/
#Definition for singly-linked list.
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

# we need to go through ll
# check if element is equal to next element
# if so delete the next node

#TC - O(N) - N is ll length
#SC - O(1)


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr_node = head
        if(curr_node == None):
            return head
        while(curr_node.next != None):
            if(curr_node.val == curr_node.next.val):
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next
        return head
test = Solution()

list1 = ListNode(1,ListNode(1,ListNode(2) ) )
print("Input: head = [1,1,2]")
print(test.deleteDuplicates(list1))
#Input: head = [1,1,2]
#Output: [1,2]

list1 = ListNode(1,ListNode(1,ListNode(2, ListNode(3, ListNode(3) ) ) ) )
print("Input: head = [1,1,2,3,3]")
print(test.deleteDuplicates(list1))
#Input: head = [1,1,2,3,3]
#Output: [1,2,3]

#edge case - []
print("Input: head = None")
print(test.deleteDuplicates(None))
#Input: head = None
#Output: None

#edge case - []
