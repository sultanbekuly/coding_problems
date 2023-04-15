"""
https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/
Related Topics
Array
Dynamic Programming
Prefix Sum

We need to get evey possible ways to do k moves and get the max from that

dfs
    if k == 1: return the pop
    store = pop
    store_arr = []
    for pile in piles
        store_arr.append(pop + __) dfs.    pile - choosen to pop, piles, k -= 1

    return max(store_arr)
"""


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        #https://www.youtube.com/watch?v=nR3oE6W1Sdc
        N = len(piles)

        has_cache = [[False] * (k+1) for _ in range(N)]
        cache = [[None] * (k+1) for _ in range(N) ]

        def calculate(index, kleft):
            if index == N:
                return 0
            if kleft == 0:
                return 0
            if has_cache[index][kleft]:
                return cache[index][kleft]

            # take "x" items from top of the piles
            best = 0
            L = min(len(piles[index]) + 1, kleft + 1)
            scores = 0
            for x in range(L):
                best = max(best, calculate(index+1, kleft-x) + scores)
                if x < len(piles[index]):
                    scores += piles[index][x]
            has_cache[index][kleft] = True
            cache[index][kleft] = best
            return best
        
        return calculate(0, k)
















