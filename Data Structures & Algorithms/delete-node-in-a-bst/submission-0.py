# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def get_min(root):
            if root and root.left:
                return get_min(root.left)
            return root
               

        def remove(root, key):
            if not root: return

            if key > root.val:
                root.right = remove(root.right, key)
            elif key < root.val:
                root.left = remove(root.left, key)
            else:
                print(f"achei, {root.val}")
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    next_to_remove = get_min(root.right).val
                    root.val = next_to_remove
                    root.right = remove(root.right, next_to_remove)
               
            return root
            
        

        return remove(root, key)