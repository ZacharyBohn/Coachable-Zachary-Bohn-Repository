class SparseVector:
    def __init__(self, nums: List[int]):
        self.hashmap = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.hashmap[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        total = 0
        smaller_vec = None
        larger_vec = None
        if len(self.hashmap) <= vec.hashmap:
            smaller_vec = self
            larger_vec = vec
        else:
            smaller_vec = vec
            larger_vec = self
        for i, num in smaller_vec.hashmap.items():
            if i in larger_vec.hashmap:
                total += num * larger_vec.hashmap[i]
        return total

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)