# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# Names of time complexities
# float('inf'), '-inf'


class Solution:
	def maxProfit(self, prices: list[int]) -> int:
		if len(prices) <= 1 :
			return 0 
		min_p = 0 
		profit = 0
		for i in range(len(prices)):
			if prices[min_p] > prices[i]:
				min_p = i
			if prices[i]-prices[min_p] > profit:
				profit = prices[i]-prices[min_p]
			# print(min_p, profit)
		return profit
		# Time: O(N) N - len(prices)
		# Space: O(1)
		
	

# Tests (input, expected output)
tests = [
	([7,1,5,3,6,4], 5),
	([7,6,4,3,1], 0),
	([], 0),
	([1], 0),
	([7,1,5,3,6,4,0,100], 100),
	
	
]
for inp1, expected in tests:
	out = Solution().maxProfit(inp1)
	status = "PASSED" if expected==out else "FAILED"
	print(f"{status}! Input: {(inp1)} -> {out} (expected {expected})")