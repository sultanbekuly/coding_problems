# https://leetcode.com/problems/longest-common-prefix/description/

# break for loop (pass, continue)

class Solution:
	def longestCommonPrefix(self, strs: list[str]) -> str:
		if len(strs) == 1:
			return strs[0]
		prefix = list(strs[0])
		for s in strs:
			len_s = len(s)
			len_p = len(prefix)
			len_smallest = len_s if len_s < len_p else len_p
			prefix = prefix[0:len_smallest] # cut prefix by smallest len
			for i in range(len_smallest):
				if s[i] != prefix[i]:
					prefix = s[0:i] # cut prefix by discrepency
					break
			
		return "".join(prefix)
		# Time: O(N*M) N - len(strs), M - len(str)
		# Space: O(1)	
	


# Tests (input, expected output)
tests = [
	(["flower","flow"], "flow"),
	(["flower","flow","flight"], "fl"),
	(["dog","racecar","car"], ""),
	(["dog"], "dog"),
	(["ab", "a"], "a"),	
]
for inp1, expected in tests:
	out = Solution().longestCommonPrefix(inp1)
	status = "PASSED" if expected==out else "FAILED"
	print(f"{status}! Input: {(inp1)} -> {out} (expected {expected})")