
class MaxHeap:

    def __init__(self):
        self.data = [0]
        self.count = 0
    
    def size(self):
        return self.count
    
    def isEmpty(self):
        return self.count == 0

    def insert(self, item):
        self.data.append(item)
        self.count += 1
        self.shiftUp(self.count)

    def shiftUp(self, k):
        while k > 1 and (self.data[k/2] < self.data[k]):
            self.data[k/2], self.data[k] = self.data[k], self.data[k/2]
            k /= 2






    


