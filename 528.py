# Runtime: O(log n)
# n = len(w)
#
# Space: O(n)
# n = len(w)
class Solution:
    def __init__(self, w: List[int]):
        self.total = 0
        self.ranges = []
        for x in w:
            # [inclusive, exclusive] range
            self.ranges.append([self.total, self.total+x])
            self.total += x

    def pickIndex(self) -> int:
        seed = random.randint(0, self.total - 1)
        left, right = 0, len(self.ranges) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if seed >= self.ranges[mid][0] and seed < self.ranges[mid][1]:
                # target found
                return mid
            elif seed < self.ranges[mid][0]:
                right = mid - 1
            elif seed >= self.ranges[mid][1]:
                left = mid + 1
            else:
                raise Exception('error in binary search')
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

'''
3, 5 ->

[0, 3] = 3 - 0 = length of 3
   [3, 8] = 8 - 3 = length of 5

'''