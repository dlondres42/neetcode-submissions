# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        def solve(root, curr_min):
            if not root:
                return curr_min
            node_result = abs(root.val - target)
            curr_min_result = abs(curr_min - target)
            if node_result < curr_min_result:
                curr_min = root.val
            
            curr_min = solve(root.left, curr_min)
            return solve(root.right, curr_min)


        return solve(root, root.val)