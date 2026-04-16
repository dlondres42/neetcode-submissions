# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        def merge(list1_head, list2_head):   
            if not list1_head: return list2_head
            if not list2_head: return list1_head

            if list1_head and list2_head:
                if list1_head.val < list2_head.val:
                    list1_head.next = merge(list1_head.next, list2_head)
                else:
                    list2_head.next = merge(list1_head, list2_head.next)

                return list1_head if list1_head.val < list2_head.val else list2_head
            # preciso retornar o primeiro elemento

        return merge(list1, list2)