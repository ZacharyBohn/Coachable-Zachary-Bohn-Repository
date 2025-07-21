# Updated Code

# nit: changed to tabs for indentation

from collections import deque

# Changed class name to PascalCase
# and changed name from NetworkNode -> Node
class Node:
	def __init__(self, type: str, value: int):
		self.type = type
		self.value = value

# Added to make it very clear what the row, column tuple is
class GridCoordinate:
	def __init__(self, row: int, col: int):
		self.row = row
		self.col = col
	
	# This will simplify some syntax below
	def __add__(self, other) -> GridCoordinate:
		if not isInstance(other, GridCoordinate):
			raise Exception(f'Can\'t add GridCoordinate with {type(other)}')
		return GridCoordinate(self.row + other.row, self.col + other.col)

def check_connected(grid: List[List[Node]], max_diff: int) -> bool:
	# Add sizes of the grid as constants for enhanced readability
	ROWS, COLS = len(grid), len(grid[0])

	# Changed to visited
	# should follow typical conventions unless there is a
	# good reason to deviate
	visited = set()

	# Created start / end coord for enhanced readability
	start_coord, end_coord = GridCoordinate(0, 0), GridCoordinate(ROWS-1, COLS-1)

	# Changed to a deque
	# 4 things are wrong here
	# 1. It was named Q even though it was a stack
	# 2. A BFS is better for finding paths since it has more
	#	predictable performance
	# 3. Didn't follow naming conventions or styling. Changed to coord_queue
	#	since we are storing grid coord location, not nodes
	# 4. nit: should add a comment here to specify what is in the queue or
	#	create a class to specify this. I opted to create a class GridCoordinate
	#	this also let's us create a start and end node
	coord_queue = deque([GridCoordinate(0,0)])

	# nit: can just check if queue is not empty using below syntax
	while coord_queue:
		# Changed to popleft since we are now using BFS
		# Changed to coord
		coord = coord_queue.popleft()

		# Added this here for readability / to remove
		# duplicate code below
		node = get_node(coord, grid)


		# It is pointless to deconstruct a coord, just to reconstruct it
		# All following instances of this will be changed without comment.
		#
		# Should prefer guard clauses to deep nesting
		#
		# nit: Don't need to check visited here for BFS.
		# Prefer to check for visited / add to visited
		# during neighbor traversal.

		# Changed to use end_coord
		if coord == end_coord:
			return True

		# I believe there are several dormant bugs here in how
		# boundaries are being tested. The code is functional,
		# but confused. I moving this logic to a helper function
		# and cleaned it up.
		#
		# These if blocks are duplicating a lot of logic.
		# If instead of re-applying the valid neighbor logic
		# to every potential neighbor, potential neighbors
		# should be generated, and checked in a loop.
		# I've made this change below.
		#
		# Also, lots of naming styling wasn't followed, that's been updated.
		#
		# The code was also generally confusing to reason about, this
		# has been updated as well.
		for neighbor_coord in get_neighbors(coord, ROWS, COLS):
			neighbor = get_node(neighbor_coord)
			if neighbor_coord in visited:
				continue
			if (node.type == neighbor.type or
				abs(node.value - neighbor.value) <= max_diff):
				coord_queue.append(neighbor_coord)
				visited.add(neighbor_coord)

	# Removed needless check for end node here

	return False

def get_node(coord: GridCoordinate, grid: List[List[Node]]) -> Node:
	return grid[coord.row][coord.col]

def is_coord_in_bounds(coord: GridCoordinate, ROWS: int, COLS: int) -> bool:
	return 0 <= coord.row < ROWS and 0 <= coord.col < COLS

def get_neighbors(coord: GridCoordinate, ROWS: int, COLS: int) -> List[GridCoordinate]:
	'''
	Generates all neighbors of coord within the bounds of ROWS, COLS
	'''
	directions = [GridCoordinate(-1, 0), GridCoordinate(1, 0), GridCoordinate(0, -1), GridCoordinate(0, 1)]
	neighbors = []
	for delta in directions:
		neighbor = coord + delta
		if is_coord_in_bounds(coord, ROWS, COLS):
			neighbors.append(neighbor)
	return neighbors
			
