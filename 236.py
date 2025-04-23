# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = []
        q_path = []
        # depth first search looking for p or q
        path = []
        visited = set()
        node = root
        while node:
            if node is p:
                p_path = [x for x in path]
                p_path.append(node)
            if node is q:
                q_path = [x for x in path]
                q_path.append(q)
            if node.left and node.left not in visited:
                path.append(node)
                visited.add(node.left)
                node = node.left
                continue
            if node.right and node.right not in visited:
                path.append(node)
                visited.add(node.right)
                node = node.right
                continue
            if path:
                node = path.pop()
                continue
            node = None

        # lca will be the last common node in their
        # paths
        lca = None
        for i in range(min(len(p_path), len(q_path))):
            if p_path[i] is not q_path[i]:
                break
            lca = p_path[i]
        return lca


'''
Option 1:
Traverse the tree, adding in parent to each node
Then trace back up from p to root
trace from q to root, first node that is in p's path
is the LCA.

Option 2:
Depth first search until p and q are found from the root.
Then you'll have two lists which are the paths of p and q.
Going backwards from the elements of p's path, check if
any exist in q's path. First one that does, is the LCA.
Can use a set to make checking faster

5's path:
[3, 5]
1's path:
[3, 1]

5's path checking
5 in 1's path: no
3 is 1's path: yes, that is the LCA

5 and 7
5's path:
[3, 5]
7's path:
[3, 5, 2, 7]

Option 3:
Depth first search while tracking the current path.
When p or q is found, add the path to that node.
Once both are found, loop through the paths until
they diverge. The last similar node is the LCA.
path's should be recorded as a list of nodes.

Option 3 is the way to go.

'''