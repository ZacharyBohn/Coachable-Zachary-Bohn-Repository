import unittest


'''
Concretely describe your criteria for binary search. When do you search the left half? When do you search the right half?
'''

class Solution:
    def minEatingSpeed(self, piles, h):
        pass  # Placeholder for the actual solution

class TestCases(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.minEatingSpeed([3,6,7,11], 8), 4)

    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.minEatingSpeed([30,11,23,4,20], 5), 30)

    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.minEatingSpeed([30,11,23,4,20], 6), 23)

    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.minEatingSpeed([1,1,1,1,1], 5), 1)

    def test_case_5(self):
        sol = Solution()
        self.assertEqual(sol.minEatingSpeed([1000000000], 2), 500000000)

if __name__ == "__main__":
    unittest.main()
