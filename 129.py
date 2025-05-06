# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Runtime: O(n)
# Space: O(n) worst case
# n = number of nodes
# 
# Time to complete: 21:58
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.sumHelper(root, 0)
    
    def sumHelper(self, node: TreeNode, given_value: int) -> int:
        total = node.val + (given_value * 10)
        if not (node.left or node.right):
            # base case
            return total
        
        left_value = 0
        right_value = 0
        if node.left:
            left_value = self.sumHelper(node.left, total)
        if node.right:
            right_value = self.sumHelper(node.right, total)
        return left_value + right_value


'''
Going to have to visit each node; no way around that.
Don't know the value of a node, until we reach a leaf node.

Base case, only 1 node:
return that value

For every other case:
return the sum of all children + given value

give each child, (self.val * 10) + (given value * 10) 

Simpler way to think about it:
each node's value will be:
self.value +
given value * 10 +
+ the sum of all returned values of children

This should account for if a node's value is 0.

'''