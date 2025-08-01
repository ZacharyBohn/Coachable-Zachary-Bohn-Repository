import unittest

'''
You must use binary search but in a modified way.

Part 1: Implement a solution that uses the following approach.

Use binary search to find the pivot.
Once you know the pivot, use the modulo operator to imagine a sorted array starting from the pivot and use binary search on this virtual sorted array.
Part 2: Implement a solution that uses a single pass of binary search. What are your conditions to searching the left or right half of the array?
'''


class Solution:
    def search(self, nums, target):
        pass  # Placeholder for the actual solution

class TestCases(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.search([4,5,6,7,0,1,2], 0), 4)

    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.search([4,5,6,7,0,1,2], 3), -1)

    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.search([1], 0), -1)

    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.search([1,3], 3), 1)

    def test_case_5(self):
        sol = Solution()
        self.assertEqual(sol.search([5,1,3], 5), 0)

if __name__ == "__main__":
    unittest.main()
