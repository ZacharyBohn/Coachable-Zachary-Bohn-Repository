from typing import List

# the first solution that I came up with
class Solution1:
	def longestConsecutive(self, nums: List[int]) -> int:
		hashset = set(nums)
		longest_seq = 0
		for n in nums:
			if n-1 in hashset: continue
			current_seq = 1
			while n+1 in hashset:
				current_seq += 1
				n += 1
			longest_seq = max(longest_seq, current_seq)
		return longest_seq

# the second and best solution I came up with
class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = {}
        longest = 0
        for n in nums:
            if n in hashset: continue
            start, end = n, n
            if n-1 in hashset: start = hashset[n-1][0]
            if n+1 in hashset: end = hashset[n+1][1]
            # to be able to skip duplicates of n
            hashset[n] = None
            hashset[start] = [start, end]
            hashset[end] = [start, end]
            longest = max(longest, end - start + 1)
        return longest

# another version of the second solution that I did
# just because
#
# in the hashset is stored n, start, end as
# {n*2: start, n*2+1: end}
# this just takes advantage of the fact that I am storing
# 2 values for each number, the currently known start
# and the currently known end
class Solution3:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = {}
        longest = 0
        for n in nums:
            n2 = n*2
            if n2 in hashset: continue
            start, end = n2, n2
            if n2-2 in hashset: start = hashset[n2-2]
            if n2+2 in hashset: end = hashset[n2+3]
            # to be able to skip duplicates of n
            hashset[n2] = None
            hashset[start] = start
            hashset[start+1] = end
            hashset[end] = start
            hashset[end+1] = end
            longest = max(longest, (end // 2) - (start//2) + 1)
        return longest