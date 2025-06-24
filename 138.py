# Time: O(n)
# Space: O(n)
#
# Time to complete: 25:33

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapp = {}
        mapp[None] = None

        node = head
        dummy = Node(0)
        copy = dummy
        # copy val and next pointers
        while node:
            copy.next = Node(node.val)
            copy = copy.next
            mapp[node] = copy
            node = node.next
        
        # reset head nodes
        node = head
        copy = mapp[node]
        # copy random pointers
        while node:
            if node.random is not None:
                copy.random = mapp[node.random]
            node = node.next
            copy = copy.next
        
        return dummy.next
            

'''
[[1,1],[2,1]]

new: [1,1] -> [2,?] 

old = 1
new = 1
map[1 old] = 1 new
map[2 old] = 2 new




loop through the linked list O(n)
and create copies
make a hashmap of old: new while doing so
loop through both lists again
following the path through the hashmap
to build the random pointers of the new list


hash map {
    old: new
}

2 -> 3 -> 5
          |
^----------


2 -> 3 -> 5


'''