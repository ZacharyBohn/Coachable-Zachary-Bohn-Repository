# Time: O(n)
# Space: O(1)
#
# Time to complete: 19:46


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        # start of next jump window
        start = 1
        far = nums[0]

        # first iteration manually
        # calculated above
        for i in range(1, n):
            if i == start:
                jumps += 1
                start = far + 1
            far = max(far, i + nums[i])
        
        return jumps


'''
[1,1,1,1,0]
       |
i = 4
s = 4
j = 4
far = 4

BFS
 0  1    2
[1, 2, 1, 1, 1, 0]
       |  |
jump = 0
end = 0
far = nums[0]

for i:
    if can reach end:
        break
    if can go farther:
        update far
    if i == end:
        update jumps


return jump



'''

# Time: O(n^2)
# Space: O(n)
#
# Time to complete: 42:39

import math


class Solution2:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        jumps = [math.inf] * len(nums)
        jumps[-1] = 0
        jumps[-2] = 1
        for i in range(len(nums) - 3, -1, -1):
            span = jumps[i:i+nums[i]+1]
            if len(span) > 0:
                jumps[i] = min(span) + 1
        return jumps[0]


'''
[2,3,1,1,4]

0 1 2 1 2


always possible to reach the end
get minimum amount of jumps, given nums

[?] -> answer is 0
[1+, ?] -> answer is 1

go backwards and count quickest ways to get
to the end.

[1, 1, 0] -> 2
[2, 1, 0] -> 1


[1, 2, 1, 0] -> 2
    |
    v
[2, 1, 1, 0]


build secondary array
start at 0
i = len(nums) - 1
decrement i
min(nums[i-1]+1, i)


last number is 0
next is 1
perform the jump, add 1


4 1 3 1 1 0 0
3 3 2 3 2 1 0

if you hit a number, then you can skip building

min of all possible jumps + 1

O(n^2)

'''