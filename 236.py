# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.lcaHelper(root, p, q)[2]


    def lcaHelper(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> (bool, bool, 'TreeNode'):
        '''
        Returns (has_p, has_q, answer_node)
        '''
        # queue of children to process
        # syntax is a bit cleaner this way
        queue = []
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
        
        has_p = root == p
        has_q = root == q
        for child in queue:
            res = self.lcaHelper(child, p, q)
            if res[2]:
                return (True, True, res[2])
            has_p |= res[0]
            has_q |= res[1]
            if has_p and has_q:
                return (True, True, root)
        return (has_p, has_q, None)