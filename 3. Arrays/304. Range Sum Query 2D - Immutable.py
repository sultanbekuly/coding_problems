"""304. Range Sum Query 2D - Immutable 
Medium
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:
NumMatrix(int[][] matrix) initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) returns the sum of the elements of the matrix array inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
 
Example 1:
[
    [3, 0, 1, 4, 2], 
    [5, 6, 3, 2, 1], 
    [1, 2, 0, 1, 5], 
    [4, 1, 0, 1, 7], 
    [1, 0, 3, 0, 5]]
Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], 
[2, 1, 4, 3], 
[1, 1, 2, 2], 
[1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangele).
2, 0, 1, 
1, 0, 1,
0, 3, 0
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangele).
6, 3,
2, 0
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangele).
3, 2, 1,
0, 1, 5
 
 
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-105 <= matrix[i][j] <= 105
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
At most 104 calls will be made to sumRegion.
"""
#O(n) n - number of all elements
class numsMatrix:
	def __init__(self, nums):
		self.nums = nums

	def sumRegion(self, row1,col1,row2,col2):
		sum = 0 
		for i in range(row1,row2+1):
			for j in range(col1,col2+1):
				sum += self.nums[i][j]
		return sum

numMatrix = numsMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(numMatrix.sumRegion(2, 1, 4, 3)) # return 8 (i.e sum of the red rectangele).
print(numMatrix.sumRegion(1, 1, 2, 2)) # return 11 (i.e sum of the green rectangele).
print(numMatrix.sumRegion(1, 2, 2, 4)) # return 12 (i.e sum of the blue rectangele).



