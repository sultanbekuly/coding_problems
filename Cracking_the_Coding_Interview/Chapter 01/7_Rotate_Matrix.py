
# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the 
# image is 4 bytes, write a method to rotate the image by 90 degrees. 
# Can you do this in place?
# Hints:#51, #100

# 4 bytes.. - 32–bit Size - int - long
# rotate the image to 90 degrees in which direction? clockwise? counterclockwise?

#get size of the input array
#create same size new array 
#create index variables for both of the array and make them iterate in own right way
#fill in the new array
#return new array

#We can do in this in place by doing replacement of 4 items in one moment 

#TC - O(N^2) where matrix size is NxN 
#SC - O(N^2) where matrix size is NxN 

def Rotate_Matrix(arr:int)->int: #clockwise
    print(arr)
    arr_len = len(arr)
    new_arr = [[0 for _ in range(arr_len) ] for _ in range(arr_len) ]
    #i, j = 0,0          #arr iterator     #>i++ >j++
    x, y = 0,len(arr)-1 #new_arr iterator #>y-- >x++ #x,y;0,4;1,4;2,4;3,4
    for i in range(arr_len):
        for j in range(arr_len):
            new_arr[x][y] =  arr[i][j]
            x+=1
        y-=1
        x=0
    return new_arr

arr = [
    [ 1,  2,  3,  4,  5],
    [ 6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]]
print(Rotate_Matrix(arr))
# [[21, 16, 11, 6, 1],
#  [22, 17, 12, 7, 2],
#  [23, 18, 13, 8, 3],
#  [24, 19, 14, 9, 4],
#  [25, 20, 15, 10, 5]]

arr2 = [
    [ 1,  2,],
    [ 3,  4,]]
print(Rotate_Matrix(arr2))
# [[3, 1],
#  [4, 2]]


#TC - O(N^2) where matrix size is NxN 
#SC - O(1)
def Rotate_Matrix_inplace(arr):#counter clockwise
    print(arr)
    #arr[0,4], arr[4,4], arr[4,0], arr[0,0] = arr[4,4], arr[4,0], arr[0,0], arr[0,4]
    #arr[1,4], arr[4,3], arr[3,0], arr[0,1] = arr[4,3], arr[3,0], arr[0,1], arr[1,4]
    #arr[2,4], arr[4,2], arr[2,0], arr[0,2] = arr[4,2], arr[2,0], arr[0,2], arr[2,4]
    #arr[3,4], arr[4,1], arr[1,0], arr[0,3] = arr[4,1], arr[1,0], arr[0,3], arr[3,4]
    #    | |---i---| |       | |---x---| |     i--| |       | |---x---| |       | |--i
    #    |--j        |---y---|        j--|          |---y---|           |---j---|
    #need to do something like this
        #note arr[3,4] should be arr[3][4]
    #i in range(len(arr)//2+1) and x in reversed(range(len(arr)//2+1)) OR x = len(arr)-i-1
        #i should be reversed one
    #j in range(len(arr)-1) and y in reverse(range(len(arr)-1))  OR y = len(arr)-j-1
    
    for x in range(len(arr)//2): #range(len(arr)//2+1) not +1 because central item is not changed:)
        i = len(arr)-1-x
        for j in range(x, len(arr)-1-x): #starting position increases, fininsh position decreases
            y = len(arr)-1-j
            #print(i,x,j,y)
            arr[j][i], arr[i][y], arr[y][x], arr[x][j] = arr[i][y], arr[y][x], arr[x][j], arr[j][i]
        #print(x,i,arr)
    return arr

print("Rotate_Matrix_inplace")
arr = [
    [ 1,  2,  3,  4,  5],
    [ 6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]]
print(Rotate_Matrix_inplace(arr))
#[[5, 10, 15, 20, 25], 
# [4, 9, 14, 19, 24], 
# [3, 8, 13, 18, 23], 
# [2, 7, 12, 17, 22], 
# [1, 6, 11, 16, 21]]

arr2 = [
    [ 1,  2,],
    [ 3,  4,]]
print(Rotate_Matrix_inplace(arr2))
# [[2, 4],
#  [1, 3]]


print(arr2[- 1][0])



# Type Name 32–bit Size 64–bit Size 
# char      1 byte      1 byte 
# short     2 bytes     2 bytes 
# int       4 bytes     4 bytes 
# long      4 bytes     8 bytes 
# long long 8 bytes     8 bytes 
