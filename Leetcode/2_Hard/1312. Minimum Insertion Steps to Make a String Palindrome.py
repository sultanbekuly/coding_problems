"""
https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/
Related Topics
String
Dynamic Programming


Solution: https://www.youtube.com/watch?v=rSEoN6qnb8Q
"""
import math

class Solution:
    def minInsertions(self, s: str) -> int:
        # changes = 0
        # def isPolindrome(s:str) -> bool:
        #     for i in range( floor( len(s)/2 ) ):
        #         if s[i] != s[(i+1)*-1]:
        #             return False
        #     return True

        # if isPolindrome(s):
        #     return changes

        # return 100
        def helper(i, j):
            if i>=j:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if s[i] == s[j]:
                memo[(i,j)] = helper(i+1, j-1)
            else:
                choice1 = 1 + helper(i+1, j)
                choice2 = 1 + helper(i, j-1)
                memo[(i,j)] =  min(choice1, choice2)
            return memo[(i,j)]
        memo = {}

        return helper(0, len(s)-1)


