# One Away: There are three types of edits that can be performed on strings: 
# insert a character, remove a character, or replace a character. 
# Given two strings, write a function to check if they are one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true 
# pales, pale -> true 
# pale, bale -> true 
# pale, bake -> false

# First check if difference of length of the strings is not more than 1.
# Get the biggest length and use it for range in for loop
# create two variables for string pointers
# Iterate through loop and increment the pointers
# use them to get string index and check if they are the same
# if yes ok
# if not check i+1 == j or i == j+1
#  if so update index accordingly
# else return false

# TC - O(N)
# SC - O(1)

def One_Away(str1, str2):
    print(str1," ; ",str2)
    if( abs( len(str1)-len(str2) ) > 1):
        return False
    i = 0
    j = 0
    smallest_len = 0
    if(len(str1) < len(str2)):
        smallest_len = len(str1)
    else:
        smallest_len = len(str2)
    num_of_edits = 0
    for _ in range(smallest_len):
        if(str1[i] == str2[j]):
            i += 1
            j += 1
        elif(str1[i+1] == str2[j] and num_of_edits==0):
            i+=2
            j+=1
            num_of_edits += 1
        elif(str1[i] == str2[j+1] and num_of_edits==0):
            i+=1
            j+=2
            num_of_edits += 1
        elif(str1[i+1] == str2[j+1] and num_of_edits==0):
            i+=2
            j+=2
            num_of_edits += 1
        else:
            return False
    return True
            



print(One_Away("pale", "ple")) #true
print(One_Away("pales", "pale")) #true
print(One_Away("pale", "bale")) #true
print(One_Away("pale", "bake")) #false


