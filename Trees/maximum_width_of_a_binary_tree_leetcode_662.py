# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        self.bfs(root, ans)
        return ans[0]

    def bfs(self, node, ans) -> None:
        q = deque()
        q.append((node, 0))
        while(len(q) != 0):
            curr_len = len(q)
            ans[0] = max(ans[0], q[curr_len-1][1] - q[0][1] + 1)
            while(curr_len != 0):
                currentNode, index = q.popleft()
                if currentNode.left != None:
                    q.append((currentNode.left, 2*index+1))
                if currentNode.right != None:
                    q.append((currentNode.right, 2*index+2))
                curr_len -= 1
            
            
