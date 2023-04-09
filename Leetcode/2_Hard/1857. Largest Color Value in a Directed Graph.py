"""
https://leetcode.com/problems/largest-color-value-in-a-directed-graph/description/
"""
"""
my - not correct
convert the edges to the graph
Node:
    val: str[index]
    directs_to: list[Nodes]

Nodes_hm = {} #key:node.val/index,#val:Node 
go through edges
    create two Nodes 
        only if the Node is not created already
        check dict of Nodes 
    append direction

check for loop by fast and slow pointers in array

go through the graph and do dfs/bfs 
    return ["acaa","b"]
---
#my
class Node:
    def __init__(self, val: str):
        self.val = val
        self.directs_to = []

"""

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)

        # print(adj)

        #Return max freq of colors
        def dfs(node):
            if node in path:
                return float("inf")
            if node in visit:
                return 0
            visit.add(node)
            path.add(node)

            colorIndex = ord(colors[node]) - ord('a')
            count[node][colorIndex] = 1

            for nei in adj[node]:
                if dfs(nei) == float("inf"):
                    return float("inf")
                for c in range(26):
                    count[node][c] = max(
                        count[node][c],
                        count[nei][c] + (1 if c==colorIndex else 0)
                    )
            path.remove(node)
            return max(count[node])

        n, res = len(colors), 0
        visit, path = set(), set()
        count = [[0] * 26 for i in range(n)] #Map count[node][color] -> max freq color
        for i in range(n):
            res = max(dfs(i), res)
        return -1 if res==float("inf") else res






