class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        size = len(nums)

        # Color pointers tells the valid insertion position at any given instant of corresponding color ball
        red_pointer, white_pointer, blue_pointer = 0, 0, size-1

        while(white_pointer <= blue_pointer):            
            if nums[white_pointer] == 1:
                # White pointer sees white color ball, move white pointer to right
                white_pointer += 1
            elif nums[white_pointer] == 0:
                # White pointer sees red color ball, it swaps it with ball at red pointer
                nums[white_pointer] = nums[red_pointer]
                nums[red_pointer] = 0
                # Increment both red and white pointers
                red_pointer += 1
                white_pointer += 1
            else:
                # White pointer sees blue color ball, it swaps it with ball at blue pointer
                nums[white_pointer] = nums[blue_pointer]
                nums[blue_pointer] = 2
                # Decrement the blue pointer
                blue_pointer -= 1
        
        




            


        