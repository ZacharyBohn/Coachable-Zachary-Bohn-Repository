# Runtime: O(n log n)
# Space: O(n)
# n = number of intervals
#
# Time to complete: 18:21
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # in-place quick sort
        intervals.sort()
        answer = [intervals[0]]
        # will this throw an error if intervals.length == 1?
        for interval in intervals[1:]:
            last_answer_end = answer[-1][1]
            interval_start, interval_end = interval
            if last_answer_end >= interval_start:
                # only need to update the end
                answer[-1][1] = max(last_answer_end, interval_end)
            else:
                answer.append(interval)
        return answer

'''
sorted? not necessarily.

Option 1:
sort then, merge from start to end
(modified quick sort)

to merge, once they are sorted,
elem does not overlap with next (or any other)
elem overlaps with one OR MORE next elems

should create a new array, and return that

'''