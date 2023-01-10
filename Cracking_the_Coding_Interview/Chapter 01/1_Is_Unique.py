#Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?
# Hint #44, #117, # 132 
# Answer pg. 192 

# What if you cannot use additional data structures?
# ->
    #Sort the string - O(NlogN)
    #Then, Search for duplicates by going through the sorted string by pairs O(N)
    #Overall time complexity is O(NlogN)

#time complexity is O(n)/O(1) as we will not iterate more than 128 items.
#space compelexity is O(1) - 128 
def is_Unique (input: str ) -> bool:
    print(input)
    if(len(input) > 128):
        return False
    charset = [False for _ in range(128)]
    for i in input:
        val = ord(i)
        #print(i,"-",val)
        if(charset[val] == True):
            return False
        charset[val] = True
    return True
print( is_Unique("cba"))
print( is_Unique("cbc"))


#charset = [False for _ in range(128)] -> fill the array with 128 False values

#ord(char) -> provides ASCII numeric representation of the char

