class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        solutions = set()
        lo = 0
        hi = len(numbers) - 1
        while lo < hi:
            summ = numbers[lo] + numbers[hi]
            if summ == target:
                break
            elif summ < target:
                lo += 1
                while numbers[lo] == numbers[lo - 1]:
                    lo += 1
            # summ > target
            else:
                hi -= 1
                while numbers[hi] == numbers[hi+1]:
                    hi -= 1
        return [lo+1, hi+1]