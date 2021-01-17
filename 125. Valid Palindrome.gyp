"""
Easy
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
 

Constraints:

s consists only of printable ASCII characters.
"""

def isPalindrome(s):
    new_s = ""
    for i in range(len(s)):
        ord_s = ord(s[i:i+1])
        print("s[i:i+1]",s[i:i+1],"ord",ord_s)
        if( (ord_s>=0 and ord_s<48) or (ord_s>57 and ord_s<65) or (ord_s>90 and ord_s<97) or (ord_s>122)):
            continue
        elif(ord_s>96 and ord_s<123):
            new_s += chr(ord_s-32)
        else:
            new_s += s[i:i+1]
        print("new_s:",new_s)
    for i in range(len(new_s)//2):
        if(new_s[i] != new_s[len(new_s)-i-1]):
            return False
    return True
print(isPalindrome("A man, a plan, a canal: Panama"))

print(isPalindrome("race a car"))

print(isPalindrome(""))


print(isPalindrome("A A"))
print(isPalindrome("Aa"))
print(isPalindrome("0P"))


