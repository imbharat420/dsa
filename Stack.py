class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")
    def push(self,item):
        self.items.append(item)

cls = Stack()

cls.push(1)
cls.push(4)
cls.push(3)
cls.push(53)
print(cls.is_empty())
cls.pop()
cls.pop()
print(cls.peek())

print(cls.size())