
from typing import List
from math import gcd
from functools import lru_cache

class Solution:
    @lru_cache(None)
    def dfs(self, nums: List[int], round: int, state: int) -> int:
        if round > len(nums) // 2:
            return 0
        
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                picked = (1 << i) | (1 << j)
                if (state & picked) == 0:
                    ans = max(ans, round * gcd(nums[i], nums[j]) + self.dfs(nums, round + 1, state | picked))
        
        return ans
    
    def maxScore(self, nums: List[int]) -> int:
        return self.dfs(tuple(nums), 1, 0)

# # Usage example
# solution = Solution()
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# print(solution.maxScore(nums))
