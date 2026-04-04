# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def insert_tree(root, val):
            if not root:
                return TreeNode(val, None, None)
            
            if val > root.val:
                root.right = insert_tree(root.right, val)
            else:
                root.left = insert_tree(root.left, val)
            return root
            
        return insert_tree(root, val)