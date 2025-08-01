from collections import deque
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        alice = 0

        adj_list = defaultdict(list)

        for start, end in edges:
            adj_list[start].append(end)
            adj_list[end].append(start)

        leafs = set()
        
        for node, edges in adj_list.items():
            if len(edges) == 1 and node != 0:
                leafs.add(node)
        
        
        # Find Bob's Path. There is only 1 path between 2 nodes in a tree.
        bob_path = []
        visited = set()
        def dfs(node: int) -> list:
            if node in visited:
                return None
            if node == 0:
                return [node]
            visited.add(node)
            for neighbor in adj_list[node]:
                cur_path = dfs(neighbor)
                if cur_path:
                    cur_path.append(node)
                    return cur_path 

            return None

        bob_path = dfs(bob)
        bob_path = bob_path[::-1]
        opened_gates = set()
        alice_queue = deque([(0, 0, 0)])
        max_profit = float('-inf')
        visited = set()
        bob_current = bob
        while len(alice_queue) > 0:
            node, profit, level = alice_queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            if level < len(bob_path):
                bob_current = bob_path[level]
            opened_gates.add(bob_current)
            
            if bob_current == node:
                profit += amount[node] // 2
            elif node in opened_gates:
                profit += 0
            else:
                profit += amount[node]
         
            if node in leafs:
                max_profit = max(max_profit, profit)
            else:
                for neighbor in adj_list[node]:
                    alice_queue.append((neighbor, profit, level + 1))

        return max_profit