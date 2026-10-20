class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        while top <= bottom:
            mid_str = top + (bottom - top) // 2
            if matrix[mid_str][0] > target:
                bottom = mid_str - 1
            elif matrix[mid_str][-1] < target:
                top = mid_str + 1
            else:
                left = 0
                right = len(matrix[mid_str]) - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if matrix[mid_str][mid] > target:
                        right = mid - 1
                    elif matrix[mid_str][mid] < target:
                        left = mid + 1
                    else:
                        return True
                return False
        return False
