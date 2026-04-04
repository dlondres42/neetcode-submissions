# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def is_equal(p, q):
            if p and not q:
                return False
            elif q and not p:
                return False
            if not p and not q:
                return True

            print(f"p: {p.val}, q: {q.val}")

            if p.val == q.val:
                return True and is_equal(p.left, q.left) and is_equal(p.right, q.right)
            else:
                return False
            
 

        return is_equal(p, q)