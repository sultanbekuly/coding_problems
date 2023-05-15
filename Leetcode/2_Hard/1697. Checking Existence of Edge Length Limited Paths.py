"""
https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/
Related Topics
Array
Union Find
Graph
Sorting

"""
class UnionFind:
    def __init__(self, n):
        self.id = list(range(n))
        self.rank = [0] * n

    def unionByRank(self, u, v):
        i = self.find(u)
        j = self.find(v)
        if i == j:
            return
        if self.rank[i] < self.rank[j]:
            self.id[i] = j
        elif self.rank[i] > self.rank[j]:
            self.id[j] = i
        else:
            self.id[i] = j
            self.rank[j] += 1

    def find(self, u):
        if self.id[u] == u:
            return u
        self.id[u] = self.find(self.id[u])
        return self.id[u]


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ans = [False] * len(queries)
        uf = UnionFind(n)

        for i in range(len(queries)):
            queries[i].append(i)

        queries.sort(key=lambda x: x[2])
        edgeList.sort(key=lambda x: x[2])

        i = 0  # i := edgeList's index
        for query in queries:
            # Union edges whose distances < limit (query[2])
            while i < len(edgeList) and edgeList[i][2] < query[2]:
                uf.unionByRank(edgeList[i][0], edgeList[i][1])
                i += 1
            if uf.find(query[0]) == uf.find(query[1]):
                ans[query[3]] = True

        return ans
