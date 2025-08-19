class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        size = len(matrix)

        # Idea is to consider square boundaries of thickness 1 and rotate them in clockwise direction element wise and do this one square layer at a time

        # Consider the cell (top-left) in the current boundary
        for start_idx in range(int(size/2)):
            # Current boundary length that needs to be rotated
            curr_boundary_len = size - 2 * start_idx
            
            # Rotate the layer cell-wise, only needs to traverse the top layer of boundary as changing it affects remaining elements in layer
            for i in range(start_idx, start_idx + curr_boundary_len - 1):
                curr_x = start_idx
                curr_y = i
                prev_val = matrix[curr_x][curr_y]
                # Changing one element in each top layer of boundary affects the other cells in the boundary
                for _ in range(4):
                    new_x = curr_y
                    new_y = (curr_boundary_len - 1) - curr_x + 2 * start_idx
                    new_val = matrix[new_x][new_y]
                    matrix[new_x][new_y] = prev_val
                    prev_val = new_val
                    curr_x = new_x
                    curr_y = new_y
        



        