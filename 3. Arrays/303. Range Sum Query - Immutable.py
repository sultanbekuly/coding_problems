"""
303. Range Sum Query - Immutable
Easy

Given an integer array nums, find the sum of the elements between indices left and right inclusive, where (left <= right).

Implement the NumArray class:

NumArray(int[] nums) initializes the object with the integer array nums.
int sumRange(int left, int right) returns the sum of the elements of the nums array in the range [left, right] inclusive (i.e., sum(nums[left], nums[left + 1], ... , nums[right])).
 

Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1)) 
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
 

Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105
0 <= left <= right < nums.length
At most 104 calls will be made to sumRange."""

class NumArray:

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        #check input:
        if (left>=0 and left<len(self.nums) and right>=0 and right<len(self.nums)):
            pass
        else: return "error. input is out of the range of the list"
        #O(n):
        sum = 0 
        for i in range(left, right+1):
            sum += self.nums[i]
        return sum

test1 = NumArray([-2, 0, 3, -5, 2, -1])
print(test1.sumRange(0, 2))#1
print(test1.sumRange(2, 5))#-1
print(test1.sumRange(0, 5))#-3

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)