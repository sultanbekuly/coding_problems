"""
58. Length of Last Word
Easy

910

2912

Add to List

Share
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Example 2:

Input: s = " "
Output: 0
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
"""

def length_of_last_word(s):

    s = s.strip() # get rid of spaces    
    counter = 0 
    for element in reversed(range(0, len(s))): 
        if(s[element]==" "):
            break
        counter += 1
    return counter

print(length_of_last_word(" "))#0

print(length_of_last_word("a "))#1

print(length_of_last_word(" a "))#1

print(length_of_last_word("Hello World"))#5

