class SparseVector:
    def __init__(self, nums: List[int]):
        self.hashmap = {}
        for i in range(len(nums)):
            num = nums[i]
            if num != 0:
                self.hashmap[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        total = 0
        for i, num in self.hashmap.items():
            if i in vec.hashmap:
                total += num * vec.hashmap[i]
        return total

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)