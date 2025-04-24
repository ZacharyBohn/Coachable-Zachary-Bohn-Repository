from string import ascii_lowercase
from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_counts = defaultdict(int)
        window_counts = defaultdict(int)
        for x in s1:
            s1_counts[x] += 1
        # doing len(s1)-1 here might be a bit weird?
        # keeps the code farther down more concise tho
        for x in s2[:len(s1)-1]:
            window_counts[x] += 1
        # main iteration
        # both pointers are inclusive
        left = 0
        for right in range(len(s1) - 1, len(s2)):
            window_counts[s2[right]] += 1
            if self.isEqual(s1_counts, window_counts):
                return True
            window_counts[s2[left]] -= 1
            left += 1
        return False

    def isEqual(self, s1_counts: int, window_counts: dict[str, int]):
        if len(s1_counts) != len(window_counts):
            return False
        for x in s1_counts:
            if s1_counts[x] != window_counts[x]:
                return False
        return True
