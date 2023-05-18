# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # print("-------------")
        # if head == None or head.next == None:
        #     return head
        # node1 = head
        # node2 = node1.next
        # head = node2
        # node2.next, node1.next = node1, node2.next
        # while node1.next != None and node2.next != None :
        #     node0 = node1
        #     print("#0", node0)
        #     node1 = node1.next
        #     print("#1", node1)
        #     node2 = node1.next
        #     print("#2", node2)
        #     a = node0
        #     b = node1
        #     c = node2

        #     node0.next, node2.next, node1.next = node2, node1, node2.next
        #     a = node0
        #     b = node1
        #     c = node2
        #     node0.next = b
        #     node2.next = a
        #     node1.next = c.next
        # return head        

        # Dummy node
        dummy = ListNode(0)
        # Point the next of dummy node to the head
        dummy.next = head
        # This node will be used to traverse the list
        current = dummy
        # Loop until we reach to the second last node
        while current.next is not None and current.next.next is not None:
            # First node of the pair
            first = current.next
            # Second node of the pair
            second = current.next.next
            # Point the next of first node to the node after second node
            first.next = second.next
            # Now the current node's next should be the second node
            current.next = second
            # Linking the original second node to the first node
            current.next.next = first
            # Move the pointer two nodes ahead
            current = current.next.next
        return dummy.next
        