from string import ascii_lowercase, ascii_uppercase

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        min_size = float('inf')
        res = [-1, -1]
        window = Window(s, t)
        while True:
            if window.is_valid():
                if window.size() < min_size:
                    res = [window.left, window.right]
                    min_size = window.size()
                window.shrink()
            else:
                if window.right == len(s) - 1:
                    break
                window.expand()
        
        if min_size == float('inf'):
            return ""
        return s[res[0]:res[1]+1]

class Window:
    def __init__(self, s: str, t: str) -> None:
        self.s: str = s
        self.t: str = t
        self.left = 0
        self.right = 0
        # represents how many chars in the window are equal to 
        # or greater than the amount of chars in t
        self.matches = 0
        self.window_counts = {}
        self.t_counts = {}
        for x in ascii_lowercase + ascii_uppercase:
            self.window_counts[x] = 0
            self.t_counts[x] = 0
        for i in range(len(t)):
            self.t_counts[t[i]] += 1
        self.window_counts[s[0]] += 1
        for x in self.t_counts:
            if self.window_counts[x] >= self.t_counts[x]:
                self.matches += 1
        return
    
    def is_valid(self) -> bool:
        # 26 uppercase, 26 lowercase
        return self.matches == 52
    
    def shrink(self) -> None:
        if self.window_counts[self.s[self.left]] == self.t_counts[self.s[self.left]]:
            self.matches -= 1
        self.window_counts[self.s[self.left]] -= 1
        self.left += 1
        return
    
    def expand(self) -> None:
        self.right += 1
        self.window_counts[self.s[self.right]] += 1
        if self.window_counts[self.s[self.right]] == self.t_counts[self.s[self.right]]:
            self.matches += 1
        return
    
    def size(self) -> int:
        return self.right - self.left + 1
