class MinHeap:
    def __init__(self) -> None:
        self.heap = [0]
    
    def top(self) -> int:
        if len(self.heap) == 1: return -1
        return self.heap[1]

    def push(self, val:int) -> None:
        self.heap.append(val)
        i = len(self.heap) - 1
        # percolate up
        while i > 1:
            if self.heap[i] < self.heap[i//2]:
                self.heap[i//2], self.heap[i] = self.heap[i], self.heap[i//2]
                i //= 2
            else:
                break

    def pop(self) -> int:
        if len(self.heap) == 1: return -1
        if len(self.heap) == 2: return self.heap.pop()
        result = self.heap[1]
        self.heap[1] = self.heap.pop()
        # percolate down
        self._percolate_down(start = 1)
        return result

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums
        start = (len(self.heap) - 1) // 2
        while start > 0:
            self._percolate_down(start = start)
            start -= 1

    def _percolate_down(self, start : int) -> None:
        i = start
        while 2 * i < len(self.heap):
            # determine the smaller child
            smallest = 2 * i
            if 2 * i + 1 < len(self.heap) and self.heap[2 * i + 1] < self.heap[2 * i]:
                smallest = 2 * i + 1
            
            # if current is larger than the smaller child, swap
            if self.heap[i] > self.heap[smallest]:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
            else:
                break

    def __repr__(self) -> str:
        return f"Class MinHeap({self.heap[1:]})"