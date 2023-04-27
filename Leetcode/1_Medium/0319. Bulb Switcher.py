"""
https://leetcode.com/problems/bulb-switcher/
Related Topics
Math
Brainteaser

Solution: https://www.youtube.com/watch?v=oheChnqf54w

"""
class Solution:
    def bulbSwitch(self, n: int) -> int:
        # res = 0
        # my_dict = {}
        # for i in range(1, n+1):
        #     k = False
            
        #     # if (i/2) in my_dict:
        #     #     k = not my_dict[i/2] 
        #     #     res += 1 if k==True else 0
        #     #     my_dict[i] = k
        #     #     print(i,":",k)
        #     #     continue
            
        #     for j in range(1, i+1):
        #         if(i%j==0):
        #             k = not k
        #         print(i,"%", j,"=", i%j, "-----", k)
        #     print(i,":",k)
        #     my_dict[i] = k
        #     res += 1 if k==True else 0
        # return res

        if(n==0): 
            return 0
        curr = 3
        idx = 1
        total = 0
        while(total<n):
            total += curr
            curr+=2
            idx += 1

        return idx-1


#99999