import unittest

class Solution:
	def asteroidCollision(self, asteroids):
		asteroids_state = []
		for asteroid in asteroids:
			asteroids_state.append(asteroid)
			while (len(asteroids_state) > 1 and 
					asteroids_state[-2] > 0 and 
					asteroids_state[-1] < 0):
				right = asteroids_state.pop()
				left = asteroids_state.pop()
				if abs(right) == abs(left):
					continue
				elif abs(right) > abs(left):
					asteroids_state.append(right)
				else:
					asteroids_state.append(left)
		return asteroids_state

'''
if negative and stack
	- pop from stack, compare collision
else
	add to output

stack
for ast in asteroids
'''

class TestCases(unittest.TestCase):
	def test_case_1(self):
		sol = Solution()
		self.assertEqual(sol.asteroidCollision([5, 10, -5]), [5, 10])

	def test_case_2(self):
		sol = Solution()
		self.assertEqual(sol.asteroidCollision([8, -8]), [])

	def test_case_3(self):
		sol = Solution()
		self.assertEqual(sol.asteroidCollision([10, 2, -5]), [10])

	def test_case_4(self):
		sol = Solution()
		self.assertEqual(sol.asteroidCollision([-2, -1, 1, 2]), [-2, -1, 1, 2])

	def test_case_5(self):
		sol = Solution()
		self.assertEqual(sol.asteroidCollision([1, -2, -2, -2]), [-2, -2, -2])

if __name__ == "__main__":
	unittest.main()
