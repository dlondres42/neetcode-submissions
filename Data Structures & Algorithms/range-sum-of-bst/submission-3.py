# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # solucao anterior desconsiderava completamente caracteristica da ordenacao
        # dos nos na BST; levando isso em consideracao é possível pular chamadas cujos
        # valores estão fora do range

        def solve(root):
            if not root:
                return 0
            total_sum = 0
            left_sum = 0
            right_sum = 0
            if low <= root.val <= high:
                total_sum += root.val
            
            if root.val > low:
                left_sum = solve(root.left)

            if root.val < high:
                right_sum = solve(root.right)

            return total_sum + left_sum + right_sum 


        return solve(root)