class Solution:
    def arraySign(self, nums: List[int]) -> int:
        val = 1
        for i in nums:
            if i == 0:
                return 0
            val *= i
        return 1 if val>1 else -1
        