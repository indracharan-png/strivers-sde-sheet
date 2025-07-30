class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1: return [[1]]
        pascals_tri = [[1], [1, 1]]

        for row_idx in range(2, numRows):
            new_row = [1]
            for i in range(row_idx-1):
                new_row.append(pascals_tri[row_idx-1][i] + pascals_tri[row_idx-1][i+1])
            new_row.append(1)
            pascals_tri.append(new_row)
        
        return pascals_tri


        