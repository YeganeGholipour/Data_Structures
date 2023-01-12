
######## Implementing Priority Queue #########

class PriorityQueue:
    MAX_SIZE = 10
    def __init__(self):
        self._data = [None] * PriorityQueue.MAX_SIZE
        self._size = 0
        self._front = 0
        self._rear = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def first(self):
        if self.is_empty():
            raise Empty('Priority Queue Is Empty')
        return self._data[self._front]
    def dequeue(self):
        if self.is_empty():
            raise Empty('Priority Queue Is Empty')
        element = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        #self._front = self._data.index(min(self._data))
        self._size -= 1
        return element
    def _insertion_sort(self):
        for i in range(1, len(self._data)):
            j = i
            while((self._data[j]<self._data[j-1]) and j > 0):
                temp = self._data[j-1]
                self._data[j-1] = self._data[j]
                self._data[j] = temp
                j -= 1
        return self._data
    def enqueue(self, element):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        if self.is_empty():
            self._data[self._front] = element
            self._size += 1
        else:
            avail = (self._front + self._size) % len(self._data)
            self._data[avail] = element
            self._insertion_sort()
            self._front = self._data.index(min(self._data))
            self._size += 1
    def _resize(self, cap):
        old = self. data
        self._data = [None]*cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk] 
            walk = (1 + walk) % len(old)
        self._front = 0




