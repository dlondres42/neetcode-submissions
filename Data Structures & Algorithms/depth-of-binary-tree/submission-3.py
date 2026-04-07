# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # utilizando BFS em vez de DFS
        level = 0
        node_queue = deque()
        if root:
            node_queue.append(root)
        print(node_queue)
        while node_queue:
            level += 1
            
            for i in range(len(node_queue)):
                root = node_queue.popleft()
                if root and root.left:
                    node_queue.append(root.left)
                if root and root.right:
                    node_queue.append(root.right)
            

        return level