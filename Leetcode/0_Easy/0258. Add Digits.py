"""
https://leetcode.com/problems/add-digits/
Related Topics
Math
Simulation
Number Theory

TC: O(log n)  n - num
SC: O(1)
"""
class Solution:
    def addDigits(self, num: int) -> int:
        # print(num)
        # print(len(str(num)))
        x = 0
        while True:
            div = 1
            for i in range(len(str(num))):
                # print("int(num / div) % 10:", int(num / div) % 10)
                x += int(num / div) % 10
                div *= 10
            # print("x:",x)
            if len(str(x)) == 1:
                return x
            num = x
            x = 0

        return 0