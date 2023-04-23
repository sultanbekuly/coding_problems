"""
https://leetcode.com/problems/restore-the-array/description/
Related Topics
String
Dynamic Programming
"""
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        cache = {}
        def backtrack(pos: int) -> int:
            original_pos = pos
            count = 0
            buffer = 0
            if pos in cache:
                return cache[pos]
            for i in range(pos, len(s)):
                buffer *= 10 
                buffer += int(s[i])
                if buffer <= k and i+1 <= len(s)-1 and s[i+1] != '0':
                    count += (backtrack(i+1) % 1000000007)
                if buffer > k:
                    break
            else:
                if buffer <= k:
                    count += 1
            cache[original_pos] = count
            return count
        return backtrack(0) % 1000000007

        # mod = 10**9 + 7
        
        # def dfs(x, y):
        #     print(s[x:y])
        #     if (x,y) in memo:
        #         return memo[(x,y)]
                
        #     if s[x:y] == "":
        #         memo[(x,y)] = 0
        #         return memo[(x,y)]
            
        #     if s[x:y][0] == "0":
        #         memo[(x,y)] = 0
        #         return memo[(x,y)]

        #     z = int(s[x:y])
        #     if(z <= k and z != 0):
        #         memo[(x,y)] = 1
        #         # return memo[(x,y)]

        #     print(range(1, y-x+1))
        #     for i in range(1, y-x+1): #1,2,3,4
        #         res = dfs(x, x + i) + dfs(x + i, y) #1234  (1, '234') 

        #     return res
        # memo = {}
        # res = dfs(0, len(s))
        
        # print("memo:", memo, "res:", res)

        # return 0