import heapq

# Runtime O(n log n)
# Space O(k)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for num in nums:
            heapq.heappush(h, num)
            if len(h) > k:
                heapq.heappop(h)
        return heapq.heappop(h)
'''

option 1 heap
option 2 quick select

'''