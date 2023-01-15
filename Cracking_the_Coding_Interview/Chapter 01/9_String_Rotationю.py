# String Rotation: Assume you have a method isSubstringwhich checks 
# if one word is a substring of another. 
# Given two strings, s1 and s2, write code to check if s2 is a rotation 
# of s1 using only one call to isSubstring (e.g.,"waterbottle" is a rotation of"erbottlewat").
#  Hints:#34,#88, #704

# simplest test is to check if their length is the same
# next, create new_s2 = s2 + s2
# so we will have erbottlewaterbottlewat
# where we can see the s1 in the erbottle'waterbottle'wat
# iterate through range(len(s1))
#   check if s1 == new_s2[i:len(s1)]
#       if so return True
# after loop return False

#TC - O(N) - N is len of s1/s2
#SC - O(N^2)
# takes up too much memory - find a way to do it with less memory - solved below String_Rotation2
def String_Rotation(s1, s2):
    print(s1,s2)
    if(len(s1)!=len(s2)):
        return False
    new_s2 = s2+s2
    print("new_s2:",new_s2)
    for i in range(len(s1)):
        if(s1 == new_s2[i:len(s1)+i]):
            return True
    return False

print(String_Rotation('waterbottle', 'erbottlewat'))#True
print(String_Rotation('foo', 'bar'))#False
print(String_Rotation('foo', 'foofoo'))#False

#TC - O(N) - N is len of s1/s2
#SC - O(N)
def String_Rotation_2(s1, s2):
    print(s1,s2)
    if(len(s1)!=len(s2)):
        return False
    for i in range(len(s1)):
        new_s2 = s2[i:] + s2[:i]
        # print("new_s2:",new_s2)
        if(s1 == new_s2):
            return True
    return False

print("String_Rotation_2")
print(String_Rotation_2('waterbottle', 'erbottlewat'))#True
print(String_Rotation_2('foo', 'bar'))#False
print(String_Rotation_2('foo', 'foofoo'))#False

# ('waterbottle', 'erbottlewat', True),
# ('foo', 'bar', False),
# ('foo', 'foofoo', False)




#if i in hashmap.keys():
#for i in hashmap.values():