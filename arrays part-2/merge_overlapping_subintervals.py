from functools import cmp_to_key
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # # Sort the intervals according to their start time
        # sorted_intervals = sorted(intervals, key=cmp_to_key(lambda ele1, ele2: ele1[0] - ele2[0]))

        intervals.sort()
        
        size = len(intervals)
        output = []

        # Start with the first interval in array
        new = intervals[0]

        # Traverse the sorted intervals from index 1
        for i in range(1, size):
            current = intervals[i]
            # Check if current interval's start time overelaps with new interval
            if current[0] <= new[1]:
                # Upadate the end time of prev interval with max end time between both
                new[1] = max(new[1], current[1])
            else:
                # In case not overlapping add the the newly formed interval and start fresh starting from this point on
                output.append(new)
                new = intervals[i]
        
        # Add the new interval to output
        output.append(new)
        return output



    