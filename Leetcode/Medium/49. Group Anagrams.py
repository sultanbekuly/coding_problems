#49. Group Anagrams
#https://leetcode.com/problems/group-anagrams/description/

#array_of_HM
#res_arr_of_arr = []
#for word in strs:
#   create hashmap of lettercount for the word  | {e:1,a:1,t:1}
#   iterate through array_of_HM   | [{e:1,a:1,t:1},{t:1,a:1,n:1}]
#       check if array_of_HM[i] == word_HM
#           res_arr_of_arr[i].append(word)
#       else: add it to array_of_HM
#              res_arr_of_arr.append([word])
#

#TC - O(N^2)
#SC - O(N)  N - number of elements in strs 

def groupAnagrams( strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    array_of_HM = []
    res_arr_of_arr = []
    for word in strs:
        temp_hm = {}
        for i in word:
            if i in temp_hm:
                temp_hm[i] += 1 #increment
            else:
                temp_hm[i] = 1 #initiate
        #word hm is created - temp_hm
        in_array_of_HM_flag = False
        for x in range(len(array_of_HM)):
            if array_of_HM[x] == temp_hm: #check if it works
                res_arr_of_arr[x].append(word)
                in_array_of_HM_flag = True
                break
        if( not(in_array_of_HM_flag)): #if(len(array_of_HM)==0):
            array_of_HM.append(temp_hm)
            res_arr_of_arr.append([word])
    print(array_of_HM)
    return res_arr_of_arr

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

strs = [""]
print(groupAnagrams(strs))
# Output: [[""]]        

strs = ["a"]
print(groupAnagrams(strs))
# Output: [["a"]]

#it takes too long and takes too much memory