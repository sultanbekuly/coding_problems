# https://leetcode.com/problems/is-subsequence/description/

# TODO: Edge case: Input - string/array - can be empty ""/[]

class Solution:
	def isSubsequence(self, s: str, t: str) -> bool:
		if s == "":
			return True
		i = 0
		j = 0
		while j < len(t) :
			if s[i] == t[j]: # Match
				i += 1
				if i == len(s): # End of s string
					return True
			j += 1
		return False
		# Time: O(N) N - len(t)
		# Space: O(1)
		
	

# Tests (input, expected output)
tests = [
	("abc", "ahbgdc", True),
	("abc", "abczzzz", True),
	("axc", "ahbgdc", False),
	("", "ahbgdc", True),
	("abc", "", False),
	
	
]
for word1, word2, expected in tests:
	out = Solution().isSubsequence(word1, word2)
	status = "PASSED" if expected==out else "FAILED"
	print(f"{status}! Input: {(word1), (word2)} -> {out} (expected {expected})")