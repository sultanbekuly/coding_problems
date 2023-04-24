"""
https://leetcode.com/problems/last-stone-weight/
Related Topics
Array
Heap (Priority Queue)

[2,7,4,1,8,1]
Sort Array
[1,1,2,4,7,8]

get difference first and second item (last and pre-last)
|7-8| = 1

if not zero, insert result to the sorted array
[1, 1,1,2,4]
+delete (pop) used items

repeat till list is empty or one item in the list

TC: O(nlogn + nlogn) => O(nlogn) 
    O(nlogn) - sorting + O(n*logn) - passing through list by inserting to sorted list
SC: O(1)
"""
from bisect import insort

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # print(stones)
        stones = sorted(stones)
        # print(stones)
        while(len(stones) > 1):
            # print(stones)
            s1 = stones.pop()
            s2 = stones.pop()
            diff = abs(s2-s1)
            if(diff != 0):
                insort(stones, diff)
        
        res = stones[0] if len(stones) == 1 else 0

        return res


