from collections import deque

# Runtime: O(m * n)
# Space: O(m + n)
# since the bfs queue will hold at most 2m and 2n
# at a time.
#
# Time to complete: 17:20
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid[0]), len(grid)
        visited = set()
        max_size = 0
        for y in range(N):
            for x in range(M):
                if grid[y][x] and (y,x) not in visited:
                    size = self.bfs(grid, visited, x, y, M, N)
                    max_size = max(max_size, size)
        return max_size

    
    def bfs(self, grid, visited, x, y, M, N) -> int:
        q = deque([(y,x)])
        visited.add((y,x))
        size = 1
        while q:
            y, x = q.popleft()
            for dy, dx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                ny, nx = y + dy, x + dx
                if (0 <= ny < N and 0 <= nx < M) and \
                    grid[ny][nx] and \
                    (ny,nx) not in visited:
                    q.append((ny,nx))
                    visited.add((ny,nx))
                    size += 1
        return size
        

'''
think in general terms first.
the problem is finding the largest connected component.

no adj list for this problem since building the adj list
would be a lot more work without being needed. For an island
there would be n entries, n = number of cells of that island.
instead we can just perform a single bfs per island.

loop through all cells of the grid
bfs all connected 1's
global visited set
keep track of max size
'''