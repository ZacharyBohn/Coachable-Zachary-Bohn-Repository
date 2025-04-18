class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) // 2)

            if target == nums[mid]:
                return mid

            if nums[left] <= nums[mid]:
                # left side is sorted
                if nums[left] <= target and target < nums[mid]:
                    # target may be to the left
                    right = mid - 1
                else:
                    # target may be to the right side
                    left = mid + 1
            else:
                # right side is sorted
                if nums[mid] < target and target <= nums[right]:
                    # target may be to the right side
                    left = mid + 1
                else:
                    # target may be to the left
                    right = mid - 1
        
        return -1