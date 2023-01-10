#URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
#has sufficient space at the end to hold the additional characters, and that you are given the "true"
#length of the string. (Note: If implementing in Java, please use a character array so that you can
#perform this operation in place.)
#EXAMPLE
#Input: "Mr John Smith ", 13
#Output: "Mr%20John%20Smith"

def URLify(str, len):
    print(str, "-", len)
    new_str = ""
    for i in range(len):
        if(str[i]==" "):
            new_str += "%20"
        else:
            new_str += str[i]
    return new_str

print(URLify("Mr John Smith ", 13))

