class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._array = [None for i in range(0, capacity)]
        self.size = 0

    def get(self, i: int) -> int:
        return self._array[i]

    def set(self, i: int, n: int) -> None:
        self._array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        
        self._array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        val = self._array[self.size]
        self._array[self.size] = None

        return val

    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [None for i in range(0, self.capacity)]
        for i in range(0, len(self._array)):
            new_arr[i] = self._array[i]
        self._array = new_arr 

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity