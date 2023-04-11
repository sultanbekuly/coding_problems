"""
https://leetcode.com/problems/removing-stars-from-a-string/description/
Related Topics
String
Stack
Simulation
--
we can go throug each letter (char) by using while loop
    (from left to right)
    if we face the star
        we need to concatenate and update the current string
        and decrement the pointer by one because two were deleted

TC: O(N)
SC: O(1)
"""

class Solution:
    def removeStars(self, s: str) -> str:
        point = 0
        while (point < len(s) ):
            if s[point] == '*':
                s = s[:point-1] + s[point+1:]
                point -= 2
                # print(s)
            point += 1
        
        return s
