class Solution:
    def average(self, salary: List[int]) -> float:
        maxs = salary[0]
        mins = salary[0]
        sums = float(0)
        for i in salary:
            sums += i
            maxs = i if i > maxs else maxs
            mins = i if i < mins else mins
        sums = sums - maxs - mins
        return sums/(len(salary)-2)