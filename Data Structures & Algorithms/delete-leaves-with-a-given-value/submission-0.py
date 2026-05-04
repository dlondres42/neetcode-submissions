# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # achar o no folha
        # remover no
        # verificar se o no atual virou folha; caso positivo remover
        # repetir o processo

        def solve(root):
            if not root:
                return

            print(root.val)

            if not root.right and not root.left and root.val == target:
                #print(f"achei, {root.val}")
                return None
            if not root.right and not root.left and root.val != target:
                #print(f"retornando, {root.val}")
                return root

            if root.left:
                root.left = solve(root.left)
            if root.right:
                root.right = solve(root.right)
            
            if root.val == target and not root.right and not root.left:
                root = solve(root)

            return root
        

        return solve(root)