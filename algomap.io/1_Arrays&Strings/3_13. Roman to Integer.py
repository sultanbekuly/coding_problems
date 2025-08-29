# https://leetcode.com/problems/roman-to-integer/description/

class Solution:
	def romanToInt(self, s: str) -> int:
		# Symbol       Value
		roman = {
			"I":	1,
			"V":	5,
			"X":	10,
			"L":	50,
			"C":	100,
			"D":	500,
			"M":	1000
		}
		val = 0
		i = 0
		while i < len(s):
			v1 = roman[ s[i] ]
			v2 = roman[ s[i+1] ] if i+1<len(s) else 0
			if v1 < v2:
				val += v2-v1
				i+=1
			else:
				val += v1
			# print(v1, v2, val)
			i+=1

		return val

		# Time : O(N) N - len of s
		# Space : O(1) 

# Tests (input, expected output)
tests = [
	("III", 3),
	("LVIII", 58),
	("MCMXCIV", 1994),
	
]
for word1, expected in tests:
	out = Solution().romanToInt(word1)
	status = "PASSED" if expected==out else "FAILED"
	print(f"{status}! Input: {(word1)} -> {out} (expected {expected})")