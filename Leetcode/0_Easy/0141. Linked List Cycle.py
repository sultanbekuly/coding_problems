#https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

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

# we can do it by having two pointers: fast and slow
# if fast will be None then return false
# if they will be same return true

#TC - O(N) - N is length of the ll
#SC - O(1)

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        if(fast == None):
            return False
        if(fast.next == None):
            return False

        while(True):
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                return True
            
            if(fast == None):
                break
            if(fast.next == None):
                break
        return False

test = Solution()

list = ListNode(3)
list_tail = ListNode(-4)
node_cycle_start = ListNode(2,ListNode(0, list_tail ) )
list_tail.next = node_cycle_start
list.next = node_cycle_start

print("Input: head = [3,2,0,-4], pos = 1")
print(test.hasCycle(list))
#Input: head = [3,2,0,-4], pos = 1
#Output: true
#Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).


list = ListNode(1)
list_tail = ListNode(2)
list.next = list_tail
list_tail.next = list

print("Input: head = [1,2], pos = 0")
print(test.hasCycle(list))
#Input: head = [1,2], pos = 0
#Output: true
#Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.


list = ListNode(1)

print("Input: head = [1], pos = -1")
print(test.hasCycle(list))
#Input: head = [1], pos = -1
#Output: false
#Explanation: There is no cycle in the linked list.


list = ListNode(1, ListNode(2) )
print("Input: head = [1,2], pos = -1")
print(test.hasCycle(list))
#Input: head = [1,2], pos = -1
#Output: false
#Explanation: There is no cycle in the linked list.


#if(fast == None):
#    return False
#if(fast.next == None):
#    return False