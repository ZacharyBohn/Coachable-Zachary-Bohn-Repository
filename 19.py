# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1 and head.next == None:
            return None
        current = head
        previous = None
        i = 1
        while current.next != None:
            current = current.next
            if i == n:
                previous = head
            if i > n:
                previous = previous.next
            i += 1
        if previous == None:
            head = head.next
        else:
            previous.next = previous.next.next
        return head