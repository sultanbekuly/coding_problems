#https://leetcode.com/problems/minimize-maximum-of-array/description/
"""
Get max value and decrease it to max 
[3,7] -> [5,5]

I think this can be solved mathematically by O(n) time

[1,1,10]


[1,1,1,10]
13/4 => 3.


3 7 1 6
10 1
->First number in array is limitation

Iterate through the list by pairs and tying make them equal
[3,7,1,6]
[5,5,3,4]
(3+7) = 10 /2 > [5,5]
(1+6) = 7  /2 > ceil() > 4, floor() > 3 > [4,3]


[3,7,1,6] > 4,-6,5 > -10,11 > 22
[3,7,1,6] > 5,-6,4

find max
get its left side to get the minimum value

"""

#solution from internet
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        N = len(nums)
        nums.reverse()

        left = 0
        right = 10**9

        #O(N) time
        def good(target):
            carry = 0
            for x in nums:
                x += carry
                carry = 0
                if x >= target:
                    carry = x - target
            return carry == 0
        
        #O(log U) where U size of the universe -> 10^9
        #O(N logU) time
        #O(1) space
        while left < right:
            mid = (left + right) // 2

            if good(mid):
                right = mid
            else:
                left = mid + 1
                
        return left






