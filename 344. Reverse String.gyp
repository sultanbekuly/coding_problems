"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    for i in range(len(s)//2):
        s[i],s[len(s)-1-i] = s[len(s)-1-i],s[i]
    return s

print(reverseString(["h","e","l","l","o"]))#["o","l","l","e","h"]
print(reverseString(["H","a","n","n","a","h"]))#["h","a","n","n","a","H"]
print(reverseString(["H"]))
print(reverseString(["H","a","z"]))
