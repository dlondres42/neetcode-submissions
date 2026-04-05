# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    
        # em root
        # append left e right na fila
        # processa root
        # pop left, append left e right na fila
        # pop right, append left e right
        # repete o processo
        # utilizar append e popleft
        result_list = []
        children_queue = deque()
        if root:
            children_queue.append(root)
        level = 0
        while len(children_queue) > 0:
            level += 1
            level_list = []
            for i in range(len(children_queue)):
                
                root = children_queue.popleft()
                if root.left:
                    children_queue.append(root.left)
                if root.right:
                    children_queue.append(root.right)
                
                level_list.append(root.val)
                
            result_list.append(level_list[:])
           
        return result_list
