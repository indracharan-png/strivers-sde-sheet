from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = [-1]
        self.post_order(root, ans)
        return ans[0]
    
    def post_order(self, root, ans):
        # Base Case: Check if you're at root and then return '0'
        if root is None:
            return 0
        
        # Get the max distance to a leaf node towards left side
        maxLengthOnLeft = self.post_order(root.left, ans)

        # Get the max distance to a leaf node towards right side
        maxLengthOnRight = self.post_order(root.right, ans)

        # Now, check the distance b/w two extreme nodes and update 
        ans[0] = max(ans[0], (maxLengthOnLeft + maxLengthOnRight))

        # Greedy, consider the longest side and then add 1 to include current node as well
        return 1 + max(maxLengthOnLeft, maxLengthOnRight)

        