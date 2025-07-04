'''
Here are some functions and lines for quick reference.

All of this should be memorized and be able to recall
it effortlessly and implement under pressure and on the
clock.
'''

def binary_search(arr: List[int], target: int) -> int:
	lo, hi = 0, len(arr) - 1
	while lo <= hi:
		# this line always stays the same
		# regardless if you are running
		# bisect left or bisect right
		mid = (lo + hi) // 2
		# optional: if dups don't matter
		#if arr[mid] == target:
		#	return mid
		#
		# optional: if you want to bisect right
		#if target < arr[mid]:
		if arr[mid] < target:
			# mneumonic device:
			# since we are adjusting "lo" in the
			# if statement, this algorithm will return
			# the lowest value of all dups.
			lo = mid + 1
		else:
			hi = mid - 1
	return -1

# Index Edges
# No overlap, no skipped values, all elements covered
# length of each segment can easily be calculated by
# end - start
# start is inclusive
# end is exclusive
arr = [2, 4, 6, 8, 10]
arr[0:3] # returns [2, 4, 6]
arr[3:5] # returns [8, 10]


# Useful string manipulation
x = '/home//test/'
x.split('/')
# returns ['', 'home', '', 'test', '']
# one element before and after each character split

'asdfjkl39999f'.isalnum() == True
';adsf9f'.isalnum() == False

'38383'.isdigit() == True
'3333f'.isdigit() == False

'    banana  '.strip() # returns 'banana'

y = ['hello', 'there']
'.'.join(y) # returns 'hello.there'
# if you need a . before or after, you can simply add that manually
'.' + '.'.join(y) + '.'

''.join(y) # return 'hellothere'

# quick access to string lists
# placing them into a set guarentees O(1) lookup time
# though it is often unnecessary
import string
LOWERS = set(string.ascii_lowercase)
DIGITS = set(string.digits)
LETTERS = set(string.ascii_letters)
PUNCTUATIONS = set(string.punctuation)
WHITESPACES = set(string.whitespace)

# Cypher / encryption style problems.
#
# Use these 3 steps to keep ints between a - z
# or between A - Z
# -Bring down to base 0
# -Perform modulo
# -Bring back up to base ord('a'), ie 97
# in implementation this is
# value = ord(char) - ord('a')
# value %= 26
# new_char = chr(value + ord('a'))
#
# ord('a') = 97
# the next 25 lowercase letters follow
#
# ord('A') = 65
# the next 25 uppercase letters follow

# Sorting
def quick_sort():
	pass

def merge_sort():
	pass

def selection_sort():
	pass

def insertion_sort():
	pass

# Tree Traversals
#
# When traversing graphs, this template should be followed
# unless there is a specific reason not to:
# 1. Node Evaluation (select next node)
# 2. Node Processing (perform work on selected node)
# 3. Graph Traversal (add neighbors to queue / stack)
#
# breadth first / level-order
# there is only one kind of breadth first, which is level order
#
# Binary tree BFS
def bfs(root):
	queue = deque([root])
	while queue:
		node = queue.popleft()
		# process node
		if node.left:
			queue.append(node.left)
		if node.right:
			queue.append(node.right)

# Graph BFS
def bfs(root):
	q = deque([start])
	# visit / visited is perhaps a poor label
	# something like enqueued would be better
	# since items in this set have not yet been
	# processed, but they have been enqueued.
	# However, this should be used to keep
	# convention.
	visit = set([start])
	while q:
		node = q.popleft()
		# process node
		for neighbor in neighbors:
			# node could have neighbors that are
			# neighbors of each other. This guards
			# against adding any one node more than
			# once.
			if neighbor in visited:
				continue
			q.append(neighbor)
			visit.add(neighbor)

# Below are all depth first searches
def dfs(root, visit, graph):
	visit.add(root)
	# process node here for pre-order
	# type traversal
	for neighbor in graph[root]:
		if neighbor in visit:
			continue
		dfs(neighbor, visit)
	# process node here for post-order
#
# call this function with:
dfs(root, set())

# Binary tree in-order DFS
def inorder_dfs(root):
	if not root:
		return
	inorder_dfs(root.left)
	# process node here
	inorder_dfs(root.right)

# TODO: update these if necessary to ensure that they
# follow Tim's graph template.

# assume the graph is an adjacency list
adj = defaultdict(list)
def directed_graph_has_cycle(adj) -> bool:
	visited = set()
	path = set()

	# to call this for every node in the graph
	# because there may be more than one component
	# the visited set will be used to unnecessary work
	# is not performed.
	for node in adj:
		if node in visited:
			continue
		if directed_graph_has_cycle_helper(node, adj, path, visited):
			return True
	
	return False

def directed_graph_has_cycle_helper(node, adj, path, visited) -> bool:
	if node in path:
		# cycle detected
		return True
	if node in visited:
		# already checked this path
		# and no cycles were detected.
		return False
	
	path.add(node)
	visited.add(node)

	for neighbor in adj[node]:
		if directed_graph_has_cycle_helper(neighbor, adj, path, visited):
			return True
	
	path.remove(node)
	return False

# assume the graph is an adjacency list
adj = defaultdict(list)
def undirected_graph_has_cycle(adj) -> bool:
	visited = set()
	# this for loop is only necessary since the graph
	# may contain multiple components
	for node in adj:
		if node in visited:
			# this node's component has been proven
			# to not be in a cycle.
			continue
		# this helper function will visit every node
		# of this node's component.
		if undirected_graph_has_cycle_helper(node, None, adj, visited):
			return True
	return False

def undirected_graph_has_cycle_helper(node, parent, adj, visited) -> bool:
	visited.add(node)
	for neighbor in adj[node]:
		if neighbor == parent:
			# ignore parent-child relationship
			continue
		if neighbor in visited:
			# we've seen a node twice (barring child-parent
			# relationship), which means there is a cycle
			return True
		if undirected_graph_has_cycle_helper(neighbor, node, adj, visited):
			return True
	return False


# Dijkstra's Algorithm
#
# For finding the shortest path
# between two nodes in a weighted graph.
adj: Dict[str, int] = defaultdict(list)
def dijkstra_shortest_paths(graph, start_node) -> Dict[str, int]:
	# Shortest known distance from start_node to each node
	shortest_distance = {node: float('inf') for node in graph}

	# Priority queue of (distance_from_start, node_to_visit)
	frontier = [(0, start_node)]
	shortest_distance[start_node] = 0

	while frontier:
		current_distance, current_node = heapq.heappop(frontier)

		# Ignore if we already found a shorter path to this node
		if current_distance > shortest_distance[current_node]:
			continue

		for neighbor_node, edge_weight in graph[current_node]:
			distance_via_current = current_distance + edge_weight

			if distance_via_current > shortest_distance[neighbor_node]:
				continue
			
			shortest_distance[neighbor_node] = distance_via_current
			heapq.heappush(frontier, (distance_via_current, neighbor_node))

	return shortest_distance


# Whenever there are two types of data -> think greedy algorithm.
# Can determine if the problem can be greedy; by trying to give an example
# where a greedy algorithm won’t work. If you can’t think of any examples,
# then greedy will likely work.

# Framework
#
# Understand problem.
# Try to gain a solid intuitive understanding for all relevant cases by
# working through them manually. Do this by walking through SEVERAL examples of
# data. In this stage, think of it as playing with the data in order to learn.
# Identify the technique (try to consider several if necessary)
# Identity the implementation (how to modify the technique for this
# specific example.)
# Write the code.
# Walk an example through the code (since there is no access to a debugger).
# Adjust as necessary. Be wary of adjustments at this stage, since there
# is a danger of cascading changes.

