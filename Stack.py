class Empty(Exception):
    pass
    

###### Implementing Stack #####

class Stack:
    def __init__(self):
        self._stack = []
    def __len__(self):
        return len(self._stack)
    def is_empty(self):
        return len(self._stack) == 0
    def push(self, element):
        self._stack.append(element)
    def pop(self):
        if self.is_empty():
            raise Empty('Empty Stack')
        return self._stack.pop()
    def top(self):
        if self.is_empty():
            raise Empty('Empty Stack')
        return self._stack[-1]
    def inIt(self, element):
        return element in self._stack