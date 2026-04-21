# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        aux_list = []
        while curr:
            aux_list.append(curr.val)
            curr = curr.next

        l = 0
        r = len(aux_list) - 1
        while l < r:
            if aux_list[l] != aux_list[r]: return False
            l += 1
            r -= 1

        return True