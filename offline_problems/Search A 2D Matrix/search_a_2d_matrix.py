import unittest


'''
Implement a solution that runs in O(log(m) + log(n)) runtime.
'''

class Solution:
    def searchMatrix(self, matrix, target):
        pass  # Placeholder for the actual solution

class TestCases(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3), True)

    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13), False)

    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.searchMatrix([[1]], 1), True)

    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.searchMatrix([[1],[3]], 3), True)

    def test_case_5(self):
        sol = Solution()
        self.assertEqual(sol.searchMatrix([[1, 3, 5]], 2), False)

if __name__ == "__main__":
    unittest.main()
