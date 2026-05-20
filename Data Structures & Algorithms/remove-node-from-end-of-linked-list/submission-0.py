# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # um jeito mais fácil e eficiente em termos de complexidade temporal seria utilizando uma
        # stack para armazenar os nos enquanto percorre-se a lista, ao chegar na cauda
        # pega o elemento n-1 do stack e altera o ponteiro. O programa acaba em 1 iteracao mas
        # usa O(n). Para fazer em O(1), seria necessario percorrer a lista no minimo 2 vezes
        # Além disso, necessario lidar com o caso aresta onde removido == head
        # resolver com stack
        aux_stack = []
        curr = head
        while curr:
            aux_stack.append(curr)
            curr = curr.next

        size = len(aux_stack)

        node_to_remove = aux_stack[-n]
        
        if node_to_remove == head:
            new_head = head.next
            return new_head

        before_remove = aux_stack[-n - 1]
        before_remove.next = node_to_remove.next
        
        return head

        
        