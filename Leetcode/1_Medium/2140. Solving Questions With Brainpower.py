class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        r = [0] * n
        for i in range(n - 1, -1, -1):
            b = questions[i][1]
            p = questions[i][0]
            if i == n - 1:
                r[i] = p
            elif i + b + 1 >= n:
                r[i] = max(r[i+1], p)
            else:
                r[i] = max(r[i+1], p + r[i + b + 1])
        return r[0]
