import random

# get kth smallest element
# k is 0-based
#
# eg
# k = 2
# arr=[0, 1, 1, 1, 2]
#            ^
# ans: 1
def quickselect(arr, k):
	if len(arr) == 1:
		return arr[0]

	pivot = random.choice(arr)

	lows = [x for x in arr if x < pivot]
	highs = [x for x in arr if x > pivot]
	pivots = [x for x in arr if x == pivot]

	if k < len(lows):
		# lows to be further filtered
		return quickselect(lows, k)
	elif k < len(lows) + len(pivots):
		# 
		return pivot
	else:
		return quickselect(highs, k - len(lows) - len(pivots))
