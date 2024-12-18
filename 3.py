from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            window = SlidingWindow()
            for c in s:
                if window.has_char(c):
                    window.remove_duplicate(c)
                window.expand(c)
            return window.get_max()

class SlidingWindow:
    def __init__(self):
        self._window = deque()
        # used only for fast lookup
        self._hashset = set()
        self._max = 0
        return
    def has_char(self, c) -> bool:
        return c in self._hashset
    def remove_duplicate(self, c) -> None:
        '''
        removes characters from array until c is
        removed. Assumes that c is in the array.
        '''
        while True:
            x = self._window.popleft()
            self._hashset.remove(x)
            if x == c:
                break
        return
    def expand(self, c) -> None:
        self._window.append(c)
        self._hashset.add(c)
        self._max = max(self._max, len(self._window))
        return
    def get_max(self) -> int:
        '''
        returns the highest max seen so far
        '''
        return self._max