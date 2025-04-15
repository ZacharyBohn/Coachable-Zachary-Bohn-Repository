class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = len(nums)
        if count == 0: return []
        if count == 1: return nums

        prefix = [1] * count
        running_prefix = 1
        for i in range(count):
            prefix[i] = running_prefix
            running_prefix *= nums[i]

        suffix = [1] * count
        running_suffix = 1
        for i in range(count-1, -1, -1):
            suffix[i] = running_suffix
            running_suffix *= nums[i]

        answer = [1] * count
        for i in range(count):
            answer[i] = prefix[i] * suffix[i]

        return answer


