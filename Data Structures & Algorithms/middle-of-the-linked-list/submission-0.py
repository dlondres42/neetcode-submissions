# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        aux_list = []
        curr = head
        while curr:
            aux_list.append(curr)
            curr = curr.next

        return aux_list[len(aux_list) // 2]
    