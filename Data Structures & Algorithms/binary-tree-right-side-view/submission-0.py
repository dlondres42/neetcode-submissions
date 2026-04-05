# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result_nodes = []
        node_queue = deque()

        if root:
            node_queue.append(root)
        level = 0
        while len(node_queue) > 0:
            aux_list = []
            for i in range(len(node_queue)):
                root = node_queue.popleft()
                if root.left: node_queue.append(root.left)
                if root.right: node_queue.append(root.right)
                aux_list.append(root.val)

            result_nodes.append(aux_list[-1])
            

        return result_nodes