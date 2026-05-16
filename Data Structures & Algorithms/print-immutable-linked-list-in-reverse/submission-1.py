import sys

# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        sys.setrecursionlimit(2000)
        def solve(head):
            if not head: return
            solve(head.getNext())
            head.printValue()
        
        solve(head)