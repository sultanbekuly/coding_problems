"""
https://leetcode.com/problems/merge-strings-alternately/
Related Topics
Two Pointers
String


get min len 
iterate through range(min_len) by upated output string
add the remaining string tail
TC: O(N)  N - shortest string len
SC: O(N+M)  N,M - words
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1),len(word2))
        output = ""
        for i in range(min_len):
            output += word1[i]
            output += word2[i]
        if min_len == len(word1):
            output += word2[min_len :]
        else:
            output += word1[min_len :]
        return output        
