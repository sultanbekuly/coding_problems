# 599. Minimum Index Sum of Two Lists.py
#https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
#iterate through list1 by adding its items to hashmap1 with its index
# iterate through list2 
#   check if item exists in the hashmap1
#   if so add their index sum to hashmap_sum = {0:["a"], 1:["b","c"]}
#iterate through hashmap_sum 
#   get minimal key and return its array

#TC - O(N+M) N is len of list1, M is len of list2
#SC - O(N)      #hashmap_sum cannot be bigger than hashmap1
def findRestaurant(list1, list2):
    print(list1, list2)
    hashmap1 = {}
    for i in range(len(list1)):
        hashmap1[list1[i]] = i
    #print("hashmap1:", hashmap1)
    hashmap_sum = {}
    for i in range(len(list2)):
        if list2[i] in hashmap1.keys():
            index_sum = i + hashmap1[list2[i]]
            #print("i",i)
            #print("list2[i]",list2[i])
            #print("hashmap1[list2[i]]",hashmap1[list2[i]] )
            
            if(index_sum in hashmap_sum):
                hashmap_sum[index_sum].append(list2[i])
            else:
                hashmap_sum[index_sum] = [list2[i]]
    #print("hashmap_sum",hashmap_sum)
    minimal_sum = len(list1) + len(list2) #maximum posible sum +2
    for i in hashmap_sum.keys():
        minimal_sum = min(i,minimal_sum)
    #print("hashmap_sum[minimal_sum]:",minimal_sum,hashmap_sum[minimal_sum])
    return hashmap_sum[minimal_sum]

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
print(findRestaurant(list1, list2))
# Output: ["Shogun"]
# Explanation: The only common string is "Shogun".

list1 = ["Shogun","Tapioca Express","Burger King","KFC"] 
list2 = ["KFC","Shogun","Burger King"]
print(findRestaurant(list1, list2))
# Output: ["Shogun"]
# Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.

list1 = ["happy","sad","good"]
list2 = ["sad","happy","good"]
print(findRestaurant(list1, list2))
# Output: ["sad","happy"]
# Explanation: There are three common strings:
# "happy" with index sum = (0 + 1) = 1.
# "sad" with index sum = (1 + 0) = 1.
# "good" with index sum = (2 + 2) = 4.
# The strings with the least index sum are "sad" and "happy".
