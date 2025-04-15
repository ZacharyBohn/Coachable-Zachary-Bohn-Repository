class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # outer binary search to find correct row
        row_index = -1
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            value = matrix[mid][0]
            if value == target:
                return True
            elif value < target:
                if matrix[mid][-1] < target:
                    left = mid + 1
                else:
                    row_index = mid
                    break
            elif value > target:
                right = mid - 1
        # inner binary search
        row = matrix[row_index]
        left, right = 0, len(row) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            value = row[mid]
            if value == target:
                return True
            elif value < target:
                left = mid + 1
            elif value > target:
                right = mid - 1
        return False
