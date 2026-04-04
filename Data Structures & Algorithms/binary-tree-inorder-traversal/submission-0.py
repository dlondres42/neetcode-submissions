# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def traverse(root, result):
            if not root: return None, result
            if root and root.left:
                traverse(root.left, result)
            
            print(f"val: {root.val}, result: {result}")
            result.append(root.val)

            if root.right:
                traverse(root.right, result)

            return root, result

        _, result = traverse(root, [])
        return result
