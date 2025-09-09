class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        # At max there could be only 2 majority elements in an array
        maj_ele_1, maj_ele_1_cnt = 0, 0
        maj_ele_2, maj_ele_2_cnt = 0, 0 

        for num in nums:
            # Set the majority element-1 if its corresponding count is '0', make sure you're not assgining same element to both majority elements
            if maj_ele_1_cnt == 0 and num != maj_ele_2: 
                maj_ele_1 = num
                maj_ele_1_cnt += 1
            elif num == maj_ele_1: # Increment the frequency if same majority element encountered
                maj_ele_1_cnt += 1
            elif maj_ele_2_cnt == 0: # Set the majoriy element-2 if its corresponding count is '0'
                maj_ele_2 = num
                maj_ele_2_cnt += 1
            elif num == maj_ele_2:
                maj_ele_2_cnt += 1
            else:
                maj_ele_1_cnt -= 1
                maj_ele_2_cnt -= 1

        
        # Now count the frequency of two majority elements
        maj_ele_1_frq, maj_ele_2_frq = 0, 0

        for num in nums:
            if num == maj_ele_1:
                maj_ele_1_frq += 1
            elif num == maj_ele_2:
                maj_ele_2_frq += 1
        
        target_frq = int(len(nums)/ 3) + 1
        output = []
        
        # A freuency check 'cause there 0, 1 or 2 satisfied answers
        if maj_ele_1_frq >= target_frq:
            output.append(maj_ele_1)
        
        if maj_ele_2_frq >= target_frq:
            output.append(maj_ele_2)

        return output
