from typing import List, Tuple

import heapq
import unittest
import math

def dijkstras(src, tgt, adj) -> Tuple[int, List[str]]:
	# (weight, node, parent)
	heap = [(0, src, None)]
	# node: (parent, shortest_distance)
	visited = {}

	while heap:
		#evaluation
		weight, node, parent = heapq.heappop(heap)
		if node in visited:
			continue

		#processing
		visited[node] = (parent, weight)
		if node == tgt:
			break
		
		#traversal
		for nei, n_weight in adj[node]:
			if nei not in visited:
				heapq.heappush(heap, (weight + n_weight, nei, node))

	# Path reconstruction
	if tgt not in visited:
		return math.inf, []
	path = []
	curr = tgt
	while curr is not None:
		path.append(curr)
		curr = visited[curr][0]

	return visited[tgt][1], path[::-1]

class TestDijkstras(unittest.TestCase):

	def test_basic_path(self):
		"""
		A simple graph with a clear, direct shortest path.
		Expected: A-B-C with distance 3.
		"""
		adj = {
			'A': [('B', 1)],
			'B': [('C', 2)],
			'C': [('D', 1)],
			'D': []
		}
		src = 'A'
		tgt = 'C'
		distance, path = dijkstras(src, tgt, adj)
		self.assertEqual(distance, 3)
		self.assertEqual(path, ['A', 'B', 'C'])
		# print(f"Test 1 (Basic Path) - Passed: Distance={distance}, Path={path}")

	def test_no_path(self):
		"""
		Graph where target is unreachable from source.
		Expected: Infinite distance and empty path.
		"""
		adj = {
			'A': [('B', 1)],
			'B': [],
			'C': [('D', 5)]
		}
		src = 'A'
		tgt = 'C'
		distance, path = dijkstras(src, tgt, adj)
		self.assertEqual(distance, math.inf)
		self.assertEqual(path, [])
		# print(f"Test 2 (No Path) - Passed: Distance={distance}, Path={path}")

	def test_multiple_paths(self):
		"""
		Graph with multiple paths to the target,
		ensuring Dijkstra's finds the shortest one.
		Expected: A-C-D with distance 6, not A-B-D with distance 10.
		"""
		adj = {
			'A': [('B', 7), ('C', 2)],
			'B': [('D', 3)],
			'C': [('D', 4)],
			'D': []
		}
		src = 'A'
		tgt = 'D'
		distance, path = dijkstras(src, tgt, adj)
		self.assertEqual(distance, 6)
		self.assertEqual(path, ['A', 'C', 'D'])
		# print(f"Test 3 (Multiple Paths) - Passed: Distance={distance}, Path={path}")

	def test_source_is_target(self):
		"""
		Source and target nodes are the same.
		Expected: Distance 0 and path containing only the source node.
		"""
		adj = {
			'A': [('B', 1)],
			'B': [('C', 2)],
			'C': []
		}
		src = 'A'
		tgt = 'A'
		distance, path = dijkstras(src, tgt, adj)
		self.assertEqual(distance, 0)
		self.assertEqual(path, ['A'])
		# print(f"Test 4 (Source is Target) - Passed: Distance={distance}, Path={path}")

	def test_disconnected_graph(self):
		"""
		Graph where source and target are in different disconnected components.
		Expected: Infinite distance and empty path.
		"""
		adj = {
			'A': [('B', 1)],
			'B': [],
			'X': [('Y', 5)],
			'Y': []
		}
		src = 'A'
		tgt = 'Y'
		distance, path = dijkstras(src, tgt, adj)
		self.assertEqual(distance, math.inf)
		self.assertEqual(path, [])
		# print(f"Test 5 (Disconnected Graph) - Passed: Distance={distance}, Path={path}")

# This ensures the tests run when the script is executed directly
if __name__ == '__main__':
	unittest.main(argv=['first-arg-is-ignored'], exit=False)