# https://leetcode.com/problems/merge-strings-alternately/description/

# TODO: "".join(res) - how to array join to string

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for i in range( len(word1) if len(word1) > len(word2) else len(word2) ):
            # print(i)
            word1_char = word1[i] if i<len(word1) else ""
            res.append(word1_char)
            
            word2_char = word2[i] if i<len(word2) else ""
            res.append(word2_char)
            
        return "".join(res)
        # Time: O(A+B)
        # Sapace: O(A+B)
        # where A is len of word1, B is len of word2
        
    


# Tests (input, expected output)
tests = [
    ("abc", "pqr", "apbqcr"),
    ("ab", "pqrs", "apbqrs"),
    ("abcd", "pq", "apbqcd"),
    
]
for word1, word2, expected in tests:
    out = Solution().mergeAlternately(word1, word2)
    status = "PASSED" if expected==out else "FAILED"
    print(f"{status}! Input: {(word1, word2)} -> {out} (expected {expected})")