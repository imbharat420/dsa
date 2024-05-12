class Stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self,item):
        self.append(item)
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is empty")
    def size(self):
        return len(self)

    def insert(self,index,data):
        raise AttributeError("No attribute 'insert' at stack")
cls=Stack()
cls.push(20)
cls.push(40)
cls.pop()
print(cls.peek())
print(cls.size())
