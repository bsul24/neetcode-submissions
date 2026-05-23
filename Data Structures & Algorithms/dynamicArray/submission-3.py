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
        if self.length == self.capacity:
            self.resize()
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        val = self.arr[self.length - 1]
        self.length -= 1
        return val

    def resize(self) -> None:
        self.capacity *= 2
        newArr = self.capacity * [None]
        for i in range(len(self.arr)):
            newArr[i] = self.arr[i]
        self.arr = newArr


    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity

