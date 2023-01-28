# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# create new linkedlist
#append item at a time
#depending of which one of two is less

#TC - O(A+B) A len of ll1 and B is len of ll2
#SC - O(A+B)


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # print(list1)
        # print(list2) 
        ll_head = ListNode()
        curr_node = ll_head
        while True:
            if(list1 == None or list2 == None):
                break
            # val1, val2 = None
            if(list2.val > list1.val):
                curr_node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                curr_node.next = ListNode(list2.val)
                list2 = list2.next
            curr_node = curr_node.next

        if(list1 == None):
            curr_node.next = list2
        else:
            curr_node.next = list1

        return ll_head.next
        # print(list1)
        #ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 4, next: None}}}

test = Solution()

list1 = ListNode(1,ListNode(2,ListNode(4) ) )
list2 = ListNode(1,ListNode(3,ListNode(4) ) )
print("Input: list1 = [1,2,4], list2 = [1,3,4]")
print(test.mergeTwoLists(list1, list2 ).val)
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

list1 = ListNode()
list2 = ListNode()
print("Input: list1 = [], list2 = []")
print(test.mergeTwoLists(list1, list2 ).val)
# Input: list1 = [], list2 = []
# Output: []

list1 = ListNode( )
list2 = ListNode(0) 
print("Input: list1 = [], list2 = [0]")
print(test.mergeTwoLists(list1, list2 ).val)
# Input: list1 = [], list2 = [0]
# Output: [0]

