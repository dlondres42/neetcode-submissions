# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # primeiro achar a nova cabeca
        # depois de achada, percorrer os ponteiros a partir da 
        # nova cabeca e alterando iterativamente conforme passa 
        # pelos elementos que devem ser removidos
        

        # primeiro loop pra achar nova cabeca
        while head:
            if not head: return None
            if head.val != val: break #achou nova cabeca, head agora aponta para a nova cabeca
            head = head.next

        # head agora é nova cabeca
        curr = head
        while curr:
            while curr.next and curr.next.val == val:
                curr.next = curr.next.next

            curr = curr.next

        return head