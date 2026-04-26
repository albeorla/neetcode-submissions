class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [0] * self.capacity

    def get(self, i: int) -> int:
        if i < 0 or i >= self.size:
           raise IndexError("Invalid index")
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        if i < 0 or i >= self.size:
            raise IndexError("Invalid Index")
        self.array[i] = n

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity
    
    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1
    
    def popback(self) -> int:
        if self.size == 0:
            raise IndexError("Array is empty")
        self.size -= 1
        return self.array[self.size]

    def resize(self) -> None:
        tmp_array = (self.capacity * 2) * [0]
        for i in range(self.size):
            tmp_array[i] = self.array[i]
        self.array = tmp_array
        self.capacity *= 2
        


