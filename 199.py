from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Runtime: O(n)
# Space: O(log n)
# n = number of nodes
#
# Time to complete: 14:26
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        if not root:
            return answer
        q = deque([root])
        right_most = root
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if node == right_most:
                answer.append(node.val)
                if q:
                    right_most = q[-1]
                else:
                    right_most = None
        return answer


'''
Option 1
level order traversal and a stack for each level
After a full traversal, return the top element of
each stack.
Actually, don't need to record stacks,
just need to record the right most node
at each level.

How to know what level you are on?
At the root level, you know
add you will know what the last node is at the next level
because it will be the last element in the queue
Once that node

variable
right_most = root
if node == right_most, then add it to the answer
and after adding the children of the right most node
the new right most will be the last node in the q


'''