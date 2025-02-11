class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # outter binary search to find correct row
        row_index = -1
        left, right = 0, len(matrix) - 1
        while left <= right:
            i = left + ((right - left) // 2)
            value = matrix[i][0]
            if value == target:
                return True
            elif value < target:
                if matrix[i][-1] < target:
                    left = i + 1
                else:
                    row_index = i
                    break
            elif value > target:
                right = i - 1
        # inner binary search
        row = matrix[row_index]
        left, right = 0, len(row) - 1
        while left <= right:
            i = left + ((right - left) // 2)
            value = row[i]
            if value == target:
                return True
            elif value < target:
                left = i + 1
            elif value > target:
                right = i - 1
        return False
