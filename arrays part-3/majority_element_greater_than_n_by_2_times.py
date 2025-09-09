class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        
        majority_ele = 0        # Set to '0', as we haven't gone through the list to determine the majority element
        majority_ele_freq = 0   # Set to '0', as we haven't gone through the list to determine the frequency of the majority element

        for num in nums:
            # Set and increment the above two variables if the frequency is '0'
            if majority_ele_freq == 0: 
                majority_ele = num
                majority_ele_freq += 1
            elif num == majority_ele: # Increment as you've seen the same element further down in the array
                majority_ele_freq += 1
            else:
                majority_ele_freq -=1 # Decrement as this different element is taking our supposed majority element place, which implied the fact that this element could be our actual majority element in whole array.
        
        return majority_ele
        