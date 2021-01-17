"""
Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation: The third maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
 

Constraints:

1 <= nums.length <= 104
231 <= nums[i] <= 231 - 1
 

Follow up: Can you find an O(n) solution?

"""

def thirdMax(nums):
    first = min(nums)
    second = first
    third = second
    print(nums,first)
    for i in nums:
        if (third<i and second>i):
            third = i
        elif(second<i and first>i):
            third  = second
            second = i
        elif(first<i):
            third  = second
            second = first
            first = i

    if(third == second):
        return first
    else:
        return third

print(thirdMax([1,2,3]))
print(thirdMax([1,2]))
print(thirdMax([1]))
print(thirdMax([2,1,1,1,1,1]))
print(thirdMax([2,2,3,1]))



