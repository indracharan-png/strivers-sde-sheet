from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1_size = len(nums1)
        nums2_size = len(nums2)
        nums1_idx = (nums1_size - nums2_size) - 1 # An index to keep track of current nums1 element
        nums2_idx = nums2_size - 1 # An index to keep track of current nums2 element
        curr_idx = nums1_size - 1 # An index to place greatest element between elements at num1_idx and nums2_idx

        # Keep traversing as long as you have elements from each array to compare 
        while(nums1_idx >= 0 and nums2_idx >= 0):
            if nums1[nums1_idx] >= nums2[nums2_idx]:
                nums1[curr_idx] = nums1[nums1_idx]
                nums1_idx -= 1
            else:
                nums1[curr_idx] = nums2[nums2_idx]
                nums2_idx -= 1
            curr_idx -= 1
        
        # Find out which array's elements were leftout
        left_out_array, left_out_idx = (nums1,  nums1_idx) if nums1_idx >= 0 else (nums2, nums2_idx)

        # Add rest of the leftout array to the nums1 
        while(left_out_idx >= 0):
            nums1[curr_idx] = left_out_array[left_out_idx]
            curr_idx -= 1
            left_out_idx -=1

        
        