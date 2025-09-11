# Time: O(n)
# Space: O(1)
#
# Time to complete: 9:05
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymmetricHelper(root.left, root.right)
    
    def isSymmetricHelper(
        self,
        node1: Optional[TreeNode],
        node2: Optional[TreeNode],
            ) -> bool:
        # XOR
        if (node1 is None) != (node2 is None):
            return False
        if node1 is None and node2 is None:
            return True
        if node1.val != node2.val:
            return False
        return self.isSymmetricHelper(node1.left, node2.right) and \
            self.isSymmetricHelper(node1.right, node2.left)



'''
  1
 2  2
3 4 4 3

is sym:
2, 2


----

if only root -> true

isSymmetricHelper(node1, node2) -> bool

either both are null, or both are not null
both node values are the same
isSymmetricHelper(node1.left, node2.right)
and
isSymmetricHelper(node1.right, node2.left)


'''