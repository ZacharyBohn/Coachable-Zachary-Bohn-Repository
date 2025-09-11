"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

# Runtime: O(n + m)
# Space: O(n)
# n = height of the binary tree
# m = number of nodes
#
# Time to completion: 41:33
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        head = root
        while head.left:
            head = head.left
        processed = set()
        stack = [root]
        previous = None
        while stack:
            # intentionally not popped here
            last = stack[-1]
            if last.left and last.left not in processed:
                stack.append(last.left)
                continue
            # process top element from stack
            node = stack.pop()
            node.left = previous
            if previous:
                previous.right = node
            processed.add(node)
            previous = node
            # then, process right child if necessary
            if node.right:
                stack.append(node.right)
        head.left = previous
        previous.right = head
        return head

'''
Notes

visualize large binary tree (10 nodes)
stack = [8, 3]

         8  
      /     \ 
     3        11
   /   \       \   
  1     5      12    
/   \  / \      \ 
0   2 4   6      13

prev_node = None
curr_node = 0

in order DFS
record first node as head obvs
use a previous node
set the current node.left to previous node
node.right to next node

use a stack because nodes need info across many layers

if node has an unprocess left child, add it to the stack, loop
otherwise process self
if node has right child, add it to the stack

what does processing look like?
link previous and current node
node.left = previous
previous?.right = node
add it to the "processed" set
previous = node

grab from stack, process node, then process right nodes if necessary

does linking break the DFS traveral?


loop
if last element has unprocessed left child, add left child to stack
else
    pop it from the stack
    process that node
    if last element has right child, add that child to the stack



'''