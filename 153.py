class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left <= right:
            # if left->right array is sorted correctly
            if nums[left] < nums[right]:
                return nums[left]
            if left + 1 == right:
                return nums[right]
            i = left + ((right - left) // 2)
            value = nums[i]
            if nums[left] < value:
                # cut off left side
                left = i
            elif nums[right] > value:
                # cut off right side
                right = i