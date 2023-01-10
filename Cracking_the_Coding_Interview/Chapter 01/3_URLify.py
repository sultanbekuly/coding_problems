#URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
#has sufficient space at the end to hold the additional characters, and that you are given the "true"
#length of the string. (Note: If implementing in Java, please use a character array so that you can
#perform this operation in place.)
#EXAMPLE
#Input:  "Mr John Smith    ", 13
#Output: "Mr%20John%20Smith"

#TC is O(N)
#Uses new string so SC is O(N)
def URLify(str, length):
    print(str, "-", length)
    new_str = ""
    for i in range(length):
        if(str[i]==" "):
            new_str += "%20"
        else:
            new_str += str[i]
    return new_str
print(URLify("Mr John Smith    ", 13))

#TC is O(N)
#SC is O(1)
def URLify2(str, length): #str is list of chars
    print(str, "-", length)
    j = len(str)-1
    for i in reversed(range(length)):
        if(str[i]==" "):
            str[j-0] = "0"
            str[j-1] = "2"
            str[j-2] = "%"
            j -= 3
        else:
            str[j] = str[i]
            j -= 1
    return str
print(URLify2(list("Mr John Smith    "), 13))

