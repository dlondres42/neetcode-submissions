# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result_list = []

        def is_leaf(node) -> bool:
            if not node.left and not node.right:
                return True
            return False

        def dfs(node, aux_list):

            if is_leaf(node):
                aux_list.append(node.val)
                return None, aux_list

            if node.left and is_leaf(node.left):
                aux_list.append(node.left.val)
                node.left = None
            
            if node.left and not is_leaf(node.left):
                node.left, aux_list = dfs(node.left, aux_list)

            if node.right and is_leaf(node.right):
                aux_list.append(node.right.val)
                node.right = None

            if node.right and not is_leaf(node.right):
                node.right, aux_list = dfs(node.right, aux_list)

            

            return node, aux_list
        
        while root:
            root, aux_list = dfs(root, [])
            result_list.append(aux_list)
            #print(aux_list)

        return result_list