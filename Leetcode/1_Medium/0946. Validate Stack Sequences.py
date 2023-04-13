"""
https://leetcode.com/problems/validate-stack-sequences/description/
946. Validate Stack Sequences 
Related Topics
Array
Stack
Simulation


Add items to list till we face the pop item.
As pop item is faced pop it and try to pop others
poitner for each table 
and one new list 

TC: O(n+m)
SC: O(n)
    n-pushed
    m-poped

"""
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for n in pushed :
            stack.append(n)
            while i < len(popped) and stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack
            
