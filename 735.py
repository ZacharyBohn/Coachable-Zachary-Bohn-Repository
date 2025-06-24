# Time: O(n)
# Space: O(n)
#
# Time to complete: 14:59
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while True:
                if len(stack) == 0:
                    # no collision
                    stack.append(a)
                    break
                if a < 0 and stack[-1] >= 0:
                    # collision
                    abs_a, abs_last = abs(a), abs(stack[-1])
                    if abs_a >= abs_last:
                        stack.pop()
                    if abs_a <= abs_last:
                        break

                else:
                    # no collision
                    stack.append(a)
                    break
        return stack