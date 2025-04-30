# Definition for a binary tree node.
# class TreeNode:
# 	def __init__(self, val=0, left=None, right=None):
# 		self.val = val
# 		self.left = left
#		self.right = right

# Runtime: O(n)
# n = number of nodes
# Space : O(n) worst case
class Solution:
	def maxDepth(self, root: Optional[TreeNode]) -> int:
		if not root:
			return 0
		return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


'''
leaf node, max depth = 1
any other node, max depth = max(maxDepth(all children))
'''
