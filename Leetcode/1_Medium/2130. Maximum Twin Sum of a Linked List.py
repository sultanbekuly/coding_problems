
"""
TC: O(N)
SC: O(N) due to recursion
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # max_sum = 0
        # max_counter = 0

        def func(node, counter):
            if node.next == None:
                return [ (counter+1)/2 , [node.val] , 0]
            res = func(node.next, counter+1)
            arr = res[1]
            max_sum = res[2]
            # print(counter, res[0], arr, len(arr), "|",node.val)
            if(len(arr) == res[0]):
                # print("AAAAA")
                last_val = arr.pop()
                x = node.val + last_val
                max_sum = x if x > max_sum else max_sum
                res[0] -= 1

            else:
                arr.append( node.val )

            return [res[0], arr, max_sum]

        res = func(head, 0)
        # print(res)
        max_sum = res[2]
        
        return max_sum
