from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(lambda: 0)
        left = 0
        max_len = 0
        for right in range(len(s)):
            counts[s[right]] += 1
            if self.isWindowInvalid(left, right, k, counts):
                counts[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len

    
    def isWindowInvalid(self, left: int, right: int, k: int, counts) -> bool:
        most_common_char_count = max(counts.values())
        window_size = right - left + 1
        return (window_size - most_common_char_count) > k