'''
Visited: nodes that have been processed.
'''


def traversal(adj: Dict[str, List[str]], startnode):
	'''
	Template traversal function that can be easily
	adapted to:
	- BFS
	- DFS
	'''
	datastructure = [startnode]
	visited = set()
	while datastructure:
		# eval
		node = datastructure.pop()

		# proc
		# ...
		# this always necessary
		visited.add(node)

		# trav
		for nei in adj[node]:
			if nei not in visited:
				datastructure.append(node)

def bfs(adj, start):
	q = deque([start])
	visited = set()
	while q:
		# eval
		node = q.popleft()

		# proc
		# ...
		visited.add(node)

		# trav
		for neighbor in adj[node]:
			if neighbor not in visited:
				q.append(neighbor)
	return

def dfs(adj):
	stack = [adj.keys()[0]]
	visited = set()
	while stack:
		# eval
		node = stack.pop()

		# proc
		# ...
		visited.add(node)

		# trav
		for neighbor in adj[node]:
			if neighbor not in visited:
				stack.append(neighbor)
	return

# visited set should be passed into
# a recursive DFS
def dfs_recur(adj, start, visited):
	# eval
	if node in visited:
		return
	
	# proc
	# ...
	visited.add(node)

	# trav
	for neighbor in adj[node]:
		if neighbor not in visited:
			dfs_recur(adj, neighbor, visisted)


'''
assume adjlist is weighted
adjlist: {
	A: [(B, 4), (C, 3)]
}

Prims is used for build an MST
from a weighted undirected graph.
'''
def prims(adj):
	# heap node: (weight, dest, src) 
	heap = [(0, adjlist.keys()[0], None)]
	visited = set()
	edgelist = set()
	while heap:
		#evaluation
		weight, node, parent = datastructure.pop()
		if node in visited:
			# this makes sure we don't add a higher
			# weighted edge to the edgelist after
			# we've already gotten a lower one
			# from the heap
			continue

		#processing
		if parent is not None:
			# max, min used here for consistency in
			# creating the edge list
			edgelist.add((min(node, parent), max(node, parent), weight))
		visited.add(node)


		#traversal
		for nei, n_weight in adj[node]:
			if nei in visited:
			datastructure.append((n_weight, nei, node))

	return edgelist

'''
Assuming no cycle and directed graph
i.e. DAG
'''
def top_sort1(adj):
	#Check for cycle if cannot assume no cycle.

	visited = set()
	top_order = []
	dfs_postorder(adj, node=adj.keys()[0], visited, top_order)

	top_order.reverse()
	return top_order

def dfs_postorder(adj, node=adj.keys()[0], visited, top_order):
	# evaluation
	if node in visited:
		return

	# Traversal
	for neighbor in adj[node]:
		if neighbor not in visited:
			dfs_recur(adj, neighbor, visisted)

	# processing
	top_order.append(node)
	visited.add(node)


def top_sort2(adj):
	q = deque([adj.keys()[0]])
	visited = set()

	#preprocess indegree list
	indegree = defaultdict(int)
	for src, neighbors in adj.items():
	for nei in neighbors:
		indegree[nei] += 1 

	top_order = []

	while q:
		# evaluation
		node = q.popleft()

		# processing
		top_order.append(node)
		visited.add(node)

		# Traversal
		for neighbor in adj[node]:
			if neighbor in visited:
			continue
			if indegree[neighbor] > 0:
			indegree[neighbor] -= 1
			continue
			q.append(neighbor)

	return top_order
