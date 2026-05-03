# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # usando solucao anterior mas inteiro em vez de str
        def solve(root, curr_sum):
            if not root:
                return 0

            curr_sum = 10 * curr_sum + root.val
            #print(root.val)
            if not root.left and not root.right:
                #print(f"somando {curr_sum}")
                return curr_sum
            
            return solve(root.left, curr_sum) + solve(root.right, curr_sum)
            
        
        
        return solve(root, 0) 