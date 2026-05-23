class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = capacity * [None]
        self.capacity = capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.capacity == self.length:
            self.resize()
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        self.length -= 1
        return self.arr[self.length]

    def resize(self) -> None:
        self.capacity *= 2
        tmp = self.capacity * [None]
        for i in range(len(self.arr)):
            tmp[i] = self.arr[i]
        self.arr = tmp


    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity