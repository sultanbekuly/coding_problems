"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
 

Constraints:

1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.
"""
from collections import Counter
def numJewelsInStones(jewels, stones):
    stones_arr = []
    for i in range(len(stones)):
        stones_arr.append(stones[i:i+1])
    stones_dict = Counter(stones_arr)
    # print("stones_dict:",stones_dict)
    counter = 0
    for i in range(len(jewels)):
        counter += stones_dict.get(jewels[i:i+1],0)
    return counter

print(numJewelsInStones("aA","aAAbbbb"))
print(numJewelsInStones("z","ZZZ"))
