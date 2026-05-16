# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        # constant time

        curr = head
        tail = None
        while curr:
            if not curr.getNext():
                tail = curr
                tail.printValue()
            curr = curr.getNext()

        # tail encontrado, fazer 1 loop ate encontrar tail
        while tail:
            if tail == head:
                tail = None
            else:
                curr = head
                while curr.getNext() != tail: 
                    curr = curr.getNext()
                curr.printValue()
                tail = curr
            