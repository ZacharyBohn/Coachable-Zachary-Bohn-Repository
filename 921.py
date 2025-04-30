class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        inbalances = 0
        num_opens = 0
        for c in s:
            if c == '(':
                num_opens += 1
            elif num_opens == 0:
                inbalances += 1
            else:
                num_opens -= 1
        return num_opens + inbalances
'''
Main case:
balance the number of opens and closes

Edge case 1:
)(
number of opens / closes are equal,
but answer should be two

inbalance variable and stack
opens added to stack
closes remove from stack
answer = inbalance + len(stack)

can just use a int variable instead of stack
since there is only one type of enclosement
'''