# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # fazer inorder traversal, armazenar resultado
        # em array e depois pegar o resultado por indexacao

        result = []
        def solve(root, result):
            if not root:
                return

            
            solve(root.left, result)
            result.append(root.val)
            #print(result)
            solve(root.right, result)
        
        solve(root, result)
        return result[k - 1]