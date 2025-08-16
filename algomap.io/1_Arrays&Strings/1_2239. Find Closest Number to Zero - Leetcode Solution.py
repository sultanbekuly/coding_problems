# https://leetcode.com/problems/find-closest-number-to-zero/description/


class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        # print("nums:", nums)
        closest = nums[0]
        for num in nums:
            # print("num:", num)
            if abs(closest) > abs(num):
                closest = num
            if abs(closest) == abs(num) and num > closest:
                closest = num
                # print("closest:", closest)
        return closest
        
        # Time: O(n)
        # Space: O(1)


# Tests (input, expected output)
tests = [
    ([-4,-2,1,4,8], 1),
    ([2,-1,1], 1),
    ([-100000,-100000], -100000),
    ([2,1,1,-1,100000], 1)
    
]
for arr, expected in tests:
    out = Solution().findClosestNumber(arr)
    status = "PASSED" if expected==out else "FAILED"
    print(f"{status}! Input: {arr} -> {out} (expected {expected})")