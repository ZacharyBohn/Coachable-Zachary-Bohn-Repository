from collections import defaultdict

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        WIDTH, HEIGHT = len(heights[0]), len(heights)
        adj = defaultdict(list)
        for y in range(HEIGHT):
            for x in range(WIDTH):
                for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < WIDTH and 0 <= ny < HEIGHT):
                        continue
                    # edge src -> dest if
                    # src -> dest is level or goes uphill
                    # not downhill since we are tracing backwards
                    if heights[y][x] <= heights[ny][nx]:
                        adj[(y,x)].append((ny,nx))
        
        pacific_starting = []
        for x in range(WIDTH):
            pacific_starting.append((0,x))
        for y in range(HEIGHT):
            pacific_starting.append((y,0))
        atlantic_starting = []
        for x in range(WIDTH):
            atlantic_starting.append((HEIGHT-1,x))
        for y in range(HEIGHT):
            atlantic_starting.append((y,WIDTH-1))
        
        pacific_visited = self.bfs(pacific_starting, adj)
        atlantic_visited = self.bfs(atlantic_starting, adj)

        answer = []
        for node in pacific_visited & atlantic_visited:
            answer.append(list(node))
        return answer

    def bfs(self, starting, adj):
        q = deque(starting)
        visited = set(starting)
        while q:
            node = q.popleft()
            for neighbor in adj[node]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                q.append(neighbor)
        return visited



'''
How it's a graph. What are the nodes? What are the edges?
Nodes are the heights. Edges are the cardinal direction neighbors of each node, as long as the neighbor's height is less than or equal to the node's height.

What input are you given to represent the graph? How can you convert the input to an adjacency list?
Directed graph, I think? I would loop through the matrix, and check if the neighbor's height matches the water flow rules, and if they do, then add them as a neighbor to the adjacency list.

What is the general graph problem you are solving here?
Path finding: checking if a path exists from one node to another.

=====
build adj list
perform bfs from the pacific ocean uphill
same for atlantic
build answer from the visited sets of each

'''