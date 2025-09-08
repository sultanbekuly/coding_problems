# https://leetcode.com/problems/summary-ranges/description/

class Solution:
	def summaryRanges(self, nums: list[int]) -> list[str]:
		if len(nums) == 0: return [] # if input empty
		
		start = nums[0]
		end = nums[0]
		res = []

		for i in range(1,len(nums)):
			# print(i,nums[i], start, end)
			if end == nums[i]-1:
				end = nums[i]
			else:
				if start == end:
					res.append(f"{start}")
				else:
					res.append(f"{start}->{end}")
				start = nums[i]
				end = nums[i]
		
		if start == end:
			res.append(f"{start}")
		else:
			res.append(f"{start}->{end}")

		return res
		# Time: O(N) N - len(nums)
		# Space: O(N) N - len(nums)
		
	



# Tests (input, expected output)
tests = [
	([0,1,2,4,5,7], ["0->2","4->5","7"]),
	([0,2,3,4,6,8,9], ["0","2->4","6","8->9"]),
	([], []),
	([0], ["0"]),
	([0,2,4], ["0","2","4"]),
	
	
]
for inp1, expected in tests:
	out = Solution().summaryRanges(inp1)
	status = "PASSED" if expected==out else "FAILED"
	print(f"{status}! Input: {(inp1)} -> {out} (expected {expected})")