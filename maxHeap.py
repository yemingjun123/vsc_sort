
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

    def dequeue(self):
        assert(self.count > 0)
        maxItem = self.data[1]
        self.data[1], self.data[self.count] = self.data[self.count], self.data[1]
        self.data.remove(maxItem)
        self.count -= 1
        self.shiftDown(1)
        return maxItem      

    def shiftUp(self, k):
        while k > 1 and (self.data[int(k/2)] < self.data[k]):
            self.data[int(k/2)], self.data[k] = self.data[k], self.data[k/2]
            k /= 2

    def shiftDown(self, k):
        while (2*k  <= self.count):
            j = int(2*k)

            if (j + 1 <= self.count) and (self.data[j+1] > self.data[j]):
                j += 1
            if self.data[k] >= self.data[j]:
                break
            
            self.data[k], self.data[j] = self.data[j], self.data[k]
            k = j
