from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])

        # Set triggers for top-most row and left-most col to preserve presence of zeros as these row & col will be changed further down the line
        top_most_row_has_zero, left_most_col_has_zero = False, False

        for i in range(rows):
            for j in range(cols):
                # Check for zeros
                if matrix[i][j] == 0:
                    # See if it is in top-most row
                    if i == 0:
                        top_most_row_has_zero = True

                    # See if it is in left-most col
                    if j == 0:
                        left_most_col_has_zero = True

                    # If it is in neither of them set that cell's 0th row-idx and 0th col-idx cell values to zero
                    if i != 0 and j != 0:
                        matrix[0][j] = 0
                        matrix[i][0] = 0
        
        # Now, iterate over the (1,m)x(1,n) grid and set the values accordingly
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        # Check and change the top-most row values
        if top_most_row_has_zero:
            for j in range(cols):
                matrix[0][j] = 0
        
        # Check and change the left-most col values
        if left_most_col_has_zero:
            for i in range(rows):
                matrix[i][0] = 0

        




        
        

        
