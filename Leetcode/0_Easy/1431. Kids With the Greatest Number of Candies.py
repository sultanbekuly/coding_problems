"""
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
Related Topics
Array

pass through candies and find max

pass through candies 
    add extraCandies to i
    check if it is equal or greater than max
    if so True
    else False

TC: O(N) where N - len of candies
SC: O(N)
"""
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        arr = []
        for i in range(len(candies)):
            arr.append(True if candies[i]+extraCandies >= m else False)
            # if( candies[i]+extraCandies >= m):
            #     arr.append(True)
            # else:
            #     arr.append(False)
        return arr
