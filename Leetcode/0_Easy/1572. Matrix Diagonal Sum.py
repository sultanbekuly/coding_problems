class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        x = 0
        for y in range(len(mat)):
            z = (y+1) * -1
            # print(mat[y], mat[y][y], mat[y][z] )
            x += mat[y][y]
            x += mat[y][z]

        if(len(mat)%2 == 1):#odd matrix
            # print("odd")
            mid = floor( (len(mat)-1) /2 )
            x -= mat[mid][mid]
        
        return x