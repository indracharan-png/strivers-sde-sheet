from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        size = len(nums)

        # Compute sum of first 1 to n elements
        sum_n = int((size * (size+1))/2)

        # Now compute the sum of given elements in nums
        sum_nums = 0
        for i in range(size): 
            sum_nums += nums[i]
        
        x_minus_y = sum_nums - sum_n # X - Y

        # Compute sum of squares of 1 to n elements
        sum_squares_n = int((size * (size+1) * (2*size+1)) / 6)

        # Now compute sum of squares of given elements in nums
        sum_nums_squares = 0
        for i in range(size):
            sum_nums_squares += nums[i]**2
        
        x_square_minus_y_square = sum_nums_squares - sum_squares_n # X^2 - Y^2

        x_plus_y = int(x_square_minus_y_square / x_minus_y) # X + Y

        x = int((x_minus_y + x_plus_y) / 2)
        y = x_plus_y - x

        return [x, y]

        