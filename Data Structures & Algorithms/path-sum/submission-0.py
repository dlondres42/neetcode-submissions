# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def solve(root, targetSum, currSum):
            if not root: return False

            currSum += root.val
            if (not root.left) and (not root.right) and (currSum == targetSum):
                return True
            
            #print(currSum)

            return solve(root.left, targetSum, currSum) or solve(root.right, targetSum, currSum)
        
        return solve(root, targetSum, 0)
        