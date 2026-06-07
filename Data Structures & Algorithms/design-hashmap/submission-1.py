class MyHashMap:

    def __init__(self):
        self.aux_list = [-1 for _ in range(1_000_001)]


    def put(self, key: int, value: int) -> None:
        self.aux_list[key] = value

    def get(self, key: int) -> int:
        return self.aux_list[key]

    def remove(self, key: int) -> None:
        self.aux_list[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)