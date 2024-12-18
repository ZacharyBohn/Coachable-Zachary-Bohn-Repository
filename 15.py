# my first solution
# this one fails on time
class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(n) time and space
        #
        # mapping of
        # n: index of n
        hashset = {nums[y]: y for y in range(len(nums))}
        # mapping of
        # min answer: [max answer]
        duplicates = set()
        answers = []

        # O(n^2) time and O(1) space
        for i,x in enumerate(nums):
            for j,y in enumerate(nums):
                # skip duplicate of i and j
                if i == j:
                    continue
                z = -(x+y)
                k = hashset.get(z, None)
                # skip if no possible answer exists
                if not k:
                    continue
                # skip if k is a duplicate of i or j
                if k == i or k == j:
                    continue
                # found a valid answer
                minimum = min(x, y, z)
                maximum = max(x, y, z)
                if (minimum, maximum) in duplicates:
                    continue
                duplicates.add((minimum, maximum))
                answers.append([x, y, z])
        return answers

# better solution
 class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = set()
        counts = {}
        for x in nums:
            counts[x] = counts.get(x, 0) + 1
        for x in counts:
            for y in counts:
                z = -(x+y)
                if not counts.get(z, None):
                    continue
                if counts[x] == 1 and (x == y or x == z):
                    continue
                if counts[y] == 1 and y == z:
                    continue
                if counts[x] == 2 and x == y and y == z:
                    continue
                solutions.add(tuple(sorted([x,y,z])))
        return list(solutions)
