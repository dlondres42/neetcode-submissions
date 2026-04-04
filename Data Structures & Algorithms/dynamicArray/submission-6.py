class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [None for _ in range(capacity)]

    def get(self, i: int) -> int:
        return self.array[i]
    
    # TODO edge case
    def set(self, i: int, n: int) -> None:
        if not self.array[i]:
            self.array[i] = n
            self.size += 1
        else:
            self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        
        self.array[self.size] = n
        self.size += 1

    # not sure if this works
    def popback(self) -> int:
        value = self.array[self.size - 1]
        if value:
            self.array[self.size - 1] = None
            self.size -= 1

            return value

    def resize(self) -> None:
        new_arr = [i for i in self.array] + [None for _ in range(self.capacity)]
        self.array = new_arr
        self.capacity *= 2
    
    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity