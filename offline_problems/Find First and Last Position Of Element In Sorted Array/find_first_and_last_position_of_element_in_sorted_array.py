import unittest

'''
Your approach must run in O(log n) in the worst-case. Even if there are duplicates.

Follow up questions

What is the condition you use to search the right or the left side of the arrays?
How does this change if the array is rotated sorted?
'''

class Solution:
    def searchRange(self, nums, target):
        pass  # Placeholder for the actual solution

class TestCases(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.searchRange([5,7,7,8,8,10], 8), [3,4])

    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.searchRange([5,7,7,8,8,10], 6), [-1,-1])

    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.searchRange([], 0), [-1,-1])

    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.searchRange([1], 1), [0,0])

    def test_case_5(self):
        sol = Solution()
        self.assertEqual(sol.searchRange([2,2,2,2,2], 2), [0,4])

if __name__ == "__main__":
    unittest.main()
