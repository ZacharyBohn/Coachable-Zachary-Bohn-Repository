# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        _, __, lca = self.lcaHelper(root, p, q)
        return lca


    def lcaHelper(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> (bool, bool, 'TreeNode'):
        '''
        Returns (has_p, has_q, lca)
        '''
        if root == None:
            return (False, False, None)

        left_has_p, left_has_q, left_lca = self.lcaHelper(root.left, p, q)
        if left_lca:
            return (True, True, left_lca)
        
        right_has_p, right_has_q, right_lca = self.lcaHelper(root.right, p, q)
        if right_lca:
            return (True, True, right_lca)

        cur_has_p = (root == p) or left_has_p or right_has_p
        cur_has_q = (root == q) or left_has_q or right_has_q

        cur_lca = None
        if cur_has_p and cur_has_q:
            cur_lca = root
       
        return (cur_has_p, cur_has_q, cur_lca)