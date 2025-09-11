# Runtime: O(log n)
# Space: O(1)
#
# Time to complete: 32:33
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            # guard against out of bounds
            if mid-1 < 0:
                mid_left = -float('inf')
            else:
                mid_left = nums[mid-1]
            if mid+1 >= N:
                mid_right = -float('inf')
            else:
                mid_right = nums[mid+1]
            if mid_left < nums[mid] and nums[mid] > mid_right:
                return mid
            if mid_left >= nums[mid]:
                # there is peak to the left
                # so go left
                right = mid - 1
            else:
                left = mid + 1
        # this should never run
        raise Exception('No peak found')

'''
Option 1:
modified binary search
instead of checking if mid == target
we will check if mid-1 < mid < mid+1
and have a way to ensure that mid-1 and mid+1 = inf
if they are out of bounds

However, the array is not sorted, so why use binary search?

Option 2:
first number that is not greater than the previous is next to the answer?
yes.

what would a helper function look like that determines if the answer
is to the left?
it would take the value of nums[0], value of nums[n]
wouldn't work.

[0, 1, 2, 3, 2, 5, 4]
 ^        ^     ^  ^

0 - 3
len = 4
dif = 3

len = 7
dif = 4

len = 4
dif = 1


Not trying to answer the question is there is no peak within a range.
Only trying to answer if there is necessarily a peak with a range.

Compare length and differences of values?
No.

If right is less than left, then there must be a peak

Ok.

Modified binary search:
a range contains a peak if left > right
a index is valid if its higher than its neighbors
This solution should work.

=====

left >= mid:
then there is a peak between left and mid

'''