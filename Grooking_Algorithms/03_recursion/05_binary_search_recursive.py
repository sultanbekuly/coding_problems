def binary_search(list, item):
    if list == []:
        return -1
    low = 0
    high = len(list)-1
    mid = (low+high) // 2
    guess = list[mid]
    if(guess == item):
        return (item)
    elif(guess > item):
        return binary_search(list[:mid], item)
    else:
        return binary_search(list[mid+1:],item)

print(binary_search([6, 7, 8, 9, 10], 8)) # -> 8
print(binary_search([6, 7, 8, 9, 10], 6)) # -> 6
print(binary_search([6, 7, 8, 9, 10], 5)) # -> -1

