class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # A variable to store where the dicrepency occurs (right element is bigger than left element
        flag_idx = -1
        nums_len = len(nums)

        # Traverse from the right end of the list 
        for i in range(nums_len-1, 0, -1):
            if nums[i] > nums[i-1]:
                flag_idx = i-1
                break
        
        # Check if the array is in descending order and return sorted/reversed array
        if flag_idx == -1:
            nums.reverse()
            return
        
        # Search and Store the next smallest greatest number w.r.t element at flag index
        smallest_diff = 101
        next_min_ele_idx = -1
        for i in range(flag_idx+1, nums_len):
            curr_ele = nums[i]
            if curr_ele > nums[flag_idx] and (curr_ele - nums[flag_idx]) <= smallest_diff:
                smallest_diff = curr_ele - nums[flag_idx]
                next_min_ele_idx = i
        

        # Swap the element at flag idx with next smallest greatest element on right of it in array
        temp = nums[flag_idx]
        nums[flag_idx] = nums[next_min_ele_idx]
        nums[next_min_ele_idx] = temp

        # Now, just reverse the right part of array right to flag index
        left_idx = flag_idx + 1
        right_idx = len(nums) - 1
        while(left_idx < right_idx):
            temp = nums[left_idx]
            nums[left_idx] = nums[right_idx]
            nums[right_idx] = temp
            left_idx += 1
            right_idx -= 1
        






        