array1 = [1,2,3,9]
sum1 = 8

array2 = [1,2,4,4]
sum2 = 8

#Brute force solution:
def isThereSum(arr, s):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if(arr[i]+arr[j] == s):
                return True
    return False

print(isThereSum(array1,sum1))
print(isThereSum(array2,sum2))

#Hash Table solution:
def isThereSum2(arr, sum):
    dict_compl = {}
    for i in range(len(arr)):
        if(dict_compl.get(arr[i]) == True):
            return True
        else:
            dict_compl[sum-arr[i]] = True
    return False

print(isThereSum2(array1,sum1))
print(isThereSum2(array2,sum2))
