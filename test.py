from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val: Optional[int]):
        self.val = val
        self.left = None
        self.right = None

def build_tree(arr: List[Optional[int]]) -> Optional[TreeNode]:
    """Build binary tree from level-order array."""
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    index = 1

    while queue and index < len(arr):
        node = queue.popleft()

        # Left child
        if index < len(arr) and arr[index] is not None:
            node.left = TreeNode(arr[index])
            queue.append(node.left)
        index += 1

        # Right child
        if index < len(arr) and arr[index] is not None:
            node.right = TreeNode(arr[index])
            queue.append(node.right)
        index += 1

    return root

def get_tree_levels(root: TreeNode):
    """Return list of levels with TreeNode values (including None placeholders)."""
    levels = []
    queue = deque([(root, 0)])

    while queue:
        node, level = queue.popleft()
        if level == len(levels):
            levels.append([])

        levels[level].append(node.val if node else None)

        if node:
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
        else:
            # To maintain structure, add placeholders even if node is None
            queue.append((None, level + 1))
            queue.append((None, level + 1))

        # Stop if the current level is entirely None
        if all(val is None for val in levels[-1]):
            levels.pop()
            break

    return levels

def print_ascii_tree(root: Optional[TreeNode]):
    """Prints tree in ASCII art format."""
    if not root:
        print("<empty tree>")
        return

    levels = get_tree_levels(root)
    max_width = 2 ** (len(levels)) * 4  # adjust 4 for spacing

    for i, level in enumerate(levels):
        level_str = ""
        spacer = max_width // (2 ** (i + 1))
        for val in level:
            if val is None:
                level_str += " " * spacer + " " + " " * spacer
            else:
                level_str += " " * spacer + f"{val}" + " " * spacer
        print(level_str.center(max_width))

        # Print branches
        if i < len(levels) - 1:
            branch_str = ""
            for j in range(len(level)):
                left_branch = "/" if levels[i + 1][2 * j] is not None else " "
                right_branch = "\\" if levels[i + 1][2 * j + 1] is not None else " "
                branch_str += " " * (spacer - 1) + left_branch + " " + right_branch + " " * (spacer - 1)
            print(branch_str.center(max_width))

# Example usage:
arr = [31,30,48,3,None,38,49,0,16,35,47,None,None,None,2,15,27,33,37,39,None,1,None,5,None,22,28,32,34,36,None,None,43,None,None,4,11,19,23,None,29,None,None,None,None,None,None,40,46,None,None,7,14,17,21,None,26,None,None,None,41,44,None,6,10,13,None,None,18,20,None,25,None,None,42,None,45,None,None,8,None,12,None,None,None,None,None,24,None,None,None,None,None,None,9]
root = build_tree(arr)
print_ascii_tree(root)
