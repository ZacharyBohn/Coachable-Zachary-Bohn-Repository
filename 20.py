# Time: O(n)
# Space: O(n)
#
# Time to complete: 3:45
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = []
        for c in s:
            if c in pairs:
                # closing
                if len(stack) == 0:
                    return False
                if pairs[c] != stack[-1]:
                    return False
                stack.pop()
            else:
                # opening
                stack.append(c)
        
        return len(stack) == 0

'''
if there is a close and the stack is empty -> invalid
if there is a close and the last element of the stack is not its open -> invalid
if open -> append to stack
if close and there is a paring opening -> pop from stack
return len(stack) == 0
'''