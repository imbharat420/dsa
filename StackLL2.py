from Sll2 import *

class Stack:
    def __init__(self):
        self.myItem=SLL()
        self.item_count=0
    def is_empty(self):
        return self.myItem.start==None
    def push(self,item):
        self.myItem.insert_at_start(item)
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
            data = self.myItem.start.item
            self.myItem.delete_first()
            self.item_count-=1
            return data
    def peek(self):
        if not self.is_empty():
            return self.myItem.start.item
    def size(self):
        return self.item_count
cls = Stack()
cls.push(10)
cls.push(20)
cls.push(40)
cls.pop()
print(cls.peek())
print(cls.size())