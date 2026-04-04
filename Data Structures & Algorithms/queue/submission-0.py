class DequeNode:
    def __init__(self, val:int, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.size = 0
        self.head = self.tail = None

    def isEmpty(self) -> bool:
        return self.size == 0        

    def append(self, value: int) -> None: #append no final
        newNode = DequeNode(value, self.tail, None) 
        if self.size == 0:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
        
        self.tail = newNode
        self.size += 1

    def appendleft(self, value: int) -> None:
        newNode = DequeNode(value, None, self.head) 
        if self.size == 0:
            self.head = self.tail = newNode
        else:
            self.head.prev = newNode
        
        self.head = newNode
        self.size += 1

    def pop(self) -> int:
        if self.size == 0: return -1
        elif self.size == 1: 
            val = self.head.val
            self.head = self.tail = None
            self.size -= 1
            return val
        
        val = self.tail.val
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1
        return val

    def popleft(self) -> int:
        if self.size == 0: return -1
        elif self.size == 1: 
            val = self.head.val
            self.head = self.tail = None
            self.size -= 1
            return val
        
        val = self.head.val
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1
        return val