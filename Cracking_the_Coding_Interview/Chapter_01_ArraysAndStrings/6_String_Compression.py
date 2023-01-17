
# String Compression: Implement a method to perform basic string compression using 
# the counts of repeated characters. 
# For example, the string aabcccccaaa would become a2b1c5a3. 
# If the "compressed" string would not become smaller than the original string, 
# your method should return the original string. 
# You can assume the string has only uppercase and lowercase letters (a - z).
# Hints:#92, #110

#Get the length of the input string
#create array and new string len counter
# in the array will be stored new string one by one ['a2','b1'...]
# go through the input string with while loop
#  check if the current char is equal to next char
#   if so update counter
#  else reset counter and append char with counter to arr
#       and update new_str_len_counter += char(1) need to check counter length
#           (convert to string and get len  or  some manipulations with %10..)
# and in the compare input_str_len and new_str_len_counter
#   and return corresponding string
#       in case of new string: convert arr to string

#TC - O(N) where N is len of input string
#SC - O(N) where N is number of elements in the arr

def string_Compression(input:str)->str:
    print(input)
    arr=[]
    new_str_len = 0
    counter = 1 #for each char
    for i in range(len(input)):        
        if(i+1<=len(input)-1): #check if i+1 allowed
            if(input[i] == input[i+1]):
                counter += 1
            else:  
                arr_append_val,new_str_len,counter  = the_else(input[i], counter, new_str_len)
                arr.append(arr_append_val)                
        else:  #only works for last char
            arr_append_val,new_str_len,counter  = the_else(input[i], counter, new_str_len)
            arr.append(arr_append_val)   
    print(arr, new_str_len)
    if(len(input) < new_str_len):
        return input
    else:
        return "".join(arr)

def the_else(the_char,counter,new_str_len):
    arr_append_val = ((the_char+str(counter)))
    new_str_len += 1+len(str(counter)) 
    counter_val = 1 #reset counter
    return arr_append_val, new_str_len, counter_val

print(string_Compression("aabcccccaaa")) #a2b1c5a3
print(string_Compression("abc")) #abc

print("string_Compression2")
def string_Compression2(input:str)->str:
    arr=[]
    counter = 0
    for i in range(len(input)):
        if(i!=0 and input[i]!=input[i-1]):
            arr.append(input[i-1]+str(counter))
            counter = 0
        counter += 1 
    #adding the last item
    arr.append(input[i-1]+str(counter))
    return min(input, ''.join(arr), key=len)

print(string_Compression2("aabcccccaaa")) #a2b1c5a3
print(string_Compression2("abc")) #abc

#if(i+1<=len(input)-1): #check if i+1 allowed
#=>if(i!=0 and input[i]!=input[i-1]):

#str(number)

#return min(input, ''.join(arr), key=len)

