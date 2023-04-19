"""
https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
Related Topics
Dynamic Programming
Tree
Depth-First Search
Binary Tree


dfs function that will get max of zigzag under its childs

dfs(node):
    l = dfs(node.left) if node.left != None else 0
    r = dfs(node.right)  if node.right != None else 0
    m = max( l, r)

    return m+1


TC:O(N)  N is numer of nodes
SC:O(1) / O(N) if we count the dfs deepth

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # print(root)
        self.max_zz = 0
        def dfs(node, path, zz_count): #path: l/r
            if self.max_zz < zz_count:
                self.max_zz = zz_count

            if path=='l':
                if node.right != None:
                    dfs(node.right, "r", zz_count + 1)
                if node.left != None:
                    dfs(node.left, "l", 1) 
            elif path=='r':
                if node.right != None:
                    dfs(node.right, "r", 1)  
                if node.left != None:
                    dfs(node.left, "l", zz_count + 1)  
            else:
                if node.right != None:
                    dfs(node.right, "r", 1)
                if node.left != None:
                    dfs(node.left, "l", 1)
            

            # m = max( l, r)
            # print("m:",m,"l:", l,"r:", r)
            # return m+1

        dfs(root, 'None', 0)
        # print("max_zz:", self.max_zz)
        return self.max_zz
















