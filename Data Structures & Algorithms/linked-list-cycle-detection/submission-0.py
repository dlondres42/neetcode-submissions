# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # a cada chamada recursiva manter uma variavel local
        # que rastreia quantidade de de referencias para um no
        # se um no passar de 1 referencia, existe ciclo, propaga true
        # se .next de algum no = None, retorna false
        aux_set = set()
        def solve(head):
            if not head:
                return False
            
            if head in aux_set:
                return True

            aux_set.add(head)

            return solve(head.next)

        return solve(head)