class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit
        pass

    def isEmpty(self):
        return len(self.items) == 0
    pass

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            print("Stack is full.")    
        pass

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Stack is empty")
    pass

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("Stack is empty")
    pass
    
    def size(self):
        return len(self.items)
    pass

    def full(self):
        return len(self.items) == self.limit
    pass

    def search(self, target):
        if target in self.items:
            return len(self.items) - self.items.index(target) - 1
        else:
            return -1
    pass
