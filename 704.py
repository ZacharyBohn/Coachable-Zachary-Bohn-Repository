class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0; right = len(nums) - 1
        while left <= right:
            i = left + ((right - left) // 2)
            value = nums[i]
            if value == target:
                return i
            elif value < target:
                left = i + 1
            elif value > target:
                right = i - 1
        return -1
        