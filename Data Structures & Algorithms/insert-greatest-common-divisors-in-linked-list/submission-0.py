# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from math import gcd

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head


        while curr.next:
            curr_next = curr.next
            result = gcd(curr.val, curr_next.val)
            curr.next = ListNode(result, curr_next)
            curr = curr_next


        return head
