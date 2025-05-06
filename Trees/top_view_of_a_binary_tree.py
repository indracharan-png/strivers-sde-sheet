from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def topView(self, root):
        # empty binary tree, return the empty list
        if root is None: return []

        # dictionary to store the top view of the binary tree
        top_view = {}

        # traverse the binary tree using inorder traversal
        self.bfs(root, top_view)

        # to store the answer
        output = []

        # sort the dictionary by the horizontal distance
        for _ , value in sorted(top_view.items()):
            output.append(value)
        
        return output


    def bfs(self, root, top_view):
        # queue to store the nodes of the binary tree
        queue = deque()

        # push the root node into the queue
        queue.append((root, 0))

        # traverse the binary tree level-wise
        while queue:
            # pop the first element of the queue
            node, hd = queue.popleft()

            # add the node to dictionary if the horizonatal distance is not present in dictionary
            if hd not in top_view:
                top_view[hd] = node.data
            
            # push the left chidl to the queue
            if node.left:
                queue.append((node.left, hd - 1))
            
            # push the right child to the queue
            if node.right:
                queue.append((node.right, hd + 1))
            






        
    




        

        
