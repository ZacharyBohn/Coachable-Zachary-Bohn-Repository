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
# breadth first / level-order
# there is only one kind of breadth first, which is level order
# uses a queue to process all nodes at the current level
# before moving onto the children (from the queue)
def breadth_first():
	pass

# Below are all depth first searches
def post_order_dfs():
	pass

def pre_order_dfs():
	pass

def post_order_dfs():
	pass


# Whenever there are two types of data -> greedy
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

