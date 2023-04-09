"""
https://leetcode.com/problems/clone-graph/description/

Create new Node
    assign the node val
    check if the node has heighbours
    for n in neighbors
        repeat

return first node wich will have link to every node
--
add to this logic that we need to check if node copy has been already created

 #[1 [2 [1 [..], 3[2 [..],4[..]] ], 4[1,3 [2[..],4[..]] ]]]

"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if(node == None):
            return None

        oldToNew = {} # key - old node, value - new node

        def copy_dfs(node):
            if(node in oldToNew):
                return oldToNew[node]
            copy_node = Node(node.val)
            oldToNew[node] = copy_node
            for nei in node.neighbors:
                copy_node.neighbors.append( copy_dfs( nei ) )
            
            return copy_node

        return copy_dfs(node)
        

       