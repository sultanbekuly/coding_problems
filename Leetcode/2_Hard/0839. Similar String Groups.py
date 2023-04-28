"""
https://leetcode.com/problems/similar-string-groups/description/
Related Topics
Array
String
Depth-First Search
Breadth-First Search
Union Find

https://walkccc.me/LeetCode/problems/0839/
"""
class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        ans = 0
        seen = [False] * len(A)
        
        for i in range(len(A)):
            if not seen[i]:
                self.dfs(A, i, seen)
                ans += 1
        
        return ans
    
    def dfs(self, A: List[str], i: int, seen: List[bool]) -> None:
        seen[i] = True
        for j in range(len(A)):
            if not seen[j] and self.isSimilar(A[i], A[j]):
                self.dfs(A, j, seen)
    
    def isSimilar(self, X: str, Y: str) -> bool:
        diff = 0
        for i in range(len(X)):
            if X[i] != Y[i]:
                diff += 1
                if diff > 2:
                    return False
        return True
