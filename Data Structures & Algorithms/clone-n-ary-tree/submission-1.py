"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root: return None
        
        aux_map = {}

        def dfs(root):
            if root in aux_map: return aux_map[root]

            new_root = Node(root.val)
            aux_map[root] = new_root
            for child in root.children:
                new_root.children.append(dfs(child))

            return new_root

        new_head = dfs(root)
        
        return new_head


