from collections import deque

# Runtime: O(n) worst case
# Space: O(n) worst case
# n = number of grid cells
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # note: technically ROWS will always equal COLS
        # but their seperation is more clear / flexible
        ROWS = len(grid)
        COLS = len(grid[0])
        target = (ROWS - 1, COLS - 1)
        if grid[0][0] == 1 or grid[target[0]][target[1]] == 1:
            return -1
        # 8 directions to nodes's neighbors
        dirs = []
        for row in range(-1, 2, 1):
            for col in range(-1, 2, 1):
                if row == 0 and col == 0:
                    continue
                dirs.append((row, col))
        # queue contains:
        # row, column
        start = (0, 0)
        q = deque([start])
        visit = set([start])
        distances = {start: 1}
        while q:
            node = q.popleft()
            node_row, node_col = node
            node_dist = distances[node]
            # process node
            if node == target:
                return node_dist
            # generate list of neighbors from grid
            neighbors = []
            for direction in dirs:
                row_delta, col_delta = direction
                row, col = node_row + row_delta, node_col + col_delta
                is_out_of_bounds = row < 0 or row >= ROWS or col < 0 or col >= COLS
                if is_out_of_bounds or grid[row][col] == 1:
                    continue
                neighbors.append((row, col))
            # add unvisited neighbors to queue
            for neighbor in neighbors:
                if neighbor in visit:
                    continue
                q.append(neighbor)
                visit.add(neighbor)
                distances[neighbor] = node_dist + 1
        return -1


'''
Can think of this problem as just a graph problem.
0's are nodes.
1's are not nodes.

Option 1:
Convert the grid into an adjacency list. O(n) time
Perform a BFS from start to end, tracking number of
nodes crossed.

Option 2:
Perform BFS without adj list
Let's do this one. Navigating the grid shouldn't be
that difficult. And this will improve runtime.
Converting into an adj list will just complicate
things.
'''