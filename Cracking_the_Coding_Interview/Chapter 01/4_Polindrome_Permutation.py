# Palindrome Permutation: 
# Given a string, write a function to check if it is a permutation of a palin­drome. 
# A palindrome is a word or phrase that is the same forwards and backwards. 
# A permutation is a rearrangement of letters. 
# The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.) 
# Hints:#106,#121,#134,#136

#As I can see from the example, it is not case sensitive. 
# So, first, I would convert every letter to lower case.
# and get rid off space(s)
#If input string length devided by two without remainder,
# it means every letter should occur twice(or 4,6..)(even number times)
# else, the same logic but only one char can occur twice
#Clarify, if the string is ASCII(or extended ASCII) or Unicode
# Then, We can create an array with 128 elements for ASCII filled with zeros
# Go through the string: 
#  convert every char to its numeric representation - ord()
#  and increment according array element
# Then go through the array and check if there are only one or no odd elements

#TC - O(N)
#SC - O(1)

def Polindrome_Permutation(input:str):
    print(input)
    updated_input = ""
    for i in input:
        if(i != " "):
            updated_input += i.lower()
    print(updated_input)
    ASCII_arr = [0 for _ in range(128) ]
    for i in updated_input:
        ASCII_arr[ord(i)] += 1
    
    allowed_odd = len(updated_input)%2 # check if one or zero odd numbers are allowed
    count_odd = 0
    for i in ASCII_arr:
        if(i%2 != 0): #odd number
            count_odd+=1
        if(count_odd > allowed_odd):
            return False
    return True


print(Polindrome_Permutation("Tact Coa"))   #True
print(Polindrome_Permutation("Tact CoaS"))  #False

