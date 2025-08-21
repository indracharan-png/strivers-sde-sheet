from functools import cmp_to_key
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals according to their start time
        sorted_intervals = sorted(intervals, key=cmp_to_key(lambda ele1, ele2: ele1[0] - ele2[0]))
        
        size = len(intervals)
        output = []

        # Every time a new interval starts, set new start and end times to -1
        new_start = -1
        new_end = -1

        # Traverse the sorted_intervals
        for i in range(size):
            # If new start and end times are not present, set them to current's intervals timings
            if new_start == -1 and new_end == -1:
                new_start, new_end = sorted_intervals[i][0], sorted_intervals[i][1]
             # Check the new intervals end time is less than equal to next intervals start time, check for overlapping
            if i != size-1 and sorted_intervals[i+1][0] <= new_end:
                # If overlapped, set the new end to longest end time between both
                new_end = max(new_end, sorted_intervals[i+1][1])
            else:
                # If the current interval does not overlap, just add itself and go back to initial state
                output.append([new_start, new_end])
                curr_start, curr_end = -1, -1
        
        return output