import random

# k is 0-based
# returns the element that is the kth smallest
def kth_smallest(arr, k):
	if len(arr) == 1:
		return arr[0]
	pivot = random.choice(arr)

	lows = [x for x in arr if x < pivot]
	pivots = [x for x in arr if x == pivot]
	highs = [x for x in arr if x > pivot]

	if k < len(lows):
		return kth_smallest(lows, k)
	if k < len(lows) + len(pivots):
		return pivot
	else:
		return kth_smallest(highs, k - len(lows) - len(pivots))











