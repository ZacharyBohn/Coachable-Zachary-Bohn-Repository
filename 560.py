# Runtime: O(n)
# Space: O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # ss = subarray sum
        ss, answer = 0, 0
        prefix_sums = defaultdict(int)
        # since not removing a prefix
        # is an option
        prefix_sums[0] = 1
        for num in nums:
            ss += num
            answer += prefix_sums[ss-k]
            prefix_sums[ss] += 1
        return answer


'''
Brute force method:
- check every possible subarray
- sum the subarray
- check if that equals k
O(n^3)

Optimization 1:
use a prefix sum array:
no longer need to sum the subarray since we can use
prefix_sums[j] - prefix_sums[i-1]
O(n^2)

Optimization 2:
instead of a prefix sums array, use a hash map
only need to consider each num once as a possible
ending point of a candidate subarray.
Then the prefix sums map will tell us if there are
any prefixes that we can remove to make a valid
subarray (ending at num).
We can find this by using map[k-sum]
O(n)

Steps
loop through nums once
num will be considered the end of the current subarray
being considered
keep track of the sum of the subarray
prefix_sums hashmap will track of how many of
each prefix we have seen thus far.
subarray sum - k gives us how much we need to
remove from the current subarray to make it a valid answer.
prefix_sums will track how many of each prefix we have seen.
so just increment answer by prefix_sums[ss - k]

'''