class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0

        max_left = [0] * n
        running_max = height[0]
        max_right = [0] * n
        for i in range(n):
            running_max = max(running_max, height[i])
            max_left[i] = running_max
        running_max = height[n-1]
        for i in range(n-1, -1, -1):
            running_max = max(running_max, height[i])
            max_right[i] = running_max
        
        total = 0
        # the first and last elements can't
        # hold water, so skip them
        for i in range(1, n-1):
            h = height[i]
            min_peak = min(max_left[i], max_right[i])
            total += max(0, min_peak - h)
        
        return total