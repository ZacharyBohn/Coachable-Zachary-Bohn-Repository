from collections import deque
from typing import Dict, List

# Runtime: O(m * n)
# Space: O(m * n)
#
# Time to complete: 14:04
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # build adjacency list
        adj = self.genAdjList(grid)
        visited = set()
        max_size = 0
        # bfs for all nodes
        for node in adj:
            size = self.getIslandSize(node, adj, visited)
            max_size = max(max_size, size)
        return max_size
    
    def genAdjList(self, grid) -> Dict[Tuple[int, int], List[Tuple[int, int]]]:
        M, N = len(grid[0]), len(grid)
        adj = {}
        for y in range(N):
            for x in range(M):
                if grid[y][x] == 1:
                    adj[(y,x)] = []
        _dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for node in adj:
            for dy,dx in _dirs:
                ny,nx = node[0] + dy, node[1] + dx
                if not (0 <= ny < N and 0 <= nx < M):
                    continue
                if grid[ny][nx] == 0:
                    continue
                adj[node].append((ny,nx))
        return adj
    
    def getIslandSize(self, node, adj, visited) -> int:
        # bfs on node to get island size
        q = deque([node])
        visited.add(node)
        size = 0
        while q:
            curr = q.popleft()
            size += 1
            for n in adj[curr]:
                if n in visited:
                    continue
                q.append(n)
                visited.add(n)
        return size



'''
General graph terms / problem solving.
High level stuff:

Searching for largest connected component.
Cells within the grid are nodes.

Convert adj list
perform bfs for each node in that list
while tracking max size seen, and keeping a global visited set.

'''