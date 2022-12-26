
def binary_search(list, item, min, max):
    mid = max//2
    if(max==min):
        return None

    guess = list[mid]    
    if(guess == item):
        return mid
    elif(guess > item):
        return binary_search(list, item, min, mid)
    else:
        return binary_search(list, item, mid+1, max+1)


my_list = [1,3,5,7,9]

print( binary_search(my_list, 3, 0, len(my_list)) ) # => 1
print( binary_search(my_list, -1, 0, len(my_list)) )# => None