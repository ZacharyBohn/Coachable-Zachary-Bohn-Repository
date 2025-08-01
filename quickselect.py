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





def quick_select(nums, k):
	def partition(left, right):
		pivot = nums[right]
		swap = left
		while left < right:
			if nums[left] < pivot:
				nums[left], nums[swap] = nums[swap], nums[left]
				swap += 1
			left += 1
		nums[right], nums[swap] = nums[swap], nums[right]
		return swap
	
	left, right = 0, len(nums) - 1

	while left <= right:
		pivot_idx = partition(left, right)
		if pivot_idx == (k-1):
			return nums[pivot_idx]
		elif pivot_idx < (k-1):
			left = pivot_idx + 1
		else:
			right = pivot_idx - 1
		



