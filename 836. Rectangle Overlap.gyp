"""
An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.

 

Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
Example 3:

Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
Output: false
 

Constraints:

rect1.length == 4
rect2.length == 4
-109 <= rec1[i], rec2[i] <= 109
rec1[0] <= rec1[2] and rec1[1] <= rec1[3]
rec2[0] <= rec2[2] and rec2[1] <= rec2[3]
"""

def isRectangleOverlap(rec1, rec2):

    min_val = min(min(rec1),min(rec2))
    
    for i in range(4):
        rec1[i] -= min_val
        rec2[i] -= min_val
    max_val = max(max(rec1),max(rec2))
    arr_2d = [[0 for i in range(max_val+1)] for j in range(max_val+1)]

    r1_x1 = rec1[0]
    r1_y1 = rec1[1]
    r1_x2 = rec1[2]
    r1_y2 = rec1[3]

    r2_x1 = rec2[0]
    r2_y1 = rec2[1]
    r2_x2 = rec2[2]
    r2_y2 = rec2[3]
    
    arr_2d[r1_x1][r1_y1] = arr_2d[r1_x1][r1_y1] + 1
    arr_2d[r1_x2][r1_y2] = arr_2d[r1_x2][r1_y2] - 1
    
    arr_2d[r2_x1][r2_y1] = arr_2d[r2_x1][r2_y1] + 1
    arr_2d[r2_x2][r2_y2] = arr_2d[r2_x2][r2_y2] - 1
    print(arr_2d)
    counter = 0
    for i in range(max_val+1):
        for j in range(max_val+1):
            counter += arr_2d[i][j]
            if(counter==2):
                return True
    return False
        
    
    



print(isRectangleOverlap([0,0,2,2], [1,1,3,3]))#true
print(isRectangleOverlap([0,0,1,1], [1,0,2,1]))#false
print(isRectangleOverlap([0,0,1,1], [2,2,3,3]))#false

print(isRectangleOverlap([11,12,13,13], [17,1,17,19]))#false

print(isRectangleOverlap([1,1,2,2], [0,0,3,3]))#true

print(isRectangleOverlap([-1,0,1,1],[0,-1,0,1]))#false

print(isRectangleOverlap([7,8,13,15],[10,8,12,20]))#true




