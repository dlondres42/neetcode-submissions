from typing import List

class Node:
    def __init__(self, val:int):
        self.val = val
        self.next = None

    def __repr__(self):
        return f"Node({self.val}, {self.next})"

class LinkedList:
    def __init__(self) -> None:
        self.head : Node = None
        self.tail : Node = None
        self.size : int = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        
        currNode = self.head
        while index:
            currNode = currNode.next
            index -= 1
        return currNode.val

    def insertHead(self, val:int) -> None:
        newHead = Node(val)
        if self.head:
            newHead.next = self.head
        if not self.tail:
            self.tail = newHead
        
        self.head = newHead
        self.size += 1

    def insertTail(self, val:int) -> None:
        newTail = Node(val)
        if self.tail:
            self.tail.next = newTail
        if not self.head:
            self.head = newTail
        
        self.tail = newTail
        self.size += 1
    
    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        if self.size == 1:
            self.head = self.tail = None
            self.size -= 1
            return True
        
        currNode = self.head
        count = 0
        while count < index - 1: # acha o no anterior a ser removido exceto head
            currNode = currNode.next
            count += 1

        print(f"removed val {currNode.val}")

        if currNode == self.head and index == 0:
            self.head = currNode.next
            self.size -= 1
            return True

        if currNode.next == self.tail:
            currNode.next = None
            self.tail = currNode
            self.size -= 1
            return True
        
        currNode.next = currNode.next.next
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        values = []
        size = self.size
        currNode = self.head
        while size:
            currVal = currNode.val 
            values.append(currVal)
            currNode = currNode.next
            size -= 1

        return values