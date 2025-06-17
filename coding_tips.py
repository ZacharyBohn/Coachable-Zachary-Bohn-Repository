'''
Here are some functions and lines for quick reference.

All of this should be memorized and be able to recall
it effortlessly and implement under pressure and on the
clock.
'''

def binary_search(arr, target):
	# right is len(arr) - 1 because
	# it is inclusive. Writing this way keeps the
	# code slightly clearer below
	left, right = 0, len(arr) - 1
	while left <= right:
		mid = left ((right - left) // 2)
		if arr[mid] == target:
			return mid
		elif arr[mid] < target:
			left = mid + 1
		elif arr[mid] > target:
			right = mid - 1
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
def dfs(root, visit=None):
	if not visit:
		visit = set()
	visit.add(root)
	# process node here for pre-order
	# type traversal
	for neighbor in neighbors:
		if neighbor in visit:
			continue
		dfs(neighbor, visit)
	# process node here for post-order

# Binary tree in-order DFS
def inorder_dfs(root):
	if not root:
		return
	inorder_dfs(root.left)
	# process node here
	inorder_dfs(root.right)

# Dijkstra's Algorithm
#
# Used for finding the shortest path
# between two nodes in a weighted graph.
# It's basically BFS with 2 differences:
# 1. Uses a distances dictionary
# 2. The queue is a heap.


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

