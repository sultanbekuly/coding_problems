"""
result = []
for i in spells
    counter = 0
    for j in potions
        if(i*j >= success):
            counter++
    result.append(counter)

TC: O(n*m) -- too slow

        # result = []
        # for i in spells:
        #     counter = 0
        #     for j in potions:
        #         if(i*j >= success):
        #             counter += 1
        #     result.append(counter)
        # return result
"""

"""
order of the Potions doesn't matter
Sort it

get the spell
min_potion = ceil(success/spell) - minimum value from potions
get index of the min_potion
len(potions) - the index

TC: O(m*Logm + n*Logm)

"""

"""
This solution first sorts the potions array in non-decreasing order using the built-in sort() function. 
It then initializes the result array pairs to all zeros.

Next, it iterates over the spells array using a for loop and for each spell, it uses the bisect_left() 
function from the bisect module to find the index of the first potion whose strength is greater than or 
equal to success/spells[i]. It then counts the number of successful pairs for the current spell by 
subtracting this index from the length of the potions array.

Finally, it returns the pairs array containing the number of successful pairs for each spell.
"""

class Solution:
    # def binary_search(sorted_list: List[int], target: int) -> int: 
    #     #returns index of target or -1 if not found
    #     left = 0
    #     right = len(sorted_list)-1
    #     print("target:", target)
    #     while left <= right:
    #         center =  ceil((left + right) / 2) #left + int(right-left)
    #         if(sorted_list[center] > target):
    #             right = center-1
    #         else:
    #             left = center+1
    #     print("left:", left)
    #     return left

    #--------------------------------------------------------------------

    # def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
    #     potions.sort()
        
    #     result = []
    #     if(len(potions) > 10):
    #         return [-1]
    #     print(potions)
    #     len_potions = len(potions)
    #     for spell in spells:
    #         min_potion = ceil(success/spell)

    #         min_potion_index = Solution.binary_search(potions, min_potion)

    #         result.append(len_potions - min_potion_index)
    #     return result

    #--------------------------------------------------------------------
    #TC: O((m + n) log m)
    #SC: O(1)
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Sort the potions array in non-decreasing order
        potions.sort()

        # Initialize the result array to all zeros
        pairs = [0] * len(spells)

        # Iterate over the spells array
        for i in range(len(spells)):
            # Find the index of the first potion whose strength is greater than or equal to success/spells[i]
            idx = bisect_left(potions, success / spells[i])

            # Count the number of successful pairs for the current spell
            pairs[i] = len(potions) - idx

        return pairs
        
        
            







