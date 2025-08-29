class Solution:
    def inversionCount(self, arr):
        return self.merge_sort(arr, 0, len(arr)-1)
    

    def merge_sort(self, arr, left, right):
        # Check if poriton of array in focus is of length 1 or zero
        if left >= right:
            return 0
        
        # Calculate the middle of the array
        mid = int((left+right)/2)
        
        # Keep track of inversion occured at each split in recursion
        no_of_inversions = 0
        
        # Recursively split the array into two halves and also add
        # the inversions occured in each recursion
        no_of_inversions += self.merge_sort(arr, left, mid)
        no_of_inversions += self.merge_sort(arr, mid+1, right)
        
        # Now compute and the inversions in current split
        no_of_inversions += self.merge_arrays(arr, left, mid, right)
        
        return no_of_inversions
        
        
    def merge_arrays(self, arr, left, mid, right):
        # Copy two parts into sorted array into 2 new arrays for further computation
        left_arr = arr[left:mid+1]
        right_arr = arr[mid+1: right+1]
        
        left_idx, size_left_arr = 0, len(left_arr)
        right_idx, size_right_arr = 0, len(right_arr)
        original_idx = left
        inversions_cnt = 0
        
        while(left_idx < size_left_arr and right_idx < size_right_arr):
            # Left element is smaller or equal to right element
            if (left_arr[left_idx] <= right_arr[right_idx]):
                arr[original_idx] = left_arr[left_idx]
                left_idx += 1
            else: # Left element is bigger than the right element
                arr[original_idx] = right_arr[right_idx]
                right_idx += 1
                # This means these two pair of elements are inversions
                # at this point these two arrays sorted hence count the inversions of the rest 
                # of the elements in left sorted array
                inversions_cnt += size_left_arr - left_idx
            original_idx += 1
        
        # Check and add up the rest of two array 
        while(left_idx < size_left_arr):
            arr[original_idx] = left_arr[left_idx]
            left_idx += 1
            original_idx += 1
        
        while(right_idx < size_right_arr):
            arr[original_idx] = right_arr[right_idx]
            right_idx += 1
            original_idx += 1
        
        return inversions_cnt
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    