from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_size = len(matrix)
        col_size = len(matrix[0])

        # Do a binary search on the 2d-matrix as it's sorted and find out the corresponding index
        row_idx = self.binarySearch_2d(0, row_size-1, target, matrix)
        # Check if there's row
        if row_idx == -1: return False 

        # Once you got the correct row, do the binary search on it
        return self.binarySearch_2d(0, col_size-1, target, matrix[row_idx]) != -1
    

    def binarySearch_2d(self, low_idx, high_idx, target, matrix) -> int:
        # Base case
        if low_idx > high_idx: 
            return -1
        
        # Compute the middle element
        mid_idx = int((low_idx + high_idx) / 2)

        # Check if matrix is 2d list
        if isinstance(matrix[0], list):
            if matrix[mid_idx][0] <= target and matrix[mid_idx][-1] >= target:
                return mid_idx # return the index
            elif target < matrix[mid_idx][0]:
                high_idx = mid_idx - 1 
            else:
                low_idx = mid_idx + 1
        # Check if matrix is just a 1d list
        else: 
            if target == matrix[mid_idx]:
                return mid_idx # return the index
            elif target > matrix[mid_idx]:
                low_idx = mid_idx + 1
            else:
                high_idx = mid_idx - 1
        
        return self.binarySearch_2d(low_idx, high_idx, target, matrix)


        