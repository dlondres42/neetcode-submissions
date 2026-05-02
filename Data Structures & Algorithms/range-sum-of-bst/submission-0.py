# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # precisa percorrer todos os nos e checar se o valor do no
        # esta dentro do range. No pior dos casos é O(n); tanto BFS
        # quanto DFS funcionam aqui; só percorrer e manter variavel da soma
        
        def solve(root):
            if not root:
                return 0
            result = 0
            if low <= root.val <= high:
                result += root.val

            result += solve(root.left) + solve(root.right)
            
            return result 

        return solve(root)