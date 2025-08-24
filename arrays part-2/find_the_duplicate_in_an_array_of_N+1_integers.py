from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Take a slow & fast pointers set to starting position
        slow = nums[0] # slow moves 1 edge at a time
        fast = nums[0] # fast moves two edges at a time

        # Keep on iterating until slow and fast pointers are same
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Now initialize another slow pointer from start 
        slow_2 = nums[0]
        # Increment both slow pointer one edge at a time 
        while slow_2 != slow:
            slow_2 = nums[slow_2]
            slow = nums[slow]
        
        # The intersection is the answer
        return slow


        # Note: Refer to flyod's cycle detection algorithm for clearer info
            

        