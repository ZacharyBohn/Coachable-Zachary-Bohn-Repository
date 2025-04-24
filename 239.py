import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = Window(nums, k)
        for i in range(len(nums) - k):
            res.append(window.get_max())
            window.remove(nums[i])
            window.add(nums[i+k])
        # get calculations for final window
        res.append(window.get_max())
        return res

class Window:
    def __init__(self, nums: List[int], k: int) -> None:
        self.heap = []
        self.heap.extend(nums[:k])
        # convert to max heap
        for i in range(len(self.heap)):
            self.heap[i] = -self.heap[i]
        heapq.heapify(self.heap)
        self.removals = Counts()
        return
    
    def get_max(self) -> int:
        while True:
            m = -self.heap[0]
            if self.removals.contains(m):
                self.removals.remove(m)
                heapq.heappop(self.heap)
            else:
                return m

    def remove(self, x: int) -> None:
        self.removals.add(x)
        return
    
    def add(self, x: int) -> None:
        heapq.heappush(self.heap, -x)
        return

class Counts:
    def __init__(self):
        self.counts = {}
        return
    
    def contains(self, x: int) -> bool:
        return x in self.counts
    
    def remove(self, x: int) -> None:
        self.counts[x] -= 1
        if self.counts[x] == 0:
            del self.counts[x]
        return
    
    def add(self, x: int) -> None:
        current = self.counts.get(x, 0)
        self.counts[x] = current + 1
        return
