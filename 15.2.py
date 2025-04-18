class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answers = []
        n = len(nums)
        for pivot in range(n - 2):
            # pivot is the lowest possible value
            # so if it is above 0, then the sum of
            # all three values will be above 0.
            if nums[pivot] > 0:
                break
            if pivot > 0 and nums[pivot] == nums[pivot - 1]:
                continue
            lo = pivot + 1
            hi = n - 1
            while lo < hi:
                summ = nums[pivot] + nums[lo] + nums[hi]
                if summ == 0:
                    answers.append([nums[pivot], nums[lo], nums[hi]])
                    lo = self.incrementLo(lo, hi, nums)
                    hi = self.incrementHi(hi, lo, nums)
                elif summ < 0:
                    lo = self.incrementLo(lo, hi, nums)
                # summ > 0
                else:
                    hi = self.incrementHi(hi, lo, nums)
        return answers
            
                
    def incrementLo(self, lo: int, stop_at: int, numbers: List[int]) -> int:
        '''Increment lo to the next non-duplicate value.
        Will return a value that is below stop_at
        Params:
        lo: current value of lo
        stop_at: lo will be guarenteed to be lower than stop_at
        numbers: the list of numbers provided to threeSum()
        '''
        lo += 1
        while lo < stop_at and numbers[lo] == numbers[lo - 1]:
            lo += 1
        return lo
    
    def incrementHi(self, hi: int, stop_at: int, numbers: List[int]) -> int:
        '''Increment hi to the next non-duplicate value, moving backwards.
        Will return a value that is above stop_at
        Params:
        hi: current value of hi
        stop_at: hi will be guarenteed to be higher than stop_at
        numbers: the list of numbers provided to threeSum()
        '''
        hi -= 1
        while hi > stop_at and numbers[hi] == numbers[hi + 1]:
            hi -= 1
        return hi

