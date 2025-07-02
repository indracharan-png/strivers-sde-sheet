# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        
        # Do the bfs traversal on the tree
        while queue:
            
            # At each level, check if the nodes are symmetric
            if not self.check_palindrome(queue): return False

            # Get the current level length
            curr_level_len = len(queue)

            for _ in range(curr_level_len):
                curr_node = queue.popleft()
                # Check for the left and right children
                if curr_node != None:
                    queue.append(curr_node.left)
                    queue.append(curr_node.right)
            
        return True
    

    def check_palindrome(self, queue:deque) -> bool:
        # Check if the queue is empty
        if not queue: return True

        left_idx, right_idx = 0, len(queue) - 1

        while left_idx < right_idx:
            # Check if the left and right nodes are equal
            if queue[left_idx] != None and queue[right_idx] != None and (queue[left_idx].val != queue[right_idx].val):
                return False
            
            # Check if one of the nodes is None
            if (queue[left_idx] == None and queue[right_idx] != None) or (queue[left_idx] != None and queue[right_idx] == None):
                return False
            
            left_idx += 1
            right_idx -= 1
        
        return True
        
        