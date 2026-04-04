# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        nodeList = []
        while curr and curr.next: # garante que ta no tail
            nodeList.append(curr)
            curr = curr.next
        
        newHead = curr
        print(newHead)


        while curr and nodeList:
            curr.next = nodeList.pop()
            curr = curr.next
            if not nodeList:
                curr.next = None

        return newHead


# percorrer armazenando os enderecos dos elementos
# chegar na cauda
# cauda.next = nodeList[-1] em diante