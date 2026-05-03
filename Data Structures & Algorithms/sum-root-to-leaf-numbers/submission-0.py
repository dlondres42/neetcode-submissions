# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # problema resolvivel com DFS e no minimo necessita de O(n)
        # para iterar por todos os caminhos. Quanto à memória, 
        # vai ser no minimo O(n) para a call stack; talvez mais memoria
        # para os caminhos?
        # 1- inorder traversal
        # 2- usar lista global para ir armazenando os caminhos 
        # conforme chega na folha
        # 3- caminhos são strings


        def solve(root, path):
            # if not root:
            #     paths.append(path)
            #     return 

            path += str(root.val)
            #print(path)
            if root.left: solve(root.left, path)
            if root.right: solve(root.right, path)
            if not root.left and not root.right: paths.append(path)

        paths = []
        solve(root, "")
    
        return sum([int(path) for path in paths])




