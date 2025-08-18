# https://leetcode.com/problems/jewels-and-stones/description/

# Set(str)=> set{} / hashset
# str in set - check if str in set

class Solution:
	def numJewelsInStones(self, jewels: str, stones: str) -> int:
		jewels_set = set(jewels)
		# print(jewels_set)
		res = 0
		for i in range(len(stones)):
			if stones[i] in jewels_set:
				res += 1
		return res
		# Time: O(n+m)
		# Space: O(n)
		

tests = [
	("aA", "aAAbbbb", 3),
	("z", "ZZ", 0),
	
]

for jewels, stones, excepted in tests:
	res = Solution().numJewelsInStones(jewels, stones)
	if_passed = "PASSED" if res == excepted else "FAILED"
	print( f"{if_passed}! for inputs: {jewels, stones}; res: {res}; excepted: {excepted}.")