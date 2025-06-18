# Runtime: O(n)
# Space: O(n)
# 
# Time to complete: 23:33
class Solution:
	def numSquares(self, n: int) -> int:
		# remainder, count
		q = deque([(n,0)])
		visited = set()
		while q:
			r,c = q.popleft()
			if r == 0:
				return c
			for x in range(1, r+1):
				diff = r - (x * x)
				if diff in visited:
					continue
				if diff < 0:
					continue
				q.append((diff, c+1))
				visited.add(diff)
		
		return -1

'''
BFS
neighbors of n are all perfect squares up to n
queue with (remainder, count)

what if n is perfect square?

n=12
squares = [1, 4, 9, 16, 25, 36]

(12, 1)

(11, 2) (8, 2) (3, 2)

(10, 3) (7, 3) (2, 3) (7, 3) (4, 3) (2, 3)


'''