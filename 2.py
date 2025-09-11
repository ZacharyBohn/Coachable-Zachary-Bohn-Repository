# Time: O(n)
# Space: O(n)
#
# Time to complete: 28:47

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        answer_node = answer
        carry = 0
        n1 = l1
        n2 = l2
        while n1 or n2 or carry > 0:
            # get values
            if n1:
                v1 = n1.val
            else:
                v1 = 0
            if n2:
                v2 = n2.val
            else:
                v2 = 0
            # sum
            curr_sum = v1 + v2 + carry
            carry = 0
            # calculate carry
            if 10 <= curr_sum < 20:
                curr_sum -= 10
                carry = 1
            elif curr_sum >= 20:
                curr_sum -= 20
                carry = 2
            # expand answer linked list
            answer_node.next = ListNode()
            answer_node = answer_node.next
            answer_node.val = curr_sum
            # move vars over to next step
            if n1:
                n1 = n1.next
            if n2:
                n2 = n2.next
        return answer.next

        

'''
answer: 748
4 -> 5 -> 6
4 -> 9

total = 748
power = 2
carry = 1
sum = 7


---

value = sum values

5 + 9 = 14
if > 10:
    carry over += 1
elif > 20:
    carry over += 2
# maxes at 27 so this works

true value = (value + carry over) * (10^step)

'''