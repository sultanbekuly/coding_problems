"""
[7,9,6,6, 7,8, 3,0,9,5], k = 5
[7,9,6,6, 8,7, 3,0,9,5]
__________-_-__________

[1, 2,3, 4, 5], k = 2
[1, 4,3, 2, 5]
____-____-____

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        x = head
        y = head
        z = head
        node = head
        n = 1
        while(node != None):
            # print(node.val)
            if n == k:
                # print("x assigned")
                x = node
            if n-k > 0:
                # print("z assigned")
                z = z.next

            n += 1
            node = node.next
        # print("x", x.val, x)
        # print("z", z.val, z)
        
        x.val, z.val = z.val, x.val
        return head
        
        
        