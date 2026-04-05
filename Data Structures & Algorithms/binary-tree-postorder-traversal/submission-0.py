# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def traverse(root, result_list):
            if not root: return []
            traverse(root.left, result_list)
            traverse(root.right, result_list)
            result_list.append(root.val)
            return result_list

        
        return traverse(root, [])
