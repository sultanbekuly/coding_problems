# """
# https://leetcode.com/problems/maximum-width-of-binary-tree/
# Related Topics
# Tree
# Depth-First Search
# Breadth-First Search
# Binary Tree


# Somehow we need to track: 
#     depth of the tree,
#     most left 
#     most right

# By using these three parameters we can get the width

# - We need to check every node
# - We can stop if it is the only node going down

# 0     1
#      / \
# 1   3   2 
#    / \ / \
# 2 5  3 n  9

#      1
#     / \
#    3   2        --2
#   / \ / \
#     5 6. 7      --W=3 and 5 somehow should know that the W should be decremented
#     5 6         --W=2 and 6 somehow should know that the W should be decremneted


#      1
#     / \
#        2 
#       / \
#       6  7

# if path = left num = num*2
# if path = right num = num*2+1

# this will do following:
# 0|    1
#  |   / \
# 1|  2   3 
#  | / \ / \
# 2|4  5 6  7

# and by subtracting from most right most left , +1 we can get len
# 7-4+1 = 4


# Queue: [ (node, num, level) (root-node:1, 1, 0)]

# bfs get from queue the top val
# lvl_min_num = 1     = num if lvl_min_num > num else lvl_min_num
# lvl_max_num = 1     = num if lvl_max_num < num else lvl_max_num
# max_diff    = 0     = lvl_max_num - lvl_min_num + 1 

# #reset values if level is changed
# lvl_min_num = num if lvl != last level
# lvl_max_num = num if lvl != last level

# # add to the queue new values
# queue.add(node.left,  num*2,    lvl+1)
# queue.add(node.right, num*2+1,  lvl+1)


# """
# #create queue

# class Qnode:
#     def __init__(self, node, num, lvl):
#         self.node = node
#         self.num = num
#         self.lvl = lvl

# class Queue:
#     def __init__(self):
#         self.top = None
#         self.tail = None
#         return None

#     def add
#     remove
#     pick
#     isEmpty
    

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:








# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
	def widthOfBinaryTree(self, root : TreeNode) -> int:
		"""
		:type root: TreeNode
		:rtype: int
		"""
		width_map = defaultdict(list)
		def helper(root , depth , column):
			if root is None :
				return 
			
			# Add column position to map 
			# width_map[1] = [0,1] <- 0 for 3 and 1 for 2.
			width_map[depth].append(column)

			
			left_col = column*2 # Calculate Left Column Position
			right_col = column*2 + 1 # Calculate Right Column Position

			left = helper(root.left , depth + 1 , left_col)   
			right = helper(root.right , depth + 1 , right_col)   

		helper(root, 0 , 0 )
		result = 0

		for key in width_map:
			min_val = min(width_map[key]) # Find Minimum for Each Level
			max_val = max(width_map[key]) # Maximum for Each Level
			if result < (max_val - min_val): # Compare Diff with result 
				result = int(max_val - min_val)

		# # # since we are counting from 0 ....to n-1 ex. 0 ,1,2,3 
		# # # total no of nodes are four .. thefoere we return +1 in final result 
		return result + 1