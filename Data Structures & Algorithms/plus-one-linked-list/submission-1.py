# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        # nao tem como fazer iteramente pq o carry over é calculado
        # na volta. A ideia é resolver recursivamente e caso chegar no
        # head, cria um novo no e vira o novo head

        def solve(head, carry_over):
            if not head:
                return 1
            # if not head.next:
            #     head.val = head.val + 1
            #     if head.val % 10 == 0: 
            #         head.val = 0
            #         return 1
            carry_over = solve(head.next, carry_over)
            head.val += carry_over
            print(f"{head.val}, {carry_over}")
            if head.val % 10 == 0 and head.val != 0:
                head.val = 0
                return 1
            return 0

        carry_over = solve(head, 0)
        if carry_over:
            new_head = ListNode(1, head)
            head = new_head

        return head