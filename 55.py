# Time: O(n)
# Space: O(1)
#
# Time to complete: 18:26
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # first jump
        i = nums[0]

        # jump continually until we reach the
        # end or dead end
        while True:
            if i >= (len(nums) - 1) or nums[i] >= (len(nums) - 1):
                return True
            if i == 0:
                return False
            if nums[i] == 0:
                # in dead end
                dead_end = i
                while i + nums[i] <= dead_end:
                    i -= 1
                    if i == 0:
                        return False
            i += nums[i]

'''
Let's try to solve it backwards

[?] -> true
[1+, ?] -> true

ok, so there's a pattern of:
if nums[i] >= (len(nums) - 1):
    return True

beyond this, algorithm will be faster
if we can find bigger numbers

can bring average time to solve up by
jumping ahead (maybe)

jump as far as you can, if you are stuck,
then backtrack until you can go further

farthest index = nums[i] + i

1. Loop through every element and keep updating a "max index reachable" var
2. Jump as far as possible, back track only as necessary

Backtracking path:

(8:00 in so far, just for planning)

new i = i + nums[i]
if cant go forward
continually decrement i by 1 until either:
1. you've reached passed the dead end
2. you hit 0

'''