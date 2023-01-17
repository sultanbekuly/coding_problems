#Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, 
# its entire row and column are set to 0.
#Hints:#17, #74, #102

#Simplest way is to iterate through the MxN matrix
# and if 0 detected set row and column to 0 by two for loops
#First issue that comes to mind is that if two zeros in one row/column, 
# algorithm will set r/c to zeros twice

#Better to create two arrays for Column and Row with size M and N, fill with 1
# Check the matrix and if zero detected set to zero according column and row arrays item
#Then update the matrix column by going through Column array if column array item is 0
# same for Row array
    #note 0 and 1 can be replaced to T/F
#hint 102 -> you can use first row and column of matrix in place of seperate row and col arrays
    #so that SC will be O(1)

#TC-O(M*N)
#SC-O(M+N)

def Zero_Matrix(matrix):
    print(matrix)
    row = [ 1 for _ in range(len(matrix))]
    col = [ 1 for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j] == 0):
                row[i] = 0
                col[j] = 0
    print(row)
    print(col)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(row[i]==0 or col[j]==0):
                matrix[i][j] = 0
    return matrix


matrix = [
    [1,  2,  3,  4,  0],
    [6,  0,  8,  9,  10],
    [11, 12, 13, 14, 15],
    [16, 0,  18, 19, 20],
    [21, 22, 23, 24, 25]]
print(Zero_Matrix(matrix))       
#  [[0,  0,   0,  0, 0],
#   [0,  0,   0,  0, 0],
#   [11, 0,  13, 14, 0],
#   [0,  0,  0,   0, 0],
#   [21, 0,  23, 24, 0]]

#TC-O(M*N)
#SC-O(1)
def Zero_Matrix2(matrix):
    print(matrix)
    r_l = len(matrix[0])    # row len
    c_l = len(matrix)       # col len
    fRowHZ = False #First Row Has Zero
    fColHZ = False #First Col Has Zero
    
    #if first col or row has 0 we will write it down for later use
    for i in range(r_l):
        if matrix[0][i] == 0:
            fRowHZ = True
            break
    for i in range(c_l):
        if matrix[i][0] == 0:
            fColHZ = True
            break
    #print("First Row,Col Has Zero:",fRowHZ, fColHZ)
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[i])):
            if(matrix[i][j] == 0):
                matrix[i][0] = 0
                matrix[0][j] = 0

    #print(matrix)
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[i])):
            if(matrix[i][0]==0 or matrix[0][j]==0):
                matrix[i][j] = 0
    #print(matrix)
    #if first Row / Col has zero, set first row / col to zeros
    if fRowHZ == True:
        for i in range(r_l):
            matrix[0][i] = 0
    if fColHZ == True:
        for i in range(c_l):
            matrix[i][0] = 0           

    return matrix


matrix = [
    [1,  2,  3,  4,  0],
    [6,  0,  8,  9,  10],
    [11, 12, 13, 14, 15],
    [16, 0,  18, 19, 20],
    [21, 22, 23, 24, 25]]
print("Zero_Matrix2")
print(Zero_Matrix2(matrix))       
#  [[0,  0,   0,  0, 0],
#   [0,  0,   0,  0, 0],
#   [11, 0,  13, 14, 0],
#   [0,  0,  0,   0, 0],
#   [21, 0,  23, 24, 0]]
