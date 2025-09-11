# Time: O(n)
# Space: O(1)
#
# Time to complete: 4:10

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow, fast = head, head.next
        while slow and fast:
            if slow is fast:
                return True
            if not fast.next:
                break
            fast = fast.next.next
            slow = slow.next
        return False

'''
two pointer solution is optimal for this
fast, slow
increment fast by 2, and slow by 1
if they meet, then there is a cycle
if fast finds the end the list, there is no cycle
'''