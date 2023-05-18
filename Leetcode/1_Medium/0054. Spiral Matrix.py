# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         arr = []
#         # for 
#         for i in range(0, len(matrix[0])-1 ):
#             print("i:",i)
#             print(matrix[0][i] )
#         print("--------------------------------")
#         for j in range(0, len(matrix)-1 ):
#             print("j:", j)
#             print(matrix[j][-1])
#         print("--------------------------------")
#         for k in range(len(matrix[0])-1, 0, -1):
#             print("k:", k)
#             print(matrix[-1][k])
#         print("--------------------------------")
#         for h in range(len(matrix)-1, 0, -1 ):
#             print("h:", j)
#             print(matrix[h][0])

#         return arr

class Solution:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    if not matrix:
      return []

    m = len(matrix)
    n = len(matrix[0])
    ans = []
    r1 = 0
    c1 = 0
    r2 = m - 1
    c2 = n - 1

    # Repeatedly add matrix[r1..r2][c1..c2] to ans
    while len(ans) < m * n:
      j = c1
      while j <= c2 and len(ans) < m * n:
        ans.append(matrix[r1][j])
        j += 1
      i = r1 + 1
      while i <= r2 - 1 and len(ans) < m * n:
        ans.append(matrix[i][c2])
        i += 1
      j = c2
      while j >= c1 and len(ans) < m * n:
        ans.append(matrix[r2][j])
        j -= 1
      i = r2 - 1
      while i >= r1 + 1 and len(ans) < m * n:
        ans.append(matrix[i][c1])
        i -= 1
      r1 += 1
      c1 += 1
      r2 -= 1
      c2 -= 1

    return ans
