class Empty(Exception):
    pass
    

class Queue:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._queue = [None]*Queue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def first(self):
        if self.is_empty():
            raise Empty('Empty Queue')
        return self._queue[self._front]
    def dequeue(self):
        if self.is_empty():
            raise Empty('Empty Queue')
        element = self._queue[self._front]
        self._queue[self._front] = None
        self._front = (self._front + 1) % len(self._queue)
        self._size -= 1
        return element
    def enqueue(self, element):
        if self._size == len(self._queue):
            self._resize(2*len(self._queue))
        avail = (self._front + self._size) % len(self._queue)
        self._queue[avail] = element
        self._size += 1
    def _resize(self, cap):
        old = self._queue
        self._queue = [None]*cap
        walk = self._front
        for k in range(self._size):
            self._queue[k] = old[walk] 
            walk = (1 + walk) % len(old)
        self._front = 0
    def __str__(self):
        return str(self._queue)


def children(T, parent):
    return (T[parent])