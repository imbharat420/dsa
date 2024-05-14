from Sll2 import *
class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.item_count=0
    def is_empty(self):
        return super().is_empty()
    def push(self,item):
        self.insert_at_start(item)
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
            self.delete_first()
            self.item_count-=1
        else:
            raise IndexError("Stack is underflow")
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack is underflow")
    def size(self):
        return self.item_count
cls =Stack()
cls.push(29)
cls.push(49)
cls.push(59)
# cls.pop()
print(cls.peek())
print(cls.size())


