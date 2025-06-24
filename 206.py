# Time: O(n)
# Space: O(1)
#
# Time to complete: 2:59

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None
        while node:
            n = node.next
            node.next = prev
            prev = node
            node = n
        return prev