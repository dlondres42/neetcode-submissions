# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        
        curr_l1, curr_l2 = l1, l2
        result = curr_l1.val + curr_l2.val
        carry = 1 if result >= 10 else 0
        new_head = ListNode((result) % 10, None)
        curr_new_head = new_head
        curr_l1, curr_l2 = curr_l1.next, curr_l2.next
        while curr_l1 or curr_l2:
            val_l1 = curr_l1.val if curr_l1 else 0
            val_l2 = curr_l2.val if curr_l2 else 0
            result = val_l1 + val_l2 + carry
            carry = 1 if result >= 10 else 0
            result %= 10

            print(result % 10)
            curr_new_head.next = ListNode(result, None)
            curr_new_head = curr_new_head.next
            if curr_l1:
                curr_l1 = curr_l1.next
            if curr_l2:
                curr_l2 = curr_l2.next



        if carry:
            curr_new_head.next = ListNode(1, None)

        return new_head