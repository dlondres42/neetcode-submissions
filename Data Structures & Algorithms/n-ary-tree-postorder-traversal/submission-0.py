"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        def traverse(root, result_list):
            if not root: return []

            if root.children:
                for child in root.children: traverse(child, result_list)
            
            result_list.append(root.val)
            return result_list 

        return traverse(root, [])